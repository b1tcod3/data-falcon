# Import the datasets needed for chapter 1

PSDS_PATH <- file.path(dirname(dirname(getwd())))

state <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'state.csv'))

### Density Estimates
# Density is an alternative to histograms that can provide more insight into the distribution of the data points.

hist(state[['Murder.Rate']], freq=FALSE )
lines(density(state[['Murder.Rate']]), lwd=3, col='blue')