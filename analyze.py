import pandas as pd

# Read in a data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# calculate summary statistics on the Purchase Amount column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?
# result = df['Purchase Amount (USD)'].agg(['mean', 'median', 'max', 'min', 'std'])
def print_purchase_amount_statistics(df):
    result = df['Purchase Amount (USD)'].agg(['mean', 'median', 'max', 'min', 'std'])

    print("Summary statistics on Purchase Amount (USD)")
    print("Mean:", result['mean'])
    print("Median:", result['median'])
    print("Max:", result['max'])
    print("Min:", result['min'])
    print("Standard Deviation:", result['std'])
    print()


# calculate summary statistics on the Age column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?
def print_summary_statistics(df, column):
    result = df[column].agg(['mean', 'median', 'max', 'min', 'std'])

    print(f"Summary statistics on {column}")
    print("Mean:", result['mean'])
    print("Median:", result['median'])
    print("Max:", result['max'])
    print("Min:", result['min'])
    print("Standard Deviation:", result['std'])
    print()

# Call the function with your DataFrame and column name
print_summary_statistics(df, 'Age')

# summary statistics
# TODO: is there another function we can use to calculate metrics on groups?
def print_group_summary_statistics(df, column, group_column):
    grouped_df = df.groupby(group_column)

    for group_name, group_data in grouped_df:
        result = group_data[column].agg(['mean', 'median', 'max', 'min', 'std'])
        
        print(f"{group_name} summary statistics on {column}")
        print("Mean:", result['mean'])
        print("Median:", result['median'])
        print("Max:", result['max'])
        print("Min:", result['min'])
        print("Standard Deviation:", result['std'])
        print()

# Call the function with your DataFrame and relevant columns
print_group_summary_statistics(df, 'Purchase Amount (USD)', 'Season')

columns_to_exclude = ["Customer ID", "Discount Applied"]
df = df.drop(columns=columns_to_exclude)

# figure out most popular payment method in NY
# TODO: is there anyway we could modularize this behavior to apply to all
# TODO: possible states? (OR possibly use a pandas function that does this
# TODO: for us already?)
def find_most_frequent_payment_method(df, location):
    location_df = df[df.Location == location]
    most_frequent_method = location_df['Payment Method'].mode().iloc[0]
    return most_frequent_method

# Call the function with your DataFrame and desired location
ny_most_frequent_method = find_most_frequent_payment_method(df, "New York")
print(f"Most frequent payment method in New York: {ny_most_frequent_method}")


# Write this updated data out to csv file
df.to_csv('data/processed/cleaned_data.csv', index=False)
