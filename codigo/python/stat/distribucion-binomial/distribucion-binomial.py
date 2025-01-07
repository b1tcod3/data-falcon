import scipy.stats as stats

print(stats.binom.pmf(2, n=5, p=0.1))

print(stats.binom.cdf(2, n=5, p=0.1))

# 0.07289999999999992
# 0.99144