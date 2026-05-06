# Import the datasets needed for chapter 1

PSDS_PATH <- file.path(dirname(dirname(getwd())))

state <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'state.csv'))

### Frequency Table and Histograms

breaks <- seq(from=min(state[['Population']]), 
              to=max(state[['Population']]), length=11)

pop_freq <- cut(state[['Population']], breaks=breaks, 
                right=TRUE, include.lowest=TRUE)

breaks
state['PopFreq'] <- pop_freq
table(pop_freq)

options(scipen=5)
hist(state[['Population']], breaks=breaks)