
#####################################################
## AB Testing  - Paired Samples T-Test
#####################################################


## Import Required Packages

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel, norm

## Create Mock Data

before = norm.rvs(loc = 500, scale = 100, size = 100, random_state = 42).astype(int)

np.random.seed(42)
after = before + np.random.randint(low = -50, high = 75, size = 100)

plt.hist(before, density = True, alpha = 0.5, label = "Before")
plt.hist(after, density = True, alpha = 0.5, label = "After")
plt.legend()
plt.show()

before_mean = before.mean()
after_mean = after.mean()
print(before_mean, after_mean)


## Set the Hypothesis and Acceptance Criteria 

null_hypothesis = "The mean of the before sample is equal to the mean of the after sample."
alternate_hypothesis = "The mean of the before sample is different to the mean of the after sample."
acceptance_criteria = 0.05

## Exceute the Hypothesis Test

t_statistic, p_value = ttest_rel(before, after)
print(t_statistic, p_value)

## Print the Results (p-value)

if p_value <= acceptance_criteria:
    print(f"As our p-value of {round(p_value, 4)} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p-value of {round(p_value, 4)} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}")
    



























































































































