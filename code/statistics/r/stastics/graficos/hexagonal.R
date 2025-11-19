## Hexagonal
library(ggplot2)

# leyendo data
PSDS_PATH <- file.path(getwd())

kc_tax <- read.csv(file.path(PSDS_PATH, 'data', 'kc_tax.csv.gz'))

kc_tax0 <- subset(kc_tax, TaxAssessedValue < 750000 & 
                  SqFtTotLiving > 100 &
                  SqFtTotLiving < 3500)

