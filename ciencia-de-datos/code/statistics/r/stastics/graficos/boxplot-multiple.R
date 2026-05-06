## Histograma

# leyendo data
PSDS_PATH <- file.path(getwd())

airline_stats <- read.csv(file.path(PSDS_PATH, 'data',
 'airline_stats.csv'),
 stringsAsFactors = FALSE)

boxplot(pct_carrier_delay ~ airline, data=airline_stats, ylim=c(0, 50), 
        cex.axis=.6, ylab='Daily % of Delayed Flights')
