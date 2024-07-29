


sample_mean = 176
sample_STD = 14
sample_size = 10000
z_score = 1.96 ## Use 1.96 for a 95% Confidence level


confidence_range1 = sample_mean - z_score * (sample_STD / (sample_size**0.5))
confidence_range2 = sample_mean + z_score * (sample_STD / (sample_size**0.5))

result = f"Based on our sample, we are 95% confident that the mean height of US men, falls between {round(confidence_range1, 2)}cm and {round(confidence_range2, 2)}cm"
print(result)



 









 









 









 









 









 









 









 
