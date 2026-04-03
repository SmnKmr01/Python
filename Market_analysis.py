import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data_estate.csv')
# print(df.info())

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
# print(df.info())
df = df.drop_duplicates()
df = df.dropna()


# NUmerical cleaning
df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)
df['area'] = df['area'].astype(str).str.replace(',', '').astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(
    str).str.replace(',', '').astype(int)
# print(df['area'])
# print(df['rate_per_sqft'])


# Categorical columns cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera approval'] = df['rera_approval'].str.strip().str.lower().map(
    {'Approved by rera': True, 'Not Approved by rera': False})
df['Flat_type'] = df['flat_type'].str.strip().str.lower()
# print(df['rera approval'])
df = df.drop_duplicates()
# print(df)
# print(df.info())


# Question 1 :Which is the costliest flat in the dataset?

costliest_flat = df.loc[df['price'].idxmax()]
print("Costliest Flat:")
'''
price                                1226300000.0
status                              ready to move
area                                        16500
rate_per_sqft                               74323
property_type    6 BHK Apartment in DLF Camellias
locality                                Sector 42
builder_name                    Provident Capital
rera_approval                Not approved by RERA
bhk_count                                       6
society                             DLF Camellias
company_name                                  DLF
flat_type                               Apartment
rera approval                                 NaN
Flat_type                               apartment'''
print(
    f"The costliest flat is: {costliest_flat['bhk_count']} BHK flat in {costliest_flat['locality']} with price {costliest_flat['price']/10000000:.2f} Cr in {costliest_flat['society']} by {costliest_flat['builder_name']}")

# Question 2: which locality has the highest average price per sqft?

highest_avg_price = df.groupby(
    'locality')['price'].mean().idxmax()
print(
    f"The locality with the highest average price is: {highest_avg_price}")

# Question3 : which locality  with the highest average price per sqft?
highest_avg_price_per_sqft = df.groupby(
    'locality')['rate_per_sqft'].mean().idxmax()
print(
    f"The locality with the highest average price per sqft is: {highest_avg_price_per_sqft}")


# Question 4 : do ready to move properties cost more than under construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status']
                                  == 'under construction']['price'].mean()
print(f"Average price of ready to move properties: {ready_to_move_avg_price}")
print(
    f"Average price of under construction properties: {under_construction_avg_price}")
if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready to move properties cost more than under construction properties.")
else:
    print("Under construction properties cost more than ready to move properties.")


# QUestion 5: DO rera approved properties cost more than non rera approved properties?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
non_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
print(f"Average price of RERA approved properties: {rera_approved_avg_price}")
print(
    f"Average price of non RERA approved properties: {non_rera_approved_avg_price}")
if rera_approved_avg_price > non_rera_approved_avg_price:
    print("RERA approved properties cost more than non RERA approved properties.")
else:
    print("Non RERA approved properties cost more than RERA approved properties.")

# How does area (sqft) impact property price?
sns.scatterplot(x='area', y='price', data=df)
plt.title('Area vs Price')
plt.xlabel('Area (sqft)')
plt.ylabel('Price')
# plt.show()


# Which BHK configuration is the most expensive on average?
avg_price_by_bhk = df.groupby('bhk_count')['price'].mean()
most_expensive_bhk = avg_price_by_bhk.idxmax()
print(
    f"The most expensive BHK configuration on average is: {most_expensive_bhk} BHK")


# Which property type (Apartment, Floor, Plot) is the costliest?
avg_price_by_property_type = df.groupby('property_type')['price'].mean()
costliest_property_type = avg_price_by_property_type.idxmax()
print(
    f"The costliest property type on average is: {costliest_property_type}")


# Do certain builders or companies consistently price higher?
avg_price_by_builder = df.groupby('builder_name')['price'].mean()
most_expensive_builder = avg_price_by_builder.idxmax()
print(
    f"The builder with the highest average price is: {most_expensive_builder}")

# Are larger homes always more expensive per square foot?
sns.scatterplot(x='area', y='rate_per_sqft', data=df)
plt.title('Area vs Rate per Sqft')
plt.xlabel('Area (sqft)')
plt.ylabel('Rate per Sqft')
plt.show()
