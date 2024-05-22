# statistics class module 2 practice problems

import scipy.stats as st

# normal distribution
#critical score, mean, std
print("Normal distribution\n")
print(st.norm.cdf(62, 55, 7.5))
print(st.norm.sf(51, 55, 7.5))
print(st.norm.cdf(60, 55, 7.5) - st.norm.cdf(49, 55, 7.5))
print(st.norm.ppf(0.8247, 55, 7.5))
print(st.norm.isf(0.95, 55, 7.5))


#student's t-distribution
# critical score, sample size - 1, mean, std
print("\n")
print("Student's t-distribution\n")
# cdf - less than
print(st.t.cdf(62, 24, 55, 7.5))
# sf - greater than
print(st.t.sf(51, 24, 55, 7.5))
# between
print(st.t.cdf(60, 24, 55, 7.5) - st.t.cdf(49, 24, 55, 7.5))
# known probability (less than)
print(st.t.ppf(0.8247, 24, 55, 7.5))
# known probability (greater than)
print(st.t.isf(0.95, 24, 55, 7.5))

# pdf = ???
print(st.t.pdf(-0.185, 30, 0, 1))
