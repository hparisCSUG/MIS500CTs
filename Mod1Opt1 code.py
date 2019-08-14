#BEGIN CODE for Data Set Exploration

""" Program Begin HERE
Data exploration exercise in Python. The needed package/module pandas has been sourced and installed.
"""
#############################################################
#Program name - Data Exploration Exercise
#input - manually defined data frame below
#output - Some Exploration statistics, successful exit code 0
###############################################################


import pandas as pd     #imports pandas, a package/module used in data analysis

# Create a data_frame of array values specified in the below block

df = pd.DataFrame({     #define df (data frame) variable
    'name':['matt', 'lisa', 'richard', 'john', 'Julia', 'jane', 'marlon'],    #name data in string literals
    'age':[23, 42, 22, 36, 27, 33, 22],   #age data associated in order of name entry in integers
    'gender':['M','F','M','M','F','F','M'],     #gender data associated in order of name entry in string literals
    'state':['DC','CO','DE','VA','MD','DE','NY'],   #state of residence data associated in order of name entry in string literals
    'yrs_svc':[2, 12, 0, 8, 4, 7, 1],    #no. of years of service data associated in order of name entry in integers
    'iq':[128, 114, 110, 122, 112, 118, 108]    #iq data associated in order of name entry in integers
})  #end of data frame array

########################################################
#BEGIN extract a 25% sample of data
########################################################

rows = df.sample(frac =.25)     #define variable rows as a sample of 25% of the provided data in the data frame

if 0.25*(len(df)) == len(rows):     #verify 25% of the data is sampled
    print(len(df), len(rows))

# Display the 25% sample of the data frame

print("Sample of 25%",'\n', rows, '\n')      #print string literal in quotations and the categories of the data frame as a "header" with following line break for readablility

""" 
Extracted 25% sample will display below categories "header" preceded by their entry sequence number, 
0=first entered in list, 1=second entered in list, with all other data following under their associated category
"""

#END extract a 25% sample of data

############################################################
# BEGIN Split categorical variables by gender, Sum, Mean, count, and describe on the data
############################################################
#Categorical Variables splitting

print ("Average IQ by Gender from all data") #print title of displayed information

groupby_gender = df.groupby ('gender')  #group defined genders from original defined data frame
for gender, value in groupby_gender ['iq']: #pull mean/average iq data associated with each group
    print((gender, value.mean()))   #print identified group(s) and the mean/average of the associated iq

# Find the Summation of all ages in the data and print the result
SumofAge=df['age'].sum()
print ('\n', 'Sum of all Ages:', SumofAge)

#Find the Mean/Average of all ages in the data and print the result
MeanAge = df['age'].mean()
print ('\n','Average of all Ages:', MeanAge)

# Find the Mean/Average of all numerical data columns and print the results
print ('\n','Average of each numerical data column','\n', df.mean(axis=0))

# Describe the Data
print ('\n', "IQ data Description:",'\n', df['iq'].describe())  #displays all standard statistical information for all the iq data in the data frame

#END code - successful run will end displaying exit code 0
