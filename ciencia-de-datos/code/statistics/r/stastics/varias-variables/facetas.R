library(ggplot2)

PSDS_PATH <- file.path(dirname(dirname(getwd())))

kc_tax <- read.csv(file.path(PSDS_PATH, 'data-falcon/codigo/practical-statistics-for-data-scientists-master/data', 'kc_tax.csv.gz'))

## Exploring Two or More Variables
# Load the kc_tax dataset and filter based on a variety of criteria

kc_tax0 <- subset(kc_tax, TaxAssessedValue < 750000 & 
                  SqFtTotLiving > 100 &
                  SqFtTotLiving < 3500)



graph <- ggplot(subset(kc_tax0, ZipCode %in% c(98188, 98105, 98108, 98126)),
                aes(x=SqFtTotLiving, y=TaxAssessedValue)) + 
  stat_binhex(colour='white') + 
  theme_bw() + 
  scale_fill_gradient(low='gray95', high='black') +
  scale_y_continuous(labels = function(x) format(x, scientific = FALSE)) +
  labs(x='Finished Square Feet', y='Tax-Assessed Value') +
  facet_wrap('ZipCode')
graph