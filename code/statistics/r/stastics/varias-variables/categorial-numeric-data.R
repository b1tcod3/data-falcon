library(gmodels)
library(ggplot2)

PSDS_PATH <- file.path(dirname(dirname(getwd())))

airline_stats <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'airline_stats.csv'), stringsAsFactors = FALSE)
lc_loans <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'lc_loans.csv'))

### Two Categorical Variables
# Load the `lc_loans` dataset

x_tab <- CrossTable(lc_loans$grade, lc_loans$status, 
                    prop.c=FALSE, prop.chisq=FALSE, prop.t=FALSE)

### Categorical and Numeric Data
# Boxplots of a column can be grouped by a different column.

boxplot(pct_carrier_delay ~ airline, data=airline_stats, ylim=c(0, 50), 
        cex.axis=.6, ylab='Daily % of Delayed Flights')

# Variation of boxplots called _violinplot_.

graph <- ggplot(data=airline_stats, aes(airline, pct_carrier_delay)) + 
  geom_violin(draw_quantiles = c(.25,.5,.75), linetype=2) +
  geom_violin(fill=NA, size=1.1) +
  coord_cartesian(ylim=c(0, 50)) +
  labs(x='', y='Daily % of Delayed Flights') +
  theme_bw()
graph