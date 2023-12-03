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

1. Firstly, you will get the data required: the original UCI Rice data (a zip file), as well as the adapted version of csv file that I made some changed of (changed the column name and format them just to make it look nicer).
   - Run, **prepare_data.py** to get both the **rice+cammeo+and+osmancik.zip** and the modified **Rice_Cammeo_Osmancik.csv** files.
   - This script will also verify the shasum hashes to ensure data integrity.

2. Secondly, run the **profile.py** script.
   - This script will read the dataset into a DataFrame and write the profiling report to **profiling/report.html**.
  
3. Finally, you could reproduce the analysis that is mentioned above by running the **analysis.py**
   - This will produce an accuracy score in terms of classifying the rice species called **results.txt** in the results folder.
   - This will also produce a confusion matrix heatmap on the testset data called condusion_matrix_testset.png in the results folder.
  
   
  <img width="568" alt="Screenshot 2023-12-03 at 00 31 02" src="https://github.com/lwangjt/is477-fall2023-final-project/assets/112108984/771d6fa8-6b9b-4e79-badd-377b137e8a1f">

  ____ worlflow pic needed here_____

## Reproducing 
1. Check your environment/create a virtual environment

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
2. Copy the repository to get the data and analysis mentioned above.
3. Run the workflow that is mentioned above
4. Check your results folder to see if the files match the results that are mentioned in the analysis section.

## License

* The MIT license is applied here for the scripts because it's a free, permissive software license that allows users to run and use my code for any purpose. This license aligns with the purpose of this project well since I did not directly provide the data in this repository. This could allow people to visit and reproduce my analysis of the rice data at any time. 
* I also applied the Creative Commons Attribution 4.0 International (CC BY 4.0) license for the modified data that I made for the CSV file since the original UCI rice data also applied this license so that make could share and make changes to the data as long as credit is given.

## References 

Cinar, I., & Koklu, M. (2019). Classification of Rice Varieties Using Artificial Intelligence Methods. International Journal of Intelligent Systems and Applications in Engineering.

Edotor — Your Favorite Online Graphviz Editor. (n.d.). https://edotor.net/

Pedregosa, F., Varoquaux, Ga"el, Gramfort, A., Michel, V., Thirion, B., Grisel, O., … others. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12(Oct), 2825–2830.
 
Rice (Cammeo and Osmancik). (2019). UCI Machine Learning Repository. https://doi.org/10.24432/C5MW4Z.
