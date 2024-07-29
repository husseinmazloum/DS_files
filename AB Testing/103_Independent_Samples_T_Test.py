
#####################################################
## AB Testing  - Independent Samples T-Test
#####################################################


## Import Required Packages

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm

## Create Mock Data

sample_a = norm.rvs(loc = 500, scale = 100, size = 250, random_state = 42).astype(int)
sample_b = norm.rvs(loc = 550, scale = 150, size = 100, random_state = 42).astype(int)

plt.hist(sample_a, density = True, alpha = 0.5)
plt.hist(sample_b, density = True, alpha = 0.5)
plt.show()

sample_a_mean = sample_a.mean()
sample_b_mean = sample_b.mean()
print(sample_a_mean, sample_b_mean)


## Set the Hypothesis and Acceptance Criteria 

null_hypothesis = "The mean of Sample A is equal to the mean of Sample B."
alternate_hypothesis = "The mean of Sample A is different to the mean of Sample B."
acceptance_criteria = 0.05

## Exceute the Hypothesis Test

t_statistic, p_value = ttest_ind(sample_a, sample_b)
print(t_statistic, p_value)

## Print the Results (p-value)

if p_value <= acceptance_criteria:
    print(f"As our p-value of {round(p_value, 4)} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p-value of {round(p_value, 4)} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}")
    

## Welch's T-test (This one is better) - equal_var parameter in the test is the only difference

## Exceute the Hypothesis Test

t_statistic, p_value = ttest_ind(sample_a, sample_b, equal_var=False)
print(t_statistic, p_value)

## Print the Results (p-value)

if p_value <= acceptance_criteria:
    print(f"As our p-value of {round(p_value, 4)} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p-value of {round(p_value, 4)} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}")
    












































































