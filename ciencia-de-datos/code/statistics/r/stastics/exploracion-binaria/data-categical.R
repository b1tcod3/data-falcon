# Import the datasets needed for chapter 1

PSDS_PATH <- file.path(dirname(dirname(getwd())))

dfw <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'dfw_airline.csv'))

## Exploring Binary and Categorical Data

dfw

barplot(as.matrix(dfw) / 6, cex.axis=0.8, cex.names=0.7, 
        xlab='Cause of delay', ylab='Count')