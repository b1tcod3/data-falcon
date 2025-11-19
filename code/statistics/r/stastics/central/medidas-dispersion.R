## medidas de dispersion en R

# leyendo data
PSDS_PATH <- file.path(dirname(dirname(getwd())))
state <- read.csv(file.path(PSDS_PATH, 'data', 'state.csv'))

# desviacion estandar
sd(state[['Population']])

# Rango intercuartílico
IQR(state[['Population']])

# desviacion absoluta mediana de la mediana 
mad(state[['Population']])