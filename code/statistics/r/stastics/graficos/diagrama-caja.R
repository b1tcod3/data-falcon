## diagrama de cajas en R

# leyendo data
PSDS_PATH <- file.path(getwd())
state <- read.csv(file.path(PSDS_PATH, 'data', 'state.csv'))

# diagrama de cajas
boxplot(state[['Population']]/1000000, ylab='Population (millions)')

