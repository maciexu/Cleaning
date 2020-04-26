"""
Converting data types

In this exercise, you'll see how ensuring all categorical variables in a DataFrame are of type category reduces memory usage.

The tips dataset has been loaded into a DataFrame called tips. 
https://github.com/mwaskom/seaborn-data/blob/master/tips.csv
This data contains information about how much a customer tipped, whether the customer was male or female, a smoker or not, etc.

Look at the output of tips.info() in the IPython Shell. 
You'll note that two columns that should be categorical - sex and smoker - are instead of type object, which is pandas' way of storing arbitrary strings. 
Your job is to convert these two columns to type category and note the reduced memory usage.
"""
# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# Print the info of tips
print(tips.info())

"""
Working with numeric data

If you expect the data type of a column to be numeric (int or float), but instead it is of type object, 
this typically means that there is a non numeric value in the column, which also signifies bad data.

You can use the pd.to_numeric() function to convert a column into a numeric data type. 
If the function raises an error, you can be sure that there is a bad value within the column. 
You can either use the techniques you learned in Chapter 1 to do some exploratory data analysis and find the bad value, 
or you can choose to ignore or coerce the value into a missing value, NaN.

A modified version of the tips dataset has been pre-loaded into a DataFrame called tips. 
For instructional purposes, it has been pre-processed to introduce some 'bad' data for you to clean. 
Use the .info() method to explore this. You'll note that the total_bill and tip columns, 
which should be numeric, are instead of type object. Your job is to fix this.
"""

# Convert 'total_bill' to a numeric dtype
# The 'total_bill' and 'tip' columns in this DataFrame are stored as object types because the string 'missing' is used in these columns to encode missing values. 
# By coercing the values into a numeric type, they become proper NaN values.

tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips['tip'], errors='coerce')

# Print the info of tips
print(tips.info())

