"""
This is when we want to combine two dataframe, but they have dup records 
Getting pairs to compare
"""

# Step 1. import recordlinkage, generate pairs, compare across columns by exact & string similarity
import recordlinkage

indexer = recordlinakge.Index()

indexer.block('state')
pairs = indexer.index(census_a, census_b)

# Create a compare object
compare_c1 = recordlinkage.Compare()

# Find exact match
compare_c1.exact('date_of_birth', 'date_of_birth', label = 'date _of_birth')
compare_c1.exact('state', 'state', label = 'state')

# Find similar match
compare_c1.string('surname', 'surname', threshold = 0.85, label = 'surname')
compare_c1.string('address', 'address', threshold = 0.85, label = 'address')

# Step 2. Generate potential matches
potetial_match = compare_c1.compute(pairs, census_a, census_b)

# Step 3.  Isolate matches with matching values for n or more colomns, n is depends on the exact and string similarity comparison.
# Find the only paris we want
matches = potential_match[potential_match.sum(axis = 1) >=2]

# Step 4. Get index for matching census B rows only. 
# Note: get_level_values(0) or get_level_values('census_A') for the first dataframe. 1 for the second dataframe. 
dup_rows = matches.index.get_level_values(1)

# Step 5. Find new (non-duplicated) rows in B
census_B_new = census_B[~census_B.index.isin(dup_rows)]

# Step 6. Link the dataframe
full_census = census_A.append(census_B_new)



""" Example codes"""
# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types - 
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')

# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.8) 

# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

"""
Question:
Print out potential_matches, the columns are the columns being compared, with values being 1 for a match, 
and 0 for not a match for each pair of rows in your DataFrames. To find potential matches, 
you need to find rows with more than matching value in a column. You can find them with

potential_matches[potential_matches.sum(axis = 1) >= n]

Where n is the minimum number of columns you want matching to ensure a proper duplicate find, 
what do you think should the value of n be?

Answer:
3 because I need to have matches in all my columns.
If n is set to 2, then you will get duplicates for all restaurants with the same cuisine type in the same city.
"""

""" Link Dataframe"""
# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis=1) >= 3]

# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)


