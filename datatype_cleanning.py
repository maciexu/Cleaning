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
movies[movies['rating'] > 5]

# drop and replace
movies.drop(movies[movies['rating'] > 5].index, inplace = True)

# drop by filtering
movies = movies[movies['ratings'] <= 5]

# verify the result
assert movies['ratings'].max() <=5







 

