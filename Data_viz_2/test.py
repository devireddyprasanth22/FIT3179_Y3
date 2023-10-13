# import pandas as pd

# # Assuming your wide format data is stored in a DataFrame named 'wide_data'
# # Replace 'wide_data' with the actual name of your DataFrame
# df = pd.read_csv("data/long_data.csv")
# # Melt the wide data into long format

# # Pivot the DataFrame to reshape it
# pivot_df = df.pivot_table(index=['Country', 'Year'], columns='Category', values='Value', aggfunc='sum').reset_index()

# # Rename columns
# pivot_df.columns.name = None
# pivot_df = pivot_df.rename(columns={'Personal ': 'Personal', 'Business and Professional ': 'Business and Professional'})
# # Display the long format data
# output_file_path = "data/new_data.csv"
# pivot_df.to_csv(output_file_path, index=False)

import pandas as pd

# Read your original data
data = pd.read_csv('data/gdpT.csv')

# Melt the data to create a long format
long_format_data = data.melt(id_vars='Country', var_name='Year', value_name='Total')

# Sort the data by "Country" and "Year" if needed
long_format_data = long_format_data.sort_values(by=['Country', 'Year'])

# Save the resulting data to a new CSV file
long_format_data.to_csv('long_format_data.csv', index=False)