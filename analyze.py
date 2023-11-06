import pandas as pd

# Read in a data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# calculate summary statistics on the Purchase Amount column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?
s1 = df['Purchase Amount (USD)'].mean()
s2 = df['Purchase Amount (USD)'].median()
s3 = df['Purchase Amount (USD)'].max()
s4 = df['Purchase Amount (USD)'].min()
s5 = df['Purchase Amount (USD)'].std()

print("Summary statistics on Purchase Amount (USD)")
print("Mean", s1)
print("Median", s2)
print("Max", s3)
print("Min", s4)
print("Standard Dev", s5)
print()

# calculate summary statistics on the Age column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?
s1 = df['Age'].mean()
s2 = df['Age'].median()
s3 = df['Age'].max()
s4 = df['Age'].min()
s5 = df['Age'].std()

print("Summary statistics on Age")
print("Mean", s1)
print("Median", s2)
print("Max", s3)
print("Min", s4)
print("Standard Dev", s5)
print()

# summary statistics
# TODO: is there another function we can use to calculate metrics on groups?
winter = df[df.Season == "Winter"]
summer = df[df.Season == "Summer"]
spring = df[df.Season == "Spring"]
fall = df[df.Season == "Fall"]

s1 = winter['Purchase Amount (USD)'].mean()
s2 = winter['Purchase Amount (USD)'].median()
s3 = winter['Purchase Amount (USD)'].max()
s4 = winter['Purchase Amount (USD)'].min()
s5 = winter['Purchase Amount (USD)'].std()

print("Winter summary statistics on Purchase Amount (USD)")
print("Mean", s1)
print("Median", s2)
print("Max", s3)
print("Min", s4)
print("Standard Dev", s5)
print()

s1 = summer['Purchase Amount (USD)'].mean()
s2 = summer['Purchase Amount (USD)'].median()
s3 = summer['Purchase Amount (USD)'].max()
s4 = summer['Purchase Amount (USD)'].min()
s5 = summer['Purchase Amount (USD)'].std()

print("Summer summary statistics on Purchase Amount (USD)")
print("Mean", s1)
print("Median", s2)
print("Max", s3)
print("Min", s4)
print("Standard Dev", s5)
print()

s1 = spring['Purchase Amount (USD)'].mean()
s2 = spring['Purchase Amount (USD)'].median()
s3 = spring['Purchase Amount (USD)'].max()
s4 = spring['Purchase Amount (USD)'].min()
s5 = spring['Purchase Amount (USD)'].std()

print("Spring summary statistics on Purchase Amount (USD)")
print("Mean", s1)
print("Median", s2)
print("Max", s3)
print("Min", s4)
print("Standard Dev", s5)
print()

s1 = fall['Purchase Amount (USD)'].mean()
s2 = fall['Purchase Amount (USD)'].median()
s3 = fall['Purchase Amount (USD)'].max()
s4 = fall['Purchase Amount (USD)'].min()
s5 = fall['Purchase Amount (USD)'].std()

print("Fall summary statistics on Purchase Amount (USD)")
print("Mean", s1)
print("Median", s2)
print("Max", s3)
print("Min", s4)
print("Standard Dev", s5)
print()

# keep all columns except for "Customer", & "Discount Applied"
# TODO: is there a more efficient way to exclude columns in your dataset?
df = df[[
    "Customer ID",
    "Age",
    "Gender",
    "Item Purchased",
    "Category",
    "Purchase Amount (USD)",
    "Location",
    "Size",
    "Color",
    "Season",
    "Review Rating",
    "Subscription Status",
    "Shipping Type",
    "Promo Code Used",
    "Previous Purchases",
    "Payment Method",
    "Frequency of Purchases"
]]

# figure out most popular payment method in NY
# TODO: is there anyway we could modularize this behavior to apply to all
# TODO: possible states? (OR possibly use a pandas function that does this
# TODO: for us already?)
payment_methods = df['Payment Method'].unique()
ny = df[df.Location == "New York"]

most_frequent_method = {}

for method in payment_methods:
    most_frequent_method[method] = len(ny[ny['Payment Method'] == method])

print(most_frequent_method)

# Write this updated data out to csv file
df.to_csv('data/processed/cleaned_data.csv', index=False)
