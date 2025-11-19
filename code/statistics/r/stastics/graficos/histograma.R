## Histograma

# leyendo data
PSDS_PATH <- file.path(getwd())
state <- read.csv(file.path(PSDS_PATH, 'data', 'state.csv'))

breaks <- seq(from=min(state[['Population']]), 
              to=max(state[['Population']]), length=11)

options(scipen=5)
#hist(state[['Population']], breaks=breaks)

# densidad

hist(state[['Murder.Rate']], freq=FALSE )
lines(density(state[['Murder.Rate']]), lwd=3, col='blue')
