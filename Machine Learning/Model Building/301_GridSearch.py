

####################################################
## GRidSearch - Basic Template
####################################################


## Import Required Python Packages

from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import GridSearchCV


## Import Sample Data

my_df = pd.read_csv("data/sample_data_regression.csv")


## Split data into input and output objects (X is input variables, y is output variable)

X = my_df.drop(["output"], axis = 1)
y = my_df["output"]


## Instatiate our GridSearch object

gscv = GridSearchCV(
    estimator = RandomForestRegressor(random_state = 42),
    param_grid = {"n_estimators" : [10, 50, 100, 500],
                  "max_depth" : [1,2,3,4,5,6,7,8,9,None]},
    cv = 5,
    scoring = "r2",
    n_jobs = -1
    )


## Fit to Data

gscv.fit(X, y)


## Get the best CV score (mean)

gscv.best_score_


## Optimal Paramaters

gscv.best_params_


## Create optimal model object

regressor = gscv.best_estimator_





































































