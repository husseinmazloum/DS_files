

#######################################################
## Random Forest for Classification - Basic Template
#######################################################


## Import Required Python Packages

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


## Import Sample Data

my_df = pd.read_csv("data/sample_data_classification.csv")


## Split data into input and output objects (X is input variables, y is output variable)

X = my_df.drop(["output"], axis = 1)
y = my_df["output"]


## Split data into training and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify = y)


## Instantiate our model object

clf = RandomForestClassifier(random_state = 42)


## Train our model

clf.fit(X_train, y_train)


## Assess model accuracy

y_pred = clf.predict(X_test)
accuracy_score(y_test, y_pred)


















































































