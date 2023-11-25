# is477-fall2023-final-project

## Overview

This project mainly analyzed the rice dataset from the UCI archive with the entire workflow stored in this repository. 
* The rice data set had two classes (Cammeo and Osmancik). Moreover, the dataset has seven numerical features: Area Integer, Perimeter Real, Major_Axis_Length Real, Minor_Axis_Length Real,	EccentricityReal, Convex_AreaInteger, and	Extent Real.
* Using the provided Python file on logistic regression, you can predict whether a new data with the features mentioned above is either Cammeo or Osmancik.
* You can obtain the accuracy score of the classification model above as well as a confusion matrix graph for the testing data to examine the level of effectiveness of the provided model.

## Contributions: 

**This is an individual project, done by Lisa.**

## Analysis

* Using logistic regression with gridsearch on the rice dataset, I could get an overall accuracy of 0.937 which is performing well in terms of determining whether a new rice data is Cammeo or Osmancik based on the numerical features. After several tries of running the model, I found out that the penalty term played an important role in increasing the accuracy.
* The confusion_matrix_testset.png provides a visualization of the classification on testset. From the graph, there are two dark blue boxes represent the correctly classified rice while having a few incorrectly classified data from the light-blue boxes.
  
## Workflow 
section must contain the workflow image from step 9.

## Reproducing 
1. Check your environment
You can reproduce the environment using the following information:
  - To add dependencies: download the requirement.txt file from this github repo main branch, then run
    ```
    pip install -r requirements.txt
    ```
  - For more information about the environment that I used, please refer to the environment.log file on this repository.
    - ProductName:macOS
    - ProductVersion:13.1
    - BuildVersion:22C65
    - Python 3.10.10
    - certifi==2023.7.22
    - charset-normalizer==3.2.0
    - idna==3.4
    - requests==2.31.0
    - urllib3==2.0.4
   
  - You can check your environment version the following on your terminal:
  ```
  sw_vers #(For MacOS version)
  ver #(For Windows version)
  python –-version
  pip freeze
  ```
3. 
4. Run files

## License
I applied the MIT license here because it's a free, permissive software license that allows users to run and use my code for any purpose. This license aligns with the purpose of this project well since I did not directly provide the data in this repository. This could allow people to visit and reproduce my analysis of the rice data at any time.

## References 
section with accurate citation(s) for any data, software, or papers used. All citations must be in APA format. Note: you can use the DataCite citation feature from Lab 7.
