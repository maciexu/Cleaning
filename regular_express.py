"""
String parsing with regular expressions

In the video, Dan introduced you to the basics of regular expressions, 
which are powerful ways of defining patterns to match strings. 
This exercise will get you started with writing them.

When working with data, it is sometimes necessary to write a regular expression to look for properly entered values. 
Phone numbers in a dataset is a common field that needs to be checked for validity. 
Your job in this exercise is to define a regular expression to match US phone numbers that fit the pattern of xxx-xxx-xxxx.

The regular expression module in python is re. 
https://docs.python.org/3/library/re.html
When performing pattern matching on data, since the pattern will be used for a match across multiple rows, 
it's better to compile the pattern first using re.compile(), and then use the compiled pattern to match values.
"""
# Import the regular expression module
import re

# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result2 = prog.match('1123-456-7890')
print(bool(result2))

"""
Extracting numerical values from strings

Extracting numbers from strings is a common task, particularly when working with unstructured data or log files.

Say you have the following string: 'the recipe calls for 6 strawberries and 2 bananas'.

It would be useful to extract the 6 and the 2 from this string to be saved for later use when comparing strawberry to banana ratios.

When using a regular expression to extract multiple numbers (or multiple pattern matches, to be exact), 
you can use the re.findall() function. 
You pass in a pattern and a string to re.findall(), and it will return a list of the matches.
"""
# Import the regular expression module
import re

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)

# Pattern matching
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# \$ to match the dollar sign, 
# \d* to match an arbitrary number of digits, 
# \. to match the decimal point, 
# \d{x} to match x number of digits.
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# A capital letter, followed by an arbitrary number of alphanumeric characters.
# Use [A-Z] to match any capital letter followed by \w* to match an arbitrary number of alphanumeric characters.
pattern3 = bool(re.match(pattern='\w*', string='Australia'))
print(pattern3)

"""
Custom functions to clean data

You'll now practice writing functions to clean data.

The tips dataset has been pre-loaded into a DataFrame called tips. 
It has a 'sex' column that contains the values 'Male' or 'Female'. 
Your job is to write a function that will recode 'Female' to 0, 'Male' to 1, 
and return np.nan for all entries of 'sex' that are neither 'Female' nor 'Male'.

Recoding variables like this is a common data cleaning task. 
Functions provide a mechanism for you to abstract away complex bits of code as well as reuse code. 
This makes your code more readable and less error prone.

You can use the .apply() method to apply a function across entire rows or columns of DataFrames. 
However, note that each column of a DataFrame is a pandas Series. 
Functions can also be applied across Series. Here, you will apply your function over the 'sex' column.
"""

# Define recode_gender()
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0
    
    # Return 1 if gender is 'Male'    
    elif gender == 'Male':
        return 1
    
    # Return np.nan    
    else:
        return np.nan

# Apply the function to the sex column
tips['recode'] = tips.sex.apply(recode_gender)

# Print the first five rows of tips
print(tips.head())


"""
Lambda functions

You'll now be introduced to a powerful Python feature that will help you clean your data more effectively: lambda functions. 
Instead of using the def syntax that you used in the previous exercise, lambda functions let you make simple, one-line functions.

For example, here's a function that squares a variable used in an .apply() method:

def my_square(x):
    return x ** 2

df.apply(my_square)
The equivalent code using a lambda function is:

df.apply(lambda x: x ** 2)
The lambda function takes one parameter - the variable x. 
The function itself just squares x and returns the result, which is whatever the one line of code evaluates to. 
In this way, lambda functions can make your code concise and Pythonic.

The tips dataset has been pre-loaded into a DataFrame called tips. 
Your job is to clean its 'total_dollar' column by removing the dollar sign. 
You'll do this using two different methods: With the .replace() method, and with regular expressions. 
"""
# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())

# Notice how the 'total_dollar_re' and 'total_dollar_replace' columns are identical.
