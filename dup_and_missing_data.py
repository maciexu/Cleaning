# Drop duplicate
# Create the new DataFrame: tracks
tracks = billboard[['year', 'artist', 'track', 'time']]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Fill in missing values
# Print info of tracks
print(tracks_no_duplicates.info())

# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)

# Print the info of airquality
print(airquality.info())

"""
Testing your data with asserts

Here, you'll practice writing assert statements using the Ebola dataset from previous chapters 
to programmatically check for missing values and to confirm that all values are positive. 
The dataset has been pre-loaded into a DataFrame called ebola.

use the .all() method together with the .notnull() DataFrame method to check for missing values in a column. 
The .all() method returns True if all values are True. 
When used on a DataFrame, it returns a Series of Booleans - one for each column in the DataFrame. 
So if you are using it on a DataFrame, you need to chain another .all() method so that you return only one True or False value. When using these within an assert statement, nothing will be returned if the assert statement is true: This is how you can confirm that the data you are checking are valid.

Note: You can use pd.notnull(df) as an alternative to df.notnull()
"""

# Assert that there are no missing values
# Use the pd.notnull() function on ebola (or the .notnull() method of ebola) and chain two .all() methods (that is, .all().all()). 
The first .all() method will return a True or False for each column, while the second .all() method will return a single True or False.

assert ebola.notnull().all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()






