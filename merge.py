"""
1-to-1 data merge

Merging data allows you to combine disparate datasets into a single dataset to do more complex analysis.

Here, you'll be using survey data that contains readings that William Dyer, Frank Pabodie, 
and Valentina Roerich took in the late 1920s and 1930s while they were on an expedition towards Antarctica. 
The dataset was taken from a sqlite database from the Software Carpentry SQL lesson.

http://swcarpentry.github.io/sql-novice-survey/

Two DataFrames have been pre-loaded: site and visited. 
Explore them in the IPython Shell and take note of their structure and column names. 
Your task is to perform a 1-to-1 merge of these two DataFrames using the 'name' column of site and the 'site' column of visited.
"""

# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(o2o)


"""
Many-to-1 data merge

In a many-to-one (or one-to-many) merge, one of the values will be duplicated and recycled in the output. 
That is, one of the keys in the merge is not unique.

Here, the two DataFrames site and visited have been pre-loaded once again. 
Note that this time, visited has multiple entries for the site column. Confirm this by exploring it in the IPython Shell.

The .merge() method call is the same as the 1-to-1 merge from the previous exercise, but the data and output will be different.
"""

"""
Many-to-many data merge

The final merging scenario occurs when both DataFrames do not have unique keys for a merge. 
What happens here is that for each duplicated key, every pairwise combination will be created.
"""
# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.head(20))

