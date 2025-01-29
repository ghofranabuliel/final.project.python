import functions

def main():
    #we define the file path for the dataset
    filepath = 'alzheimers_disease_data.csv'

    #we load the dataset from the CSV file and filter it by calling the loaddata func
    alzhData = functions.loadData(filepath)

    #we handle missing vals by calling the solve of missing values func. 
    alzhData = functions.solveOfmissingvalues(alzhData)

    #the plot of the distribution of ages in the dataset
    functions.age_distrib(alzhData)

    #the plot the distribution of gender in the dataset
    functions.gender_distrib(alzhData)

    #the plot of the distribution of alzheimer diagnosis in the dataset
    functions.diagnosis_distrib(alzhData)

    #categorize patients into age groups (60-70, 70-80, 80-90)
    alzhData = functions.ageGroups(alzhData)

    #the stacked bar chart plot that show alzheimer diagnosis between different age groups
    functions.groups_distribution(alzhData)
    
    #the stacked bar chart plot that show alzheimer diagnosis between gender
    functions.gender_diagnosis(alzhData)

    #we generate detailed age-group-based analysis with bar charts and pie charts
    functions.plot_detailed_age_group_analysis(alzhData)

    #we call the t test func to implement the test
    functions.tests(alzhData)

    #the plot of the age distribution by alzheimers diagnosis using a histogram
    functions.age_diagnosis(alzhData)

################################### Call main :D ##################################
if __name__ == "__main__":
    main()

