import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, chi2_contingency


###################################### Func1 ######################################

# we read the data file and we extract only the columns we want to use, 
# and we save the filterd data to a new csv file, in the end we return the new CSV that we created. 
def loadData(filepath):
    try:
        alzhData=pd.read_csv(filepath)
        filterData=alzhData[['PatientID', 'Age', 'Gender', 'Diagnosis']]
        filterData.to_csv('filtered_alzheimers_data.csv', index=False)
        return pd.read_csv('filtered_alzheimers_data.csv')
    except FileNotFoundError:
        print(f"Error: The file not found :(.")
        exit()
    except Exception as e:
        print(f"Error! I cant load your file :( {e}")
        exit()


###################################### Func2 ######################################
# here in this func we check the missing vals in the dataset, we count them and we remove
# all the rows with any missing data,
# and if there is no missing data we print a messege. 
def solveOfmissingvalues(alzhData):
    try:
        missingVals= alzhData.isnull().sum()
        if missingVals.sum()>0:
            print("\nThere are missing values :( Processing missing values...")
            alzhData = alzhData.dropna()
            alzhData.to_csv('processed_alzheimers_data.csv', index=False)
            print("\nRows with missing values have been removed :).")
        else:
            print("\nNo missing values detected ^_^. The data is ready!.")
        return alzhData
    except Exception as e:
        print(f"Sorry! There is an error :( {e}")
        exit()


###################################### Func3 ######################################
# here we creat and display histogram to show the age destribution in the dataset, 
# we use age coulmn
def age_distrib(alzhData):
    try:
        plt.figure(figsize=(10, 5))
        sns.histplot(alzhData['Age'], bins=20, color='darkviolet')
        plt.title('Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Sorry! I cant plot your plot :( {e}")



###################################### Func4 ######################################
# this func creats and displays a bar chart to show the ditributhin of the gender in the dataset.
def gender_distrib(alzhData):
    try:
        plt.figure(figsize=(6, 4))
        sns.countplot(x='Gender', data=alzhData, hue='Gender', dodge=False, palette='pastel', legend=False)
        plt.title('|Gender Distribution|')
        plt.xticks([0, 1], ['Male', 'Female'])
        plt.ylabel('Count')
        plt.show()
    except Exception as e:
        print(f"Sorry! I cant plot your plot :( {e}")



###################################### Func5 ######################################
# this func creats and display a pie chart to show to us the distribution of 
# alzhimer diagnosis in the dataset.
def diagnosis_distrib(alzhData):
    try:
        diagnosis_counts=alzhData['Diagnosis'].value_counts()
        plt.figure(figsize=(6, 6))
        diagnosis_counts.plot(kind='pie', autopct='%1.1f%%', labels=['No Alzheimer\'s', 'Alzheimer\'s'], colors=['skyblue', 'salmon'])
        plt.title('||Diagnosis Distribution||')
        plt.ylabel('')
        plt.show()
    except Exception as e:
        print(f"Sorry! I cant plot your plot :( {e}")



###################################### Func6 ######################################
#this func make to us a categorizes for the patients into ages groups and remove thos outside the defined age range. 
def ageGroups(alzhData):
    try:
        alzhData['AgeGroup']= pd.cut(alzhData['Age'], bins=[60, 70, 80, 90], labels=['60-70', '70-80', '80-90'])
        alzhData=alzhData.dropna(subset=['AgeGroup'])
        return alzhData
    except Exception as e:
        print(f" Sorry! I Couldnt add the gropus :( {e}")
        exit()



###################################### Func7 ######################################
# here in this func we create a stacked bar chart to visulize the distrbution of alzhimer diagnosis
# into the diffrent groups we definded above, 
# we use groupby to count how many patients are diagnosed with alzheimer im each group. 
def groups_distribution(alzhData):
    try:
        groups=alzhData.groupby(['AgeGroup', 'Diagnosis'], observed=True).size().unstack()
        fffig, axs=plt.subplots(figsize=(10, 7))
        groups.plot(kind='bar', stacked=True, color=['gray', 'brown'], ax=axs)
        axs.set_title("Alzheimer's Diagnosis by Age Group", fontsize=16, fontweight='bold')
        axs.set_xlabel('Age Group', fontsize=14)
        axs.set_ylabel('Count', fontsize=14)
        axs.legend(['No Alzheimer\'s', 'Alzheimer\'s'], fontsize=12, title_fontsize=14)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Sorry! I cant plot your plot :( {e}")



###################################### Func8 ######################################
# this func creates a stacked bar chart to visualize the distribution of Alzheimer's diagnosis by gender.
# it use groupby like the func above.
def gender_diagnosis(alzhData):
    gender_diagnosis=alzhData.groupby(['Gender', 'Diagnosis']).size().unstack()
    gender_diagnosis.plot(kind='bar', stacked=True, figsize=(8, 6), color=['skyblue', 'pink'])
    plt.title("|||Alzheimer's Diagnosis by Gender|||")
    plt.xlabel('|Gender|')
    plt.ylabel('|Count|')
    plt.xticks([0, 1], ['Male', 'Female'])
    plt.legend(['No Alzheimer\'s', 'Alzheimer\'s'], title='Diagnosis')
    plt.show()



###################################### Func9 ######################################
# this function analayz and visulaize alzhimer patients distribution within each age group using two plots per age
# group: Bar chart: Shows gender-based distribution of Alzheimer's diagnosis,
# Pie chart: Shows percentage distribution of diagnosis for each age group. 
def plot_detailed_age_group_analysis(alzhData):
    alzhData['Diagnosis']=alzhData['Diagnosis'].astype(str)
    ages = alzhData['AgeGroup'].unique()
    for num in ages:
        
        subset = alzhData[alzhData['AgeGroup']==num]
        plt.figure(figsize=(6, 4))
        sns.countplot(x='Gender', hue='Diagnosis', data=subset, palette={'0': 'gold', '1': 'purple'})
        plt.title(f"Age Group: {num}", fontsize=14)
        plt.xlabel('*Gender*')
        plt.ylabel('*Count*')
        plt.xticks([0, 1], ['Male', 'Female'], fontsize=10)
        plt.legend(title='Diagnosis', labels=['No Alzheimer\'s', 'Alzheimer\'s'])
        plt.tight_layout()
        plt.show()
        counts=subset['Diagnosis'].value_counts()
        plt.figure(figsize=(6, 6))
        counts.plot(kind='pie', autopct='%1.1f%%', colors=['green', 'yellow'], labels=['No Alzheimer\'s', 'Alzheimer\'s'])
        plt.title(f"**Diagnosis Distribution in Age: {num}**")
        plt.show()



###################################### Func10 #####################################
#in this func we do two statistical tests to analyze the relationship between alzheimer and age gender. 
# and we check if there is a significant diffrencer in age and gender and alzheimer.
def tests(alzhData):
    try:
        alzheimer_no = alzhData[alzhData['Diagnosis'] == '0']
        alzheimer_yes = alzhData[alzhData['Diagnosis'] == '1']
        t, p = ttest_ind(alzheimer_yes['Age'], alzheimer_no['Age'])
        print(f"\nAge T-Test:\nT-statistic = {t:.4f}")
        print(f"P-value = {p:.4f}")
        gender_contingency = pd.crosstab(alzhData['Gender'], alzhData['Diagnosis'])
        chi2, p2, _, _ = chi2_contingency(gender_contingency)
        print(f"\nGender Chi-Square Test:\nChi2 = {chi2:.4f}")
        print(f"P-value = {p2:.4f}")
    except Exception as e:
        print(f"Sorry! I cant implemnt your tests :( {e}")



###################################### Func11 ######################################
# This function visualizes the distribution of age among alzheimers and non alzheimer's patients using a histogram
def age_diagnosis(alzhData):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=alzhData, x= 'Age', hue='Diagnosis', kde=True, palette={'0': 'yellow', '1': 'green'}, bins=20)
    plt.title('Age Distribution by Diagnosis')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.legend(['No Alzheimer\'s', 'Alzheimer\'s'])
    plt.show()



################################### Finally: main ##################################
def main():
    #we define the file path for the dataset
    filepath = 'alzheimers_disease_data.csv'

    #we load the dataset from the CSV file and filter it by calling the loaddata func
    alzhData = loadData(filepath)

    #we handle missing vals by calling the solve of missing values func. 
    alzhData = solveOfmissingvalues(alzhData)

    #the plot of the distribution of ages in the dataset
    age_distrib(alzhData)

    #the plot the distribution of gender in the dataset
    gender_distrib(alzhData)

    #the plot of the distribution of alzheimer diagnosis in the dataset
    diagnosis_distrib(alzhData)

    #categorize patients into age groups (60-70, 70-80, 80-90, 90+)
    alzhData = ageGroups(alzhData)

    
    groups_distribution(alzhData)
    gender_diagnosis(alzhData)
    plot_detailed_age_group_analysis(alzhData)

    tests(alzhData)
    age_diagnosis(alzhData)



################################### Call main :D ##################################
if __name__ == "__main__":
    main()