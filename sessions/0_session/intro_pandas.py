
# Importing pandas
import pandas as pd

# Reading an excel file
data = pd.read_excel('Delivery truck trip data small.xlsx')

# Getting first 5 rows of data
data.head()

# Getting all column names
data.columns

# Get datatypes of column
data.dtypes

# Selecting a specific column
data['GpsProvider']

# Selecting two or more columns
data[['GpsProvider', 'customerID']]

# Getting all unique values in a column
data['customerID'].unique()

# Getting sum of a column
data['TRANSPORTATION_DISTANCE_IN_KM'].sum()

# Getting mean of a column
data['TRANSPORTATION_DISTANCE_IN_KM'].mean()

# Getting min of a column
data['TRANSPORTATION_DISTANCE_IN_KM'].min()

# Getting max of a column
data['TRANSPORTATION_DISTANCE_IN_KM'].max()

# Getting average transport distance by driver
data.groupby('Driver_Name')['TRANSPORTATION_DISTANCE_IN_KM'].mean()

# -------------- Subsetting data ------------------------------------
# Getting all rows with more than 2000 kilometers distance
data[data['TRANSPORTATION_DISTANCE_IN_KM'] > 2000]


# -------------- Manipulating data ------------------------------------

# Droping columns
data.drop('GpsProvider', axis=1, inplace=True)