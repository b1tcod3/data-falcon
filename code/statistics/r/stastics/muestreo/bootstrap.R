## Histograma
library(boot)
library(ggplot2)
# leyendo data
PSDS_PATH <- file.path(getwd())

loans_income <- read.csv(file.path(PSDS_PATH, 'data', 'loans_income.csv'))
loans_income <- loans_income[, 1]   # convert data frame to vector

## The Bootstrap
# As the calculation uses random samples, results will vary between runs

x <- seq(from=-3, to=3, length=300)

stat_fun <- function(x, idx) median(x[idx])
boot_obj <- boot(loans_income, R=1000, statistic=stat_fun)

boot_obj