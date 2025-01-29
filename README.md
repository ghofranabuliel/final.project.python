📌 Background 

This project analyzes an Alzheimer's Disease dataset to investigate patterns
related to age, gender, and diagnosis distribution. It also performs statistical 
tests to identify significant relationships in the data. The dataset was obtained 
from Kaggle and contains information on patients diagnosed with Alzheimer's.


📂 Dataset Information



The dataset contains multiple attributes, but our analysis focuses on the following key variables:

Age: The age of the patient

Gender: Male or Female

Diagnosis: Whether the patient has Alzheimer's disease (1) or not (0)

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

🛠 How to Run the Project

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


📚 References

Dataset Source: https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset/data
Statistical Methods: SciPy documentation on T-tests and Chi-Square tests

