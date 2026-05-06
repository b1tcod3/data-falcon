library(ggplot2)

session_times <- read.csv('/home/data/Documentos/practical-statistics-for-data-scientists-master/data/web_page_data.csv')
head(session_times)
session_times[,2] <- session_times[,2] * 100

mean_a <- mean(session_times[session_times['Page'] == 'Page A', 'Time'])
mean_b <- mean(session_times[session_times['Page'] == 'Page B', 'Time'])

## Permutation test example with stickiness
perm_fun <- function(x, nA, nB)
{
  n <- nA + nB
  idx_b <- sample(1:n, nB)
  idx_a <- setdiff(1:n, idx_b)
  mean_diff <- mean(x[idx_b]) - mean(x[idx_a])
  return(mean_diff)
}


set.seed(1)
perm_diffs <- rep(0, 1000)
for (i in 1:1000) {
  perm_diffs[i] = perm_fun(session_times[, 'Time'], 21, 15)
}
par(mar=c(4,4,1,0)+.1)
hist(perm_diffs, xlab='Session time differences (in seconds)', main='')
abline(v=mean_b - mean_a, lty=2, lwd=1.5)
text('  Observed\n  difference', x=mean_b - mean_a,  y=par()$usr[4]-20, adj=0)

mean(perm_diffs > (mean_b - mean_a))

