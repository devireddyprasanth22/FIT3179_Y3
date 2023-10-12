import pandas as pd

df = pd.read_csv('data/tourist_exp.csv')
# Define the columns to be used for the transformation
# Define the new column order
new_column_order = ['Country', 'Year', 'Accomodation', 'F&B', 'Passenger transport', 'Travel agencies', 'Others']

# Create a new DataFrame to store the transformed data
transformed_df = pd.DataFrame(columns=new_column_order)

# Iterate over the rows of the original DataFrame and transform the data
for index, row in df.iterrows():
    country = row['Country']
    for column in df.columns:
        if column != 'Country':
            year = column.split(' ')[-1]  # Extract the year from the column name
            category = ' '.join(column.split(' ')[:-1])  # Extract the category name
            value = pd.to_numeric(row[column], errors='coerce')  # Convert to numeric and handle errors
            if not pd.isna(value):
                # Check if a row with the same country and year exists in the transformed DataFrame
                existing_row = transformed_df[(transformed_df['Country'] == country) & (transformed_df['Year'] == year)]
                if not existing_row.empty:
                    # Update the existing row with the category value
                    transformed_df.loc[existing_row.index, category] = value
                else:
                    # Create a new row for the country and year
                    new_row = [country, year] + [0] * (len(new_column_order) - 2)  # Initialize with zeros
                    new_row[new_column_order.index(category)] = value  # Set the category value
                    transformed_df.loc[len(transformed_df)] = new_row
output_file_path = "data/data1.csv"
transformed_df.to_csv(output_file_path, index=False)