# Import the datasets needed for chapter 1

PSDS_PATH <- file.path(dirname(dirname(getwd())))

state <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'state.csv'))

## Estimates of Variability

sd(state[['Population']])
IQR(state[['Population']])
mad(state[['Population']])