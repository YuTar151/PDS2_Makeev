from scipy.stats import binom

n = 100
p = 0.9
lower_bound = 85
upper_bound = 95

prob = binom.cdf(upper_bound, n, p) - binom.cdf(lower_bound - 1, n, p)

print("The probability that the number of televisions that last the warranty period will be within [85;95] is:", prob)







