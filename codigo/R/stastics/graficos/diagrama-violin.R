## Diagrama de Violín
library(ggplot2)

# leyendo data
PSDS_PATH <- file.path(getwd())

airline_stats <- read.csv(file.path(PSDS_PATH, 'data',
 'airline_stats.csv'),
 stringsAsFactors = FALSE)

graph <- ggplot(data=airline_stats, aes(airline, pct_carrier_delay)) + 
  geom_violin(draw_quantiles = c(.25,.5,.75), linetype=2) +
  geom_violin(fill=NA, size=1.1) +
  coord_cartesian(ylim=c(0, 50)) +
  labs(x='', y='Daily % of Delayed Flights') +
  theme_bw()
graph

