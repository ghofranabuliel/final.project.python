📌 # Background 

This project analyzes an Alzheimer's Disease dataset to investigate patterns
related to age, gender, and diagnosis distribution. It also performs statistical 
tests to identify significant relationships in the data. The dataset was obtained 
from Kaggle and contains information on patients diagnosed with Alzheimer's.


📂 # Dataset Information



The dataset contains multiple attributes, but our analysis focuses on the following key variables:

Age: The age of the patient

Gender: Male or Female

Diagnosis: Whether the patient has Alzheimer's disease (1) or not (0)


Research Question

Does age or gender significantly impact the likelihood of being diagnosed with Alzheimer's disease?

 Results

No missing values were found in the dataset.

Age does not significantly impact diagnosis (T-test p-value 0.7782).

Gender does not significantly impact diagnosis (Chi-square p-value 0.2596).

The prevalence of Alzheimer's is fairly consistent across different age groups, with a slight peak around age 67.

Diagnosis rates remain stable across age groups (60-90).


🚀 Project Workflow

1️⃣ Load and Preprocess Data

loadData(filepath): Reads the dataset and filters relevant columns (PatientID, Age, Gender, Diagnosis).
solveOfmissingvalues(alzhData): Identifies and removes rows with missing values.

2️⃣ Exploratory Data Analysis (EDA)

Distributions:

age_distrib(alzhData): Plots the distribution of ages.
gender_distrib(alzhData): Displays gender distribution.
diagnosis_distrib(alzhData): Shows the proportion of Alzheimer's vs. No Alzheimer's cases.

Grouping and Visualization:
ageGroups(alzhData): Creates age groups (60-70, 70-80, 80-90)
groups_distribution(alzhData): Visualizes Alzheimer's diagnosis across different age groups.
gender_diagnosis(alzhData): Analyzes diagnosis distribution by gender.
plot_detailed_age_group_analysis(alzhData): Provides a detailed breakdown of gender and diagnosis within each age group.

3️⃣ Statistical Tests

tests(alzhData): Performs T-test for age comparison and Chi-Square test for gender-diagnosis association.
age_diagnosis(alzhData): Examines age distribution with respect to diagnosis

🛠 Virtual Environment Activation

To create and activate a virtual environment:

python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows

1.Ensure you have Python installed with the required libraries:
pip install pandas
seaborn 
matplotlib scipy
2.Place the dataset file (alzheimers_disease_data.csv) in the same directory as the script.
3.Run the script:python script_name.py


📊 Expected Outcomes

Identification of key demographic factors influencing Alzheimer's diagnosis.
Visualization of patterns in age, gender, and diagnosis distribution.
Statistical validation of whether differences in age and gender are significant predictors of Alzheimer's.
Insights for further research on how demographics correlate with Alzheimer's disease.


Project Structure

alzheimers_analysis
│── data
│   │── raw
│   │   │── alzheimers_disease_data.csv  # Original dataset
│   │── processed
│   │   │── filtered_alzheimers_data.csv  # Cleaned dataset
│   │   │── processed_alzheimers_data.csv  # Final dataset after preprocessing
│
│── src
│   │── __init__.py
│   │── preprocessing
│   │   │── __init__.py
│   │   │── load_data.py 
│   │   │── clean_data.py 
│   │
│   │── analysis
│   │   │── __init__.py
│   │   │── eda.py  
│   │   │── statistical_tests.py  
│   │
│   │── visualization
│   │   │── __init__.py
│   │   │── plots.py  # Functions for visualizing distributions
│
│── tests
│   │── __init__.py
│   │── test_data_processing.py  # Tests for data preprocessing
│   │── test_analysis.py  # Tests for statistical functions
│
│── main.py  # Main script to run the entire analysis
│── README.md  # Project documentation
│── requirements.txt  
│── pyproject.toml  
│── alzheimers_analysis.code-workspace  





📌 Uses


Research & Academic Analysis: Understanding demographic factors affecting Alzheimer's diagnosis.

Data Visualization: Generating visual insights for diagnosis distribution.

Statistical Testing: Performing T-tests and Chi-square tests to assess significance.

Predictive Modeling: Can be extended for machine learning-based predictions.

📚 References

Dataset Source: https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset/data
Statistical Methods: SciPy documentation on T-tests and Chi-Square tests



