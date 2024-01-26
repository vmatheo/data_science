import pandas as pd

# Define csv file path
path = "C:\\Users\\vmath\\OneDrive\\Desktop\\PycharmProjects\\sample_data_shop.txt"

# Read csv path into a pandas dataframe
df = pd.read_csv(path)

""" Options for displaying dataframe information """
print(df)  # Displays dataframe
print(type(df))  # Gives type of dataframe
print(df.info())  # Gives input and computer data
print(df.describe())  # Gives statistical data
print(df.columns)  # Gives column labels
print(df.shape)  # Gives shape of dataframe

""" Retrieving Dataframe Data """
# A dataframe is like a dictionary of lists, as opposed to a list of dictionaries
print(df['total_customer_count'])  # Actually retrieves  a series object!
print(df['total_customer_count'][2])  # Index a specific value
print(df.at[2, 'total_customer_count'])  # Equivalent expression as above
print(df.total_customer_count)  # Access series without indexing!
sub_df = df[['total_customer_count', 'hours_open']]  # Create another dataframe from previous one
df_copy = df.copy()  # Create a copy dataframe
print(df.loc[2])  # Access a specific row (may also be a range of rows)
df.head(3)  # Access top of list
df.tail(3)  # Access bottom of list
print(df.first_valid_index())  # Finds first instance of a non NaN value
print(df.sample(3))  # Get a random sample of values

""" Analyzing Dataframe """
print(df.total_customer_count.sum())  # Find total number of values
avg_customer_per_hour = df.total_customer_count.sum() / df.hours_open.tail(1).sum()
print(f"{round(avg_customer_per_hour)} customers/hour")  # Perform mathematical calculations ^
print(df[df.total_customer_count > 20])  # Show only entries greater than some value
print(df[df.total_customer_count > avg_customer_per_hour])  # Find days when above average customers
df['was_raining'] = [True, False, False, False, True, True]  # Add a new column to the dataframe
df.drop(columns=['was_raining'], inplace=True)  # Remove a column
print(df.sort_values('total_customer_count', ascending=False).head(2))  # Get largest values
df.at[2, 'total_customer_count'] = 20  # Change a value in the dataframe

# When dealing with dates in your data, it must be converted to a dataframe DataTime
# This allows for easy processing and modification

print(df[df.hours_open == 2])  # Get a row from a specific column entry, as opposed to index via loc
print(df.total_customer_count.mean())  # Find mean of a column

""" Grouping and Aggregation """
regrouped_df = df.groupby('hours_open')[['total_customer_count']].sum()
print(regrouped_df)  # Changes the index as desired by regrouping

df['cumulative_customers'] = df.total_customer_count.cumsum()
print(df)  # Cumulatively add up the data over as it progresses

""" Merging Data """
second_path = "C:\\Users\\vmath\\OneDrive\\Desktop\\PycharmProjects\\sample_data_weather.txt"
weather_df = pd.read_csv(second_path)
print(weather_df)
df['was_raining'] = ['True', 'False', 'False', 'True', 'False', 'True']
print(df)
merged_df = df.merge(weather_df, on='was_raining')  # Combine dataframes together
# Combining requires the two datasets have a common column!

""" Save an edited dataframe back to CSV format """
# df.to_csv('path', index=False)

