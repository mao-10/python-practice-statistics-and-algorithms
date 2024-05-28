#may 28, 2024
#module 4 practice

from statsmodels.stats.weightstats import ztest

sample1 = [21, 28, 40, 55, 58, 60]
sample2 = [13, 29, 50, 55, 71, 90]

print(ztest(x1 = sample1, x2 = sample2))
