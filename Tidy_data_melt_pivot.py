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

"""
Pivot data

Pivoting data is the opposite of melting it. 
Remember the tidy form that the airquality DataFrame was in before you melted it? 
You'll now begin pivoting it back into that form using the .pivot_table() method!

While melting takes a set of columns and turns it into a single column, 
pivoting will create a new column for each unique value in a specified column.

.pivot_table() has an index parameter which you can use to specify the columns that you don't want pivoted: 
It is similar to the id_vars parameter of pd.melt(). 
Two other parameters that you have to specify are columns (the name of the column you want to pivot), 
and values (the values to be used when the column is pivoted). 
The melted DataFrame airquality_melt has been pre-loaded for you.
"""
# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index='Date', columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())



"""
Resetting the index of a DataFrame

After pivoting airquality_melt in the previous exercise, you didn't quite get back the original DataFrame.
https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html

What you got back instead was a pandas DataFrame with a hierarchical index (also known as a MultiIndex).

Hierarchical indexes are covered in depth in Manipulating DataFrames with pandas. 
https://learn.datacamp.com/courses/manipulating-dataframes-with-pandas

In essence, they allow you to group columns or rows by another variable - in this case, by 'Date'.

There's a very simple method you can use to get back the original DataFrame from the pivoted DataFrame: 
.reset_index(). Dan didn't show you how to use this method in the video, 
but you're now going to practice using it in this exercise to get back the original DataFrame from airquality_pivot, 
which has been pre-loaded.
"""
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()

# Print the new index of airquality_pivot_reset
print(airquality_pivot_reset.index)

# Print the head of airquality_pivot_reset
print(airquality_pivot_reset.head())



"""
Pivoting duplicate values

So far, you've used the .pivot_table() method when there are multiple index values you want to hold constant during a pivot. 
In the video, Dan showed you how you can also use pivot tables to deal with duplicate values by providing an aggregation function through the aggfunc parameter. 
Here, you're going to combine both these uses of pivot tables.

Let's say your data collection method accidentally duplicated your dataset. 
Such a dataset, in which each row is duplicated, has been pre-loaded as airquality_dup. 
In addition, the airquality_melt DataFrame from the previous exercise has been pre-loaded. 

Explore their shapes in the IPython Shell by accessing their 
.shape attributes to confirm the duplicate rows present in airquality_dup.

You'll see that by using .pivot_table() and the aggfunc parameter, you can not only reshape your data, 
but also remove duplicates. Finally, you can then flatten the columns of the pivoted DataFrame using .reset_index().

NumPy and pandas have been imported as np and pd respectively.
"""
# Pivot table the airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index='Date', columns='measurement', values='reading', aggfunc=np.mean)

# Print the head of airquality_pivot before reset_index
print(airquality_pivot.head())

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())


"""
Splitting a column with .str

The dataset you saw in the video, consisting of case counts of tuberculosis by country, year, gender, and age group, 
has been pre-loaded into a DataFrame as tb.

In this exercise, you're going to tidy the 'm014' column, which represents males aged 0-14 years of age. 
In order to parse this value, you need to extract the first letter into a new column for gender, 
and the rest into a column for age_group. 
Here, since you can parse values by position, you can take advantage of pandas' vectorized string slicing 
by using the str attribute of columns of type object.

Begin by printing the columns of tb in the IPython Shell using its .columns attribute, 
and take note of the problematic column.
"""

# Melt tb: tb_melt
tb_melt = pd.melt(tb, id_vars=['country', 'year'])

# Create the 'gender' column
tb_melt['gender'] = tb_melt.variable.str[0]

# Create the 'age_group' column
tb_melt['age_group'] = tb_melt.variable.str[1:]

# Print the head of tb_melt
print(tb_melt.head())




"""
Splitting a column with .split() and .get()

Another common way multiple variables are stored in columns is with a delimiter. 
You'll learn how to deal with such cases in this exercise, using a dataset consisting of Ebola cases and death counts by state and country. 
It has been pre-loaded into a DataFrame as ebola.
https://data.humdata.org/dataset/ebola-cases-2014

Print the columns of ebola in the IPython Shell using ebola.columns. 
Notice that the data has column names such as Cases_Guinea and Deaths_Guinea. 
Here, the underscore _ serves as a delimiter between the first part (cases or deaths), and the second part (country).

This time, you cannot directly slice the variable by position as in the previous exercise. 
You now need to use Python's built-in string method called .split(). 
By default, this method will split a string into parts separated by a space. 
However, in this case you want it to split by an underscore. 
You can do this on 'Cases_Guinea', for example, using 'Cases_Guinea'.split('_'), which returns the list ['Cases', 'Guinea'].

The next challenge is to extract the first element of this list and assign it to a type variable, 
and the second element of the list to a country variable. 
You can accomplish this by accessing the str attribute of the column and using the 
.get() method to retrieve the 0 or 1 index, depending on the part you want.
"""
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date','Day' ], var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())


