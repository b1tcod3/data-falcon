import torch
import pyro
import pyro.distributions as dist
import pyro.infer as infer
import pyro.optim as optim
import matplotlib.pyplot as plt

# Configuramos Pyro para tener salidas limpias
pyro.set_rng_seed(1)
pyro.clear_param_store()

# 1. Datos simulados (y = 0.5x + 0.3 + ruido)
X = torch.randn(100)
a_true = 0.5
b_true = 0.3
y_data = a_true * X + b_true + torch.randn(100) * 0.1 # Añadimos ruido

# Definición del Modelo
def model(X, y=None):
    # 1. Priores: Definimos nuestras creencias iniciales sobre los parámetros 'a' y 'b'.
    # Suponemos que 'a' y 'b' siguen una distribución Normal (Gaussianos).
    a = pyro.sample("a", dist.Normal(0., 1.)) # Prior para la pendiente (media 0, desviación 1)
    b = pyro.sample("b", dist.Normal(0., 1.)) # Prior para la intersección (media 0, desviación 1)

    # 2. Verosimilitud (Likelihood): La predicción y cómo se compara con los datos.
    # Usamos la regresión lineal: y_pred = a * X + b
    y_pred = a * X + b

    # Suponemos que el error (la diferencia entre y_data y y_pred)
    # sigue una distribución Normal.
    with pyro.plate("data", len(X)):
        # Observamos los datos 'y_data' condicionados a la predicción
        pyro.sample("obs", dist.Normal(y_pred, 0.1), obs=y)

    # La salida 'obs' con el argumento 'obs=y' es donde el modelo se "conecta"
    # con los datos reales y realiza la actualización bayesiana.

# Definición de la Guía (Aproximación del Posterior)
def guide(X, y=None):
    # Definimos los parámetros variacionales que Pyro optimizará.
    # Para cada parámetro (a, b), queremos aprender su media (loc) y desviación estándar (scale)
    
    # Parámetros para 'a' (la pendiente)
    a_loc = pyro.param('a_loc', torch.tensor(0.0))
    a_scale = pyro.param('a_scale', torch.tensor(1.0), constraint=dist.constraints.positive)
    pyro.sample("a", dist.Normal(a_loc, a_scale))

    # Parámetros para 'b' (la intersección)
    b_loc = pyro.param('b_loc', torch.tensor(0.0))
    b_scale = pyro.param('b_scale', torch.tensor(1.0), constraint=dist.constraints.positive)
    pyro.sample("b", dist.Normal(b_loc, b_scale))
    
    # Después del entrenamiento, 'a_loc' y 'b_loc' serán las medias del Posterior,
    # y 'a_scale' y 'b_scale' serán la incertidumbre (desviación estándar).

# 1. Configurar el optimizador
optimizer = optim.Adam({"lr": 0.01})

# 2. Configurar el SVI
# El 'ELBO' (Evidence Lower Bound) es la función de costo que se minimiza
svi = infer.SVI(model, 
                guide, 
                optimizer, 
                loss=infer.Trace_ELBO())

# 3. Bucle de entrenamiento
n_steps = 1000
losses = []

for step in range(n_steps):
    loss = svi.step(X, y_data)
    losses.append(loss)
    if step % 100 == 0:
        print(f"Paso {step:4d} Pérdida (ELBO): {loss:.2f}")

print("\n--- Entrenamiento Completado ---")

# Extraer los parámetros Posteriores (las medias y desviaciones finales)
a_loc = pyro.param("a_loc").item()
a_scale = pyro.param("a_scale").item()
b_loc = pyro.param("b_loc").item()
b_scale = pyro.param("b_scale").item()

print(f"Valor Real (a_true): {a_true:.3f}")
print(f"Posterior para la pendiente 'a': Media = {a_loc:.3f}, Desv. Est. = {a_scale:.3f}")
print("---")
print(f"Valor Real (b_true): {b_true:.3f}")
print(f"Posterior para la intersección 'b': Media = {b_loc:.3f}, Desv. Est. = {b_scale:.3f}")

# El a_loc y b_loc deberían estar muy cerca de los valores reales (0.5 y 0.3).
# El a_scale y b_scale representan la incertidumbre (cuán "ancha" es la distribución).

# 6. Muestreo del Posterior para la Predicción
# La clave de las BNN es que, para hacer una predicción, muestreamos MÚLTIPLES veces
# de la distribución Posterior y promediamos, o usamos la distribución de esas predicciones.

n_samples = 1000
predictions = []

# No necesitamos el gradiente en el muestreo, así que lo desactivamos
with torch.no_grad():
    for _ in range(n_samples):
        # La guía ahora nos da muestras del posterior aproximado.
        # En Pyro, para muestrear desde la guía entrenada, simplemente la llamamos.
        # No necesitamos pasar `obs` porque no estamos entrenando.
        a_sample = pyro.sample("a", dist.Normal(a_loc, a_scale))
        b_sample = pyro.sample("b", dist.Normal(b_loc, b_scale))

        y_pred_sample = a_sample * X + b_sample
        predictions.append(y_pred_sample.numpy())


# (Opcional) Visualización de la incertidumbre
plt.figure(figsize=(10, 6))
plt.scatter(X.numpy(), y_data.numpy(), label="Datos reales", color='blue', alpha=0.6)

# Trazamos la línea media (predicción promedio)
import numpy as np
mean_prediction = np.mean(predictions, axis=0)
plt.plot(X.numpy(), mean_prediction, color='red', label="Predicción Media (BNN)")

# Trazamos la banda de incertidumbre (ej. ± 2 desviaciones estándar)
std_prediction = np.std(predictions, axis=0)
plt.fill_between(X.numpy(), 
                 mean_prediction - 2*std_prediction, 
                 mean_prediction + 2*std_prediction, 
                 color='red', alpha=0.2, label="Incertidumbre (95% CI)")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Regresión Lineal Bayesiana: Predicción e Incertidumbre")
plt.legend()
plt.show()
