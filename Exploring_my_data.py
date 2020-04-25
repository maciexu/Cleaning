"""
Loading and viewing your data

In this chapter, you're going to look at a subset of the Department of Buildings Job Application Filings dataset from the NYC Open Data portal. 
This dataset consists of job applications filed on January 22, 2017.

https://opendata.cityofnewyork.us

Your first task is to load this dataset into a DataFrame and then inspect it using the .head() and .tail() methods. 
However, you'll find out very quickly that the printed results don't allow you to see everything you need, 
since there are too many columns. Therefore, you need to look at the data in another way.

The .shape and .columns attributes let you see the shape of the DataFrame and obtain a list of its columns. 
From here, you can see which columns are relevant to the questions you'd like to ask of the data. 
To this end, a new DataFrame, df_subset, consisting only of these relevant columns, has been pre-loaded. 
This is the DataFrame you'll work with in the rest of the chapter.

Get acquainted with the dataset now by exploring it with pandas! 
This initial exploratory analysis is a crucial first step of data cleaning.
"""
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())


"""
he .info() method provides important information about a DataFrame, 
such as the number of rows, number of columns, number of non-missing values in each column, and the data type stored in each column. 
This is the kind of information that will allow you to confirm whether the 'Initial Cost' and 'Total Est. Fee' columns are numeric or strings. 
From the results, you'll also be able to see whether or not all columns have complete data in them.
"""
# Print the info of df
print(df.info())

# Print the info of df_subset
print(df_subset.info())


# summary statistics
# Exploratory Data Analysis
df.describe()







