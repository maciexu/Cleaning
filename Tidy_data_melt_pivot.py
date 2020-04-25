"""
Recognizing tidy data

For data to be tidy, it must have:

Each column contains exactly one variable.
Each row contains exactly one observation.
However, what constitutes a unique observation depends on your use case. 
As a data scientist, you'll encounter data that is represented in a variety of different ways, 
so it is important to be able understand and describe the structure of your data.

In this exercise, two example datasets have been pre-loaded into the DataFrames df1 and df2. 
They contain the same data, but structured in different ways. 
Your job is to explore these further in the IPython Shell and answer the question below.

A note before proceeding. 
In the rest of this course, you will frequently be asked to explore the structure of DataFrames in the IPython Shell prior to performing different operations on them. 
Doing this will not only strengthen your comprehension of the data cleaning concepts covered in this course, 
but will also help you realize and take advantage of the relationship between working in the Shell and in the script.

Both formats are tidy for different reasons, 
one is focused on individual sensor measurements, 
and the other is focused on daily measurements. 
"""
print(df1.head())
print(df2.head())


"""
Reshaping your data using melt

Melting data is the process of turning columns of your data into rows of data. 
Consider the DataFrames from the previous exercise. 
In the tidy DataFrame, the variables Ozone, Solar.R, Wind, and Temp each had their own column. 
If, however, you wanted these variables to be in rows instead, you could melt the DataFrame. 
In doing so, however, you would make the data untidy! 
This is important to keep in mind: 
Depending on how your data is represented, you will have to reshape it differently 
(e.g., this could make it easier to plot values).

In this exercise, you will practice melting a DataFrame using pd.melt(). 
There are two parameters you should be aware of: id_vars and value_vars. 
The id_vars represent the columns of the data you do not want to melt (i.e., keep it in its current shape), 
while the value_vars represent the columns you do wish to melt into rows. 
By default, if no value_vars are provided, all columns not set in the id_vars will be melted. 
This could save a bit of typing, depending on the number of columns that need to be melted.

The (tidy) DataFrame airquality has been pre-loaded. 
Your job is to melt its Ozone, Solar.R, Wind, and Temp columns into rows. 
Later in this chapter, you'll learn how to bring this melted DataFrame back into a tidy form.
"""
# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt AND rename
airquality_melt = pd.melt(airquality, id_vars='Date', var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())






















