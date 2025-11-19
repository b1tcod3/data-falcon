## Histograma
library(boot)
library(ggplot2)

norm_samp <- rnorm(100)
qqnorm(norm_samp, main='', xlab='Quantile of normal distribution', ylab='z-score')
abline(a=0, b=1, col='grey')