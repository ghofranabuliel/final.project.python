📌 Background 

This project analyzes an Alzheimer's Disease dataset to investigate patterns
related to age, gender, and diagnosis distribution. It also performs statistical 
tests to identify significant relationships in the data. The dataset was obtained 
from Kaggle and contains information on patients diagnosed with Alzheimer's.


📂 Dataset Information

The dataset consists of key attributes:
PatientID: Unique identifier for each patient
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
