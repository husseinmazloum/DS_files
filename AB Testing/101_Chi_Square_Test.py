
#####################################################
## AB Testing  - Our Task for ABC Grocery
#####################################################


## Import Required Packages

import pandas as pd
from scipy.stats import chi2_contingency, chi2

## Import Data

campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name="campaign_data")


## Filter Our Data

campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]

## Summarise to get our Observed Frequencies

observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values

mailer1_signup_rate = 123 / (252 + 123)
mailer2_signup_rate = 127 / (209 + 127)
print(mailer1_signup_rate, mailer2_signup_rate)

## State Hypothesis and Set Acceptance Criteria 

null_hypothesis = "There is no relationship between mailer type and signup rate. They are independent."
alternate_hypothesis = "There is a relationship between mailer type and signup rate. They are not independent."
acceptance_criteria = 0.05

## Calculate Expected Frequencies and CHI Square Statistic

chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction=False)
print(chi2_statistic, p_value)

## Find the Critical Value For Our Test

critical_value = chi2.ppf(1 - acceptance_criteria, dof)
print(critical_value)

## Print the Results (Chi Square Statistic)

if chi2_statistic >= critical_value:
    print(f"As our chi-square statistic of {chi2_statistic} is higher than our critical value of {critical_value} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our chi-square statistic of {chi2_statistic} is lower than our critical value of {critical_value} - we retain the null hypothesis, and conclude that: {null_hypothesis}")
    
## Print the Results (p-Value)

if p_value <= acceptance_criteria:
    print(f"As our p-value of {p_value} is lower than our acceptance criteria of {acceptance_criteria} - we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    print(f"As our p-value of {p_value} is higher than our acceptance criteria of {acceptance_criteria} - we retain the null hypothesis, and conclude that: {null_hypothesis}")
    


























































