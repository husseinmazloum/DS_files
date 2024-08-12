

#########################################################
## Random Forest for Classification - ABC Grocery Task
#########################################################



######################################################################
## Import Required Packages
######################################################################

import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.inspection import permutation_importance
## from sklearn.feature_selection import RFECV


######################################################################
## Import Sample Data
######################################################################


## Import

data_for_model = pd.read_pickle("data/abc_classification_modelling.p")

## Drop Unneccessary columns

data_for_model.drop(["customer_id"], axis = 1, inplace = True)

## Shuffle Data

data_for_model = shuffle(data_for_model, random_state = 42)

## Class Balance

data_for_model["signup_flag"].value_counts(normalize = True)

######################################################################
## Deal with Missing Values
######################################################################

data_for_model.isna().sum()
data_for_model.dropna(how = "any", inplace = True)


######################################################################
## Deal with Outliers - Not Really needed for decision trees
######################################################################



######################################################################
## Split Input Variables and Output Variable
######################################################################

X = data_for_model.drop(["signup_flag"], axis = 1)
y = data_for_model["signup_flag"]

######################################################################
## Split out Training and Test Sets
######################################################################

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify = y)

######################################################################
## Deal with Categorical Variables
######################################################################

categorical_vars = ["gender"]

one_hot_encoder = OneHotEncoder(sparse_output=False, drop="first")

X_train_encoded = one_hot_encoder.fit_transform(X_train[categorical_vars])
X_test_encoded = one_hot_encoder.transform(X_test[categorical_vars])

encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

X_train_encoded = pd.DataFrame(X_train_encoded, columns=encoder_feature_names)
X_train = pd.concat([X_train.reset_index(drop=True), X_train_encoded.reset_index(drop=True)], axis = 1)
X_train.drop(categorical_vars, axis = 1, inplace = True)

X_test_encoded = pd.DataFrame(X_test_encoded, columns=encoder_feature_names)
X_test = pd.concat([X_test.reset_index(drop=True), X_test_encoded.reset_index(drop=True)], axis = 1)
X_test.drop(categorical_vars, axis = 1, inplace = True)

######################################################################
## Feature Selection - Only useful for decision trees when there are many input variables, to reduce
## noise and for computational speed.
######################################################################

"""
clf = LogisticRegression(random_state = 42, max_iter = 1000)
feature_selector = RFECV(clf)

fit = feature_selector.fit(X_train, y_train)

optimal_feature_count = feature_selector.n_features_
print(f"Optimal number of features: {optimal_feature_count}")

X_train = X_train.loc[:, feature_selector.get_support()]
X_test = X_test.loc[:, feature_selector.get_support()]

plt.plot(range(1, len(fit.cv_results_['mean_test_score']) + 1), fit.cv_results_['mean_test_score'], marker = "o")
plt.ylabel("Model Score")
plt.xlabel("Number of Features")
plt.title(f"Feature Selection using RFE \n Optimal Number of Features is: {optimal_feature_count} (at score of {round(max(fit.cv_results_['mean_test_score']),4)})")
plt.tight_layout()
plt.show()
"""

######################################################################
## Model Training
######################################################################

clf = RandomForestClassifier(random_state = 42, n_estimators = 500, max_features = 5)
clf.fit(X_train, y_train)

######################################################################
## Model Assessment
######################################################################


## Assess model accuracy

y_pred_class = clf.predict(X_test)
y_pred_prob = clf.predict_proba(X_test)[:,1]


## Confusion Matrix

conf_matrix = confusion_matrix(y_test, y_pred_class)
print(conf_matrix)

## Plot Confusion Matrix


plt.style.available

plt.style.use("seaborn-v0_8-poster")
plt.matshow(conf_matrix, cmap = "coolwarm")
plt.gca().xaxis.tick_bottom()
plt.title("Confusion Matrix")
plt.ylabel("Actual Class")
plt.xlabel("Predicted Class")
for (i, j), corr_value in np.ndenumerate(conf_matrix):
    plt.text(j, i, corr_value, ha = "center", va = "center", fontsize = 20)
plt.show()



## Accuracy (the number of correct classifications out of all the attempted classifications)

accuracy_score(y_test, y_pred_class)


## Precision (of all observations that were predicted as positive, how many were actually positive)

precision_score(y_test, y_pred_class)


## Recall (of all positive observations, how many did we predict as positive)

recall_score(y_test, y_pred_class)


## F1-Score (the harmonic mean of precision and recall)

f1_score(y_test, y_pred_class)


## Feature Importance

clf.feature_importances_

feature_importance = pd.DataFrame(clf.feature_importances_)
feature_names = pd.DataFrame(X.columns)

feature_importance_summary = pd.concat([feature_names, feature_importance], axis = 1)
feature_importance_summary.columns = ["input_variable", "feature_importance"]
feature_importance_summary.sort_values(by = "feature_importance", inplace = True)

## Plot Feature Importance 

plt.barh(feature_importance_summary["input_variable"], feature_importance_summary["feature_importance"])
plt.title("Feature Importance of Random Forest")
plt.xlabel("Feature Importance")
plt.tight_layout()
plt.show()

## Permutation Importance

result = permutation_importance(clf, X_test, y_test, n_repeats = 10, random_state = 42)

permutation_importance = pd.DataFrame(result["importances_mean"])
feature_names = pd.DataFrame(X.columns)

permutation_importance_summary = pd.concat([feature_names, permutation_importance], axis = 1)
permutation_importance_summary.columns = ["input_variable", "permutation_importance"]
permutation_importance_summary.sort_values(by = "permutation_importance", inplace = True)

## Plot Permutation Importance 

plt.barh(permutation_importance_summary["input_variable"], permutation_importance_summary["permutation_importance"])
plt.title("Permutation Importance of Random Forest")
plt.xlabel("Permutation Importance")
plt.tight_layout()
plt.show()


















































































