"""
Exploratory analysis

Whenever you obtain a new dataset, 
your first task should always be to do some exploratory analysis to get a better understanding of the data and diagnose it for any potential issues.

The Gapminder data for the 19th century has been loaded into a DataFrame called g1800s. 
In the IPython Shell, use pandas methods such as .head(), .info(), and .describe(), 
and DataFrame attributes like .columns and .shape to explore it.
"""

"""
Visualizing your data

Since 1800, life expectancy around the globe has been steadily going up. 
You would expect the Gapminder data to confirm this.

The DataFrame g1800s has been pre-loaded. 
Your job in this exercise is to create a scatter plot with life expectancy in '1800' on the x-axis and life expectancy in '1899' on the y-axis.

Here, the goal is to visually check the data for insights as well as errors. 
When looking at the plot, pay attention to whether the scatter plot takes the form of a diagonal line, 
and which points fall below or above the diagonal line. 
This will inform how life expectancy in 1899 changed (or did not change) compared to 1800 for different countries. 
If points fall on a diagonal line, it means that life expectancy remained the same!
"""

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()


"""
As you can see, there are a surprising number of countries that fall on the diagonal line. 
In fact, examining the DataFrame reveals that the life expectancy for 140 of the 260 countries did not change at all in the 19th century! 
This is possibly a result of not having access to the data for all the years back then. 
In this way, visualizing your data can help you uncover insights as well as diagnose it for errors.
"""
def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Check whether the first column is 'Life expectancy'
assert g1800s.columns[0] == 'Life expectancy'

# Check whether the values in the row are valid
assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
assert g1800s['Life expectancy'].value_counts()[0] == 1


"""
Assembling your data

Here, three DataFrames have been pre-loaded: g1800s, g1900s, and g2000s. 
These contain the Gapminder life expectancy data for, respectively, the 19th century, the 20th century, and the 21st century.
"""
# Concatenate the DataFrames column-wise
gapminder = pd.concat([g1800s, g1900s, g2000s],axis=1)

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())


"""
Reshaping your data

Now that you have all the data combined into a single DataFrame, the next step is to reshape it into a tidy data format.

Currently, the gapminder DataFrame has a separate column for each year. 
What you want instead is a single column that contains the year, and a single column that represents the average life expectancy for each year and country. By having year in its own column, you can use it as a predictor variable in a later analysis.

You can convert the DataFrame into the desired tidy format by melting it.
"""
import pandas as pd

# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(frame=gapminder,id_vars='Life expectancy')

# Rename the columns
gapminder_melt.columns = ['country', 'year', 'life_expectancy']

# Print the head of gapminder_melt
print(gapminder_melt.head())


"""
Checking the data types

Now that your data are in the proper shape, you need to ensure that the columns are of the proper data type. 
That is, you need to ensure that country is of type object, year is of type int64, and life_expectancy is of type float64.

The tidy DataFrame has been pre-loaded as gapminder. Explore it in the IPython Shell using the .info() method. 
Notice that the column 'year' is of type object. 
This is incorrect, so you'll need to use the pd.to_numeric() function to convert it to a numeric data type.

NumPy and pandas have been pre-imported as np and pd.
"""
# Convert the year column to numeric
gapminder.year = pd.to_numeric(gapminder.year)

# Test if country is of type object
assert gapminder.country.dtypes == np.object

# Test if year is of type int64
assert gapminder.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder.life_expectancy.dtype == np.float64

# Output:
# Since the assert statements did not throw any errors, you can be sure that your columns have the correct data types.


"""
Looking at country spellings

Having tidied your DataFrame and checked the data types, your next task in the data cleaning process is to look at the 'country' column 
to see if there are any special or invalid characters you may need to deal with.

It is reasonable to assume that country names will contain:

The set of lower and upper case letters.
Whitespace between words.
Periods for any abbreviations.
To confirm that this is the case, you can leverage the power of regular expressions again. 
For common operations like this, Pandas has a built-in string method - str.contains() - 
which takes a regular expression pattern, and applies it to the Series, 
returning True if there is a match, and False otherwise.

Since here you want to find the values that do not match, you have to invert the boolean, 
which can be done using ~. This Boolean series can then be used to get the Series of countries that have invalid names.
"""
# Create the series of countries: countries
countries = gapminder['country']

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
# Anchor the pattern to match exactly what you want by placing a ^ in the beginning and $ in the end.
# Use A-Za-z to match the set of lower and upper case letters, \. to match periods, and \s to match whitespace between words.
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
# Use str.contains() to create a Boolean vector representing values that match the pattern.
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
# Invert the mask by placing a ~ before it.
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
# Subset the countries series using the .loc[] accessor and mask_inverse.
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)







