# is477-fall2023-final-project
[![DOI](https://zenodo.org/badge/723204699.svg)](https://zenodo.org/doi/10.5281/zenodo.10253435)

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
   - This will also produce a confusion matrix heatmap on the testset data called **confusion_matrix_testset.png** in the results folder.

This workflow is documented in the **Snakefile** in this repo to document the input and outputs.
The picture below is the workflow visualization.
   
<img width="512" alt="Screenshot 2023-12-07 at 12 03 21" src="https://github.com/lwangjt/is477-fall2023-final-project/assets/112108984/e3dd4da3-6875-4d01-99ca-c992f5a7c70a">



## Reproducing 
1. Check your environment/create a virtual environment and add packages
You can reproduce the environment using the following information:
  - Create a virtual environment on your computer after you download the files from this repository (>Create Environment in VS Code).
  - To add dependencies: download the requirement.txt file from this github repo main branch, then run
    ```
    pip install -r requirements.txt
    ```
  - For more information about the environment that I used, please refer to the **environment.log** file on this repository.
```
ProductName:            macOS
ProductVersion:         14.1.1
BuildVersion:           23B81

Python 3.10.13

annotated-types==0.6.0
appdirs==1.4.4
attrs==23.1.0
certifi==2023.11.17
charset-normalizer==3.3.2
ConfigArgParse==1.7
connection-pool==0.0.3
contourpy==1.2.0
cycler==0.12.1
dacite==1.8.1
datrie==0.8.2
docutils==0.20.1
dpath==2.1.6
fastjsonschema==2.19.0
fonttools==4.46.0
gitdb==4.0.11
GitPython==3.1.40
htmlmin==0.1.12
humanfriendly==10.0
idna==3.6
ImageHash==4.3.1
Jinja2==3.1.2
joblib==1.3.2
jsonschema==4.20.0
jsonschema-specifications==2023.11.2
jupyter_core==5.5.0
kiwisolver==1.4.5
llvmlite==0.41.1
MarkupSafe==2.1.3
matplotlib==3.7.3
multimethod==1.10
nbformat==5.9.2
networkx==3.2.1
numba==0.58.1
numpy==1.25.2
packaging==23.2
pandas==2.0.3
patsy==0.5.4
phik==0.12.3
Pillow==10.1.0
plac==1.4.1
platformdirs==4.0.0
psutil==5.9.6
PuLP==2.7.0
pydantic==2.5.2
pydantic_core==2.14.5
pyparsing==3.1.1
python-dateutil==2.8.2
pytz==2023.3.post1
PyWavelets==1.5.0
PyYAML==6.0.1
referencing==0.31.1
requests==2.31.0
reretry==0.11.8
rpds-py==0.13.2
scikit-learn==1.3.2
scipy==1.11.4
seaborn==0.12.2
six==1.16.0
smart-open==6.4.0
smmap==5.0.1
snakemake==7.32.4
statsmodels==0.14.0
stopit==1.1.2
tabulate==0.9.0
tangled-up-in-unicode==0.2.0
threadpoolctl==3.2.0
throttler==1.2.2
toposort==1.10
tqdm==4.66.1
traitlets==5.14.0
typeguard==4.1.5
typing_extensions==4.8.0
tzdata==2023.3
urllib3==2.1.0
visions==0.7.5
wordcloud==1.9.2
wrapt==1.16.0
ydata-profiling==4.6.2
yte==1.5.1
```
   
  - You can check your environment version the following on your terminal:
  ```
  sw_vers #(For MacOS version)
  ver #(For Windows version)
  python –-version
  pip freeze
  ```

2. Set up your directory like:
```
    name_it_your_own/
                  data/
                  profiling/
                  results/
                  scripts/
                        prepare_data.py **download from this repo**
                        profile.py **download from this repo**
                        analysis.py **download from this repo**
                  requirements.txt **download from this repo**
```
4. Run the scripts
  - Choice 1: Run it step by step **without snakemake**
     1. Run the **prepare_data.py** file
   
     - As mentioned above, you will first run the **prepare_data.py** to get the original data **rice+cammeo+and+osmancik.zip** and the csv file (modified by me) **Rice_Cammeo_Osmancik.csv**.
     - This file will download the files into a **data** folder since these two files are not provided directly on this repository. The sentence "Zip/csv file has been downloaded successfully" as these files are downloaded correctly onto your computer.
     - Moreover, the integrity will be checked by comparing the **sha256** for both files. If the hash matches with the corresponding file, "The computed hash for ___ matches the expected hash" will show up on the terminal. Otherwise, "The computed hash for ____ does not match the expected hash" will show up if the file fails to confirm its integrity.

    2. Run the **profiling.py** file
   
    - As you already installed pandas and ydata-profiling, a **report.html** report will download into your **profiling** folder.

    3. Run the **analysis.py** file
    - In this file, a logistic regression task will be performed on the csv file. As a result, it will produce a **confusion_matrix_testset.png** to examine the prediction accuracy. And a **results.txt** will include the summary statistics of the features as well as the accuracy score of the classification task. These files will be stored in the **results** folder.
      
  - Choice 2: Run **with snakemake**
    ```
    snakemake --cores 1 prepare
    ```
    ```
    snakemake --cores 1 profile
    ```
    ```
    snakemake --cores 1 analyze
    ```
4. Compare all the outputs to the repo's files.
   - You could compare the outputs from the files above in the **results** and the **profiling** folder in this repo.
  
## License

* The MIT license is applied here for the scripts because it's a free, permissive software license that allows users to run and use my code for any purpose. This license aligns with the purpose of this project well since I did not directly provide the data in this repository. This could allow people to visit and reproduce my analysis of the rice data at any time. 

## References 

Cinar, I., & Koklu, M. (2019). Classification of Rice Varieties Using Artificial Intelligence Methods. International Journal of Intelligent Systems and Applications in Engineering.

Edotor — Your Favorite Online Graphviz Editor. (n.d.). https://edotor.net/

Pedregosa, F., Varoquaux, Ga"el, Gramfort, A., Michel, V., Thirion, B., Grisel, O., … others. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12(Oct), 2825–2830.
 
Rice (Cammeo and Osmancik). (2019). UCI Machine Learning Repository. https://doi.org/10.24432/C5MW4Z.
