## tabla de frecuencias

# leyendo data
PSDS_PATH <- file.path(getwd())
state <- read.csv(file.path(PSDS_PATH, 'data', 'state.csv'))

breaks <- seq(from=min(state[['Population']]), 
              to=max(state[['Population']]), length=11)
pop_freq <- cut(state[['Population']], breaks=breaks, 
                right=TRUE, include.lowest=TRUE)
table(pop_freq)

