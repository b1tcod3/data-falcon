# Los Retos de la Materia Prima

Si en la fase anterior definimos el objetivo estratégico, en esta fase analizamos la **materia prima** con la que vamos a construir la solución. Es extremadamente raro que los datos existentes se alineen a la perfección con el problema de negocio actual, principalmente porque la información histórica se suele recolectar para propósitos completamente ajenos (o sin un fin claro en mente).

Durante esta etapa, el equipo debe evaluar críticamente tres factores sobre las fuentes de datos disponibles (como bases de datos de clientes, transacciones o marketing).

## Disparidad e Inconsistencia

Diferentes bases de datos contienen información distinta, cubren poblaciones que a veces solo se intersectan parcialmente y poseen niveles variables de confiabilidad.

- **Cobertura parcial:** La base de clientes puede tener datos de unos 10,000 usuarios, mientras que la base de transacciones cubre 8,000. ¿Qué pasó con los otros 2,000?
- **Campos inconsistentes:** Una base define "ingreso" como ingreso bruto anual, otra como ingreso neto mensual.
- **Confiabilidad variable:** Datos de facturación suelen ser más precisos que datos de encuestas o de comportamiento web.

## El Costo del Acceso

No todos los datos son igual de accesibles:

| Tipo de acceso | Descripción | Ejemplo |
|---------------|-------------|---------|
| **Gratuito** | Datos ya disponibles en la organización sin esfuerzo adicional | Base de datos transaccional principal |
| **Costo medio** | Requieren esfuerzo de extracción, integración o compra | Datos de proveedores externos, APIs |
| **Costo alto** | Requieren proyectos paralelos para empezar a recolectarlos | Encuestas a clientes, sensores IoT |
| **No existen** | Simplemente no se han recolectado nunca | Historial de interacciones con servicio al cliente |

Una tarea crítica en esta fase es estimar cuidadosamente los costos y beneficios de cada fuente de datos para decidir si realmente vale la pena hacer una inversión adicional en ella.

## El Dolor de la Integración

Unificar bases de datos separadas suele ser caótico porque los registros de clientes y los identificadores de productos son notoriamente variables y ruidosos.

- **Emparejamiento de registros:** ¿"Juan Pérez" en una base es la misma persona que "J. Pérez" en otra? ¿O son dos personas distintas?
- **Identificadores inconsistentes:** El mismo producto puede tener códigos distintos en diferentes sistemas.
- **Problemas de calidad:** Limpiar y emparejar registros para asegurar que exista una única entrada por cliente es, por sí mismo, un problema analítico complejo.

De hecho, este proceso —conocido como *record linkage* o *entity resolution*— es una de las tareas más demandantes en la práctica y puede consumir gran parte del tiempo del proyecto.

## Relación con otras fases

Los hallazgos de esta fase pueden obligar a regresar a la [Comprensión del Negocio](../fase-1-comprension-del-negocio/01-el-arte-de-traducir-el-problema.md): si los datos necesarios no existen o son inaccesibles, puede ser necesario ajustar el objetivo o el escenario de uso. Esta retroalimentación es parte natural del [proceso iterativo de CRISP-DM](../../intro-ciencia-datos/04-el-proceso-de-ciencia-de-datos.md).
