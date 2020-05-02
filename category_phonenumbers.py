# Category: find inconsistent catagories 
# anti join VS inner join

inconsistent_cate = set(study_data['blood_type']).difference(catagories['blood_type'])
inconsistent_rows = study_data['blood_type'].isin(inconsistent_cate)
inconsistent_data = study_data[inconsistent_rows]

# drop inconsistent rows
consistent_data = study_data[~inconsistent_rows]

# Example Code# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")

# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])

""" what type of error could have for categorical data?
Value inconsistency: upper, lower, space, _
Too many categories or too few catagoreis: example->house income. Solution: need to remap to new ones
"""

# Caplitalized or loweecase
marriage['status'] = marriage['status'].str.upper()
marriage['status'] = marriage['status'].str.lower()
marriage['status'].value_counts()

# strip all spaces
marriage['status'] = marriage['status'].str.strip()
marriage['status'].value_counts()


# Collapse data into dategories
ranges = [0, 200000, 5000000, np.inf]
group = ['0-200K', '200K-500k', '500K+']
income['group'] = pd.cut(income['household_income'], bins = ranges, labels = group)
income[['group', 'household_income']]

# map to fewer
# previous categories: Micro, MacOS, IOS, Android, Linux
# to PCOS, MobileOS
mapping = {'Micro':'PCOS', 'MacOS':'PCOS', 'IOS':'MobileOS', 'Android':'MobileOS', 'Linux':'PCOS'}
devices['system'] = devices['system'].replace(mapping)
devices['system'].unique()

# Example Codes
# Print unique values of both columns->find the problems
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

# Verify changes have been effected
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

""" 
Example Code->Remap
to create two new categorical variables:

wait_type: 'short' for 0-60 min, 'medium' for 60-180 and long for 180+
day_week: 'weekday' if day is in the weekday, 'weekend' if day is in the weekend.
"""
# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, 
                                labels = label_names)

# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)


""" 
Text and RE
"""
# phone numbers: 
# inconsistent format-> 001-XXX, +1-XXX, 1 XXX, (647)XXX,...., 416.705.XXXX,  705  673.... 
# length vialation

# replace + with 00
phone['numbers'] = phone['numbers'].str.replace('+', '00')

# replace - with nothing
phone['numbers'] = phome['numbers'].str.replace('-', '')

# replace .
# strip white space...

# replace numbers lower than 10 digits to NaN
digits = phone['numbers].str.len()
phone.loc[digits<10, 'numbers'] = np.nan
               
# Check errors
assert phone['numbers'].str.contains('+|-').any() == False  
assert phone['numbers'].str.len().min() >= 10      

# replace anything that is not a digit with nothing
phone['numbers'] = phone['numbers'].str.replace(r'\D+', '')
               
               

# Example Codes
# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss","")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")

# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])

