# Import the datasets needed for chapter 1

PSDS_PATH <- file.path(dirname(dirname(getwd())))

state <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'state.csv'))

### Percentiles and Boxplots

quantile(state[['Murder.Rate']], p=c(.05, .25, .5, .75, .95))

boxplot(state[['Population']]/1000000, ylab='Population (millions)')