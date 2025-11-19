# Import the datasets needed for chapter 1

PSDS_PATH <- file.path(dirname(dirname(getwd())))

state <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'state.csv'))

## Estimates of Location
### Example: Location Estimates of Population and Murder Rates

# Table 1-2
state_asc <- state
state_asc[['Population']] <- formatC(state_asc[['Population']], format='d', digits=0, big.mark=',')
state_asc[1:8,]

mean(state[['Population']])
mean(state[['Population']], trim=0.1)
median(state[['Population']])

weighted.mean(state[['Murder.Rate']], w=state[['Population']])
library('matrixStats')
weightedMedian(state[['Murder.Rate']], w=state[['Population']])