import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics
from sklearn.pipeline import Pipeline
import seaborn as sns
import matplotlib.pyplot as plt

print(os.getcwd())
output_directory = "Desktop/ischool/is477-fall2023-final-project/results"
output_file_path = os.path.join(output_directory, "results.txt")


# read in data
df = pd.read_csv('Desktop/ischool/is477-fall2023-final-project/data/Rice_Cammeo_Osmancik.csv') # only contains numerical data
df = df.dropna() # no na values as suggested in csv
features = ["Area Integer", "Perimeter Real", "Major_Axis_Length Real", "Minor_Axis_Length Real", 
            "EccentricityReal", "Convex_AreaInteger", "Extent Real"]
df['Class'] = df['Class'].map({'Cammeo': 0, 'Osmancik': 1}) # convert class to binary

# summary statistics
stats = df.describe()
print(stats)

# train-test split
X_train, X_test, y_train, y_test = train_test_split(df[features], df['Class'], test_size=0.2, random_state=42)

# Logistic Regression
pipe = Pipeline([('estimator', LogisticRegression())])

param_grid = {'estimator__C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
              'estimator__class_weight': ['balanced', None], 
              'estimator__penalty': ['l1', 'l2'],
              'estimator__solver': ['liblinear']
               }

grid = GridSearchCV(pipe, param_grid, cv = 5, scoring = 'accuracy', verbose = 1, n_jobs = -1)
grid.fit(X_train, y_train)

print("Best hyperparameters: ", grid.best_params_)
print("Best CV accuracy score: ", grid.best_score_)

# make prediction
pred = grid.predict(X_test)

# calculate accuracy
acc = metrics.accuracy_score(y_test, pred)

# Report the accuracy
print(acc)

with open(output_file_path, 'w') as file:
    file.write(f"Accuracy: {acc}\n")
    file.write("\nDescribe Statistics:\n")
    file.write(stats.to_string())

#Visualize the confusion matrix
cf_matrix = metrics.confusion_matrix(y_test, pred)
print(cf_matrix)

cm = sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True, 
            fmt='.2%', cmap='Blues')

output_file_path_pic = os.path.join(output_directory, "confusion_matrix_testset.png")
plt.savefig(output_file_path_pic)