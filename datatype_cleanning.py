"""
Category VS Int
The user_type column contains information on whether a user is taking a free ride and takes on the following values:

1 for free riders.
2 for pay per ride.
3 for monthly subscribers.
"""
# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics 
print(ride_sharing['user_type_cat'].describe())



""" str VS int"""
# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())


"""Data range"""
# Q: Can future registrations exist???
# Q: Can the rating above the max value???
# Example: the max value of the movie rating is 5, but there are some of 6. First to out put the movies with ratings > 6
movies[movies['ratings'] > 5]

# Solutions:
#1 drop and replace
movies.drop(movies[movies['ratings'] > 5].index, inplace = True)

#2 drop by filtering
movies = movies[movies['ratings'] <= 5]

#3 convert these values to max value
movies.loc[movies['ratings']>5, 'ratings'] = 5

# verify the result
assert movies['ratings'].max() <=5

""" Convert to datetime"""
user['login'] = pd.to_datetime(user['login'])
assert users['login'].dtype == 'datetime64[ns]'

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Assert that maximum value of tire_sizes is 27
assert ride_sharing['tire_sizes'].max() == 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())

"""
Back to the future
A bug was discovered which was relaying rides taken today as taken next year.
"""
# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today,'ride_dt'] = today

# Assert change has been done
assert ride_sharing['ride_dt'].max().date() == today





