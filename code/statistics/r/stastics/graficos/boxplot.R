## Histograma

# leyendo data
PSDS_PATH <- file.path(getwd())

dfw <- read.csv(file.path(PSDS_PATH, 'data', 'dfw_airline.csv'))

barplot(as.matrix(dfw) / 6, cex.axis=0.8, cex.names=0.7, 
        xlab='Cause of delay', ylab='Count')
