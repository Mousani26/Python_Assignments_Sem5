'''
Create a dataframe with employeeID, empName, contact_no (one emp may have more than one contact no.), project_location (one employee may have more than one project loc).
Give the values of 5 employees in the dataframe in wide format, where the contact no. depends on project location.
Create/Reshape the table in long format using melt() method.
'''

import pandas as pd

# 1) Create a DataFrame for 5 employees in wide format
# Columns represent different project locations holding the contact numbers for those locations
data = {
    'employeeID':,
    'empName': ['Aarav', 'Diya', 'Rohan', 'Sneha', 'Vikram'],
    'Mumbai_Contact': ['9876543210', '9876543211', None, '9876543213', '9876543214'],
    'Delhi_Contact': ['9123456780', None, '9123456782', '9123456783', None],
    'Bengaluru_Contact': [None, '9988776651', '9988776652', None, '9988776654']
}

df_wide = pd.DataFrame(data)
print("Wide Format DataFrame:\n", df_wide)

# 2) Reshape the table into long format using melt()
df_long = pd.melt(
    df_wide,
    id_vars=['employeeID', 'empName'],          # Columns to keep fixed
    value_vars=['Mumbai_Contact', 'Delhi_Contact', 'Bengaluru_Contact'], # Columns to unpivot
    var_name='Project_Location',                # Name for the new location column
    value_name='Contact_No'                     # Name for the new contact number column
)

# Clean up location names and remove rows where the employee has no contact/project
df_long['Project_Location'] = df_long['Project_Location'].str.replace('_Contact', '')
df_long = df_long.dropna(subset=['Contact_No']).reset_index(drop=True)

print("\nLong Format DataFrame:\n", df_long)
