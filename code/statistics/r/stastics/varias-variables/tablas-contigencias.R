## Hexagonal
library(descr)

# leyendo data
PSDS_PATH <- file.path(getwd())

lc_loans <- read.csv(file.path(PSDS_PATH, 'data', 'lc_loans.csv'))

x_tab <- CrossTable(lc_loans$grade, lc_loans$status, 
                    prop.c=FALSE, prop.chisq=FALSE, prop.t=FALSE)

x_tab