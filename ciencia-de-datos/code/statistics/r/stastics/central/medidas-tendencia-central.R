## medidas tendencia central en R

library(matrixStats)

#leyendo data
PSDS_PATH <- file.path(dirname(dirname(getwd())))
state <- read.csv(file.path(PSDS_PATH, 'data', 'state.csv'))

#media y media truncada
mean(state[['Population']])
mean(state[['Population']], trim=0.1)

#media ponderada
weighted.mean(state[['Murder.Rate']], w=state[['Population']])

#mediana
median(state[['Population']])
#mediana ponderada
weightedMedian(state[['Murder.Rate']], w=state[['Population']])

