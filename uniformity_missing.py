# uniformity-> temperature C&F
# birthdate 27/26/1990???

birthdate['Date'] = pd.to_datetime(birthdate['Date'])   # error occurs since some data over over 12 months

# return NaN when failed, attempt to infer the format of each date
birthdate['Date'] = pd.to_datetime(birthdate['Date'], infer_dateime_format = True, errors = 'coerce') 

# change format
birthdate['Date'] = birthdate['Date'].dt.strftime('%d-%m-%Y')

# Ambiguous 2019-05-08???


"""Example Codes: banking"""
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1 

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'

# Print the header of account_opend
print(banking['account_opened'].head())

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])





""" 
Cross Field Validation
like:
sum col = total of type cols
age = now - birthdate
"""

# totla number of passengers
sum_classes = flights[['economy', 'business', 'first']].sum(axis = 1)
equ = sum_classes == flights['total_passengers']
inconsistent = flight[~equ]
consistent = flight[equ]

# age
user['Birthday'] = pd.to_datetime(user['Birthday'])
today = dt.date.today()
age_manual = today.year - user['Birthday'].dt.year
equ = age_manual == user['Age']
inconsistent = user[~equ]
consistent = user[equ]

"""Example Codes"""
# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual
age_equ = ages_manual == banking['age']

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])


""" Completeness"""
airquality.isna()  
airquality.isna().sum()

import missingno as msno
import matplotlib.ptplot as plt
# Visualize missingness
msno.metrix(airquality)
plt.show()

# isolate missing and complete values aside
missing = airqulity[airquality['CO2'].isna()]
complete = airqulity[~airquality['CO2'].isna()]

sorted_airquality = airquality.sort_values(by = 'Temp')
msno.metrix(sorted_airquality)
plt.show()

# plot output: lower temp ends up with NaN CO2 values.->could be sensor failure

# Missing type:
# Missing completely at random
# Missing at random: systematic relationship between missing data and other observed values. 
# Missing Not at random: systematic relationship between missing data and other observed values.

# To deal with missing data
# 1. Drop (direcly, filter)
# 2. impute with statistical measures (mean, median)
# 3. impute using algorithmic approach
# 4. impute using mechine learning models

# drop
airquality_drop = airquality.dropna(subset = ['CO2'])

# replace with mean
co2_mean = airquality['CO2'].mean()
# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount':acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())airquality_impute = airquality.fillna({'CO2': co2_mean})

""" Example Codes"""
# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# compare and noticed that: 
# The inv_amount is missing only for young customers, since the average age in missing_investors is 22 and the maximum age is 25.
print(investors.describe())
print(missing_investors.describe())

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by='age')
msno.matrix(banking_sorted)
plt.show()

# Notice how all the white spaces for inv_amount are on top? 
# Indeed missing values are only due to young bank account holders not investing their money!


# Drop missing customer_id rows and fill in the missing values for account amounts
# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount':acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())



