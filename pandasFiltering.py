# filtering with loc and iloc
import numpy as np
import pandas as pd

data = {
    'Name' : ['Lily','Emma','John'],
    'Age' : [38,35,28],
    'Education' : ['high school','phd','bachelor'],
    'Gender' : [0,0,1]
}
customer = pd.DataFrame(data)
print(customer)
print("----------------------------")  

#    Name  Age    Education  Gender
# 0  Lily   38  high school       0
# 1  Emma   35          phd       0
# 2  John   28     bachelor       1

# Filtering
# loc - labels
# iloc - index
# Filtering using loc means based on labels
print(customer.loc[0:2, 'Name' : 'Education']) # slicing index are inclusing as it is label means for row 0 to 2, and for columns Name to Education
print("----------------------------")  
print(customer)
print("----------------------------")  

# Filtering using iloc means based on index
print(customer.iloc[0:2, 0:2]) # slicing index are exclusive 
print("----------------------------")  
print(customer.iloc[0:2, 0:10]) 
print("----------------------------")  
print(customer.iloc[0:2, [0,1,3]]) 
print("----------------------------")  
#print(customer.iloc[0:2, 5])  #IndexError("single positional indexer is out-of-bounds")
#print("----------------------------")  
print(customer.iloc[0:2, 2])  
print("----------------------------")  

# column  access
print(customer.Education) 
print("----------------------------")  

print(customer[['Education']]) 
print("----------------------------")  

print(customer[['Age','Education']]) 
print("----------------------------")  


# Filtering on conditions
# Filter customers whose name is 'Lily'
condition = (customer['Name'] == 'Lily')
customer_filtered1 = customer[condition]
print(customer_filtered1)
print("----------------------------")  

# multiple conditions : Age >= 35 and is female (0: female, 1:male)
conditions =(customer['Age'] >=35 ) & (customer['Gender'] == 0)
customer_filtered = customer[conditions]
print(customer_filtered)
print("----------------------------")  

name_list = ['Lily', 'Sanidhya', 'John']
condition = customer['Name'].isin(name_list)
customer_filtered = customer[condition]
print(customer_filtered)
print("----------------------------")

# filter the customer name starting with 'E'
condition = customer['Name'].str.contains(r'^[E]', regex= True)
customer_filtered = customer[condition]
print(customer_filtered)
print("----------------------------")

# Handling missing values
df = pd.DataFrame(
    {
        'account_length' : [20,20,np.nan, 20,30],
        'gender' : [np.nan, 'M', 'M', 'F', 'F'],
        'education' : ['high school','high school', 'high school', 'high school', np.nan]
    }
)

print(df)
print("----------------------------")

# replace the missing value with average value of column 'account_length'
valueToReplace = df['account_length'].mean()
#valueToReplace = df['account_length'].max()
print(valueToReplace)

# fill the missing value with the valueToReplace
df['account_length'].fillna(valueToReplace)
print(df)
print("----------------------------")

df['account_length'].fillna(valueToReplace, inplace= True)
print(df)
print("----------------------------")

# replace the missing value with most frequent value in column education'
# valueToReplace2 = df['education'].mode()[0]
# df['education'].fillna(valueToReplace2, inplace= True)
# print(df)

# df['gender'].fillna('M', inplace=True)
# print(df)
print("----------------------------")

df.fillna({'account_length' : 25.0, 'gender' : 'M', 'education' : 'high school'}, inplace= True)
print(df)
print("----------------------------")


# Sorting in a data frame
data = {
    'Date' : ['2023-09-01','2023-09-02','2023-09-03','2023-09-04'], 
    'Product' : ['Product A','Product B','Product C','Product D'], 
    'Quantity Sold' : [100,150,120,80], 
    'Revenue' : [5000,7500,6000,4000]
}

# df.sort_values('Revenue', ascending= False)
# print(df)
# print("----------------------------")
# print(df.sort_values(by='Revenue', ascending= False).reset_index())
# print("----------------------------")
# print(df.sort_values(by='Revenue', ascending= False).reset_index(drop=True))
# print("----------------------------")
# print(df.sort_values(by=['Score','Age'],  ascending= [False,True].reset_index(drop=True))

# Data analysis : groupby, agg

df = pd.DataFrame({
    'product_category' : ['baby','book','book','beauty','baby'],
    'product_price' : [19.99, 12.49 , 22 , 49 , 16],
    'rating' : [5,3,3,2,4]
})

print(df);
print("----------------------------")
# what is the average rating by product category
avg_rating_summary = df.groupby('product_category')['rating'].mean().reset_index()
print(avg_rating_summary);
print("----------------------------")
avg_rating_summary.rename(columns={'rating' : 'avg_rating'}, inplace=True)
print(avg_rating_summary);
print("----------------------------")

df = pd.DataFrame({
    'order_id' : ['4235','2342','1234','5325','1342'],
    'product_category' : ['baby','beauty','baby','beauty','beauty'], 
    'product' : ['diaper','eye liner','diaper','eye shadow','face mask'],
    'product_price': [19.99,12.49,22,49,16],
    'quantity' : [5,3,3,2,4]}
)

product_summary = df.groupby('product_category').agg({'product_price':'mean'}).reset_index()
print(product_summary)
print("----------------------------")


# what is the average product price and total quantity of each product category
product_summary = df.groupby('product_category').agg({'product_price':'mean', 'quantity' : 'sum'}).reset_index()
print(product_summary)
print("----------------------------")

product_summary.rename(columns={'product_price':'avg_product_price', 'quantity':'total_quantity'},inplace=True)
print(product_summary)
print("----------------------------")

# Concatenate dataframes
csv_url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv';
titanic = pd.read_csv(csv_url)
print(titanic.head(n=3))
print("----------------------------")
titanic_a = titanic.head(n=5)
print(titanic_a)
print("----------------------------")

titanic_b = titanic.tail(n=3)
print(titanic_b)
print("----------------------------")

concat_df = pd.concat([titanic_a , titanic_b], axis=0).reset_index(drop=True)
print(concat_df)
print("----------------------------")

titanic_c = titanic[['Name','Age']].head(5)
print(titanic_c)
print("----------------------------")
titanic_d = titanic[['Ticket','Fare']].tail(3)
print(titanic_d)
print("----------------------------")

pd_concate = pd.concat([titanic_c, titanic_d], axis = 0).reset_index(drop = True)
print(pd_concate)
print("----------------------------")

pd_concate = pd.concat([titanic_c, titanic_d], axis = 1).reset_index(drop = True)
print(pd_concate)
print("----------------------------")

# Merging

product_data = {
    'product_id' : ['P2','P3','P4'],
    'product_name' : ['Product B','Product C','Product D']
}
product_df = pd.DataFrame(product_data)

review_data = {
    'product_id' : ['P1','P2','P3', np.nan],
    'review_score' : [4.5,3.8,4.0,4.1],
    'review_comment':['Great product','Needs improvement','Satisfied','Not bad']
}

review_df = pd.DataFrame(review_data)

# Merge based on 'product_id' column
merged_df = product_df.merge(review_df, on='product_id', how = 'inner')
print(merged_df)
print("----------------------------")

merged_df = pd.merge(product_df,review_df, on='product_id', how = 'inner')
print(merged_df)
print("----------------------------")

merged_df = merged_df = product_df.merge(review_df, on='product_id', how = 'left')
print(merged_df)
print("----------------------------")

merged_df = merged_df = product_df.merge(review_df, on='product_id', how = 'right')
print(merged_df)
print("----------------------------")

merged_df = merged_df = product_df.merge(review_df, on='product_id', how = 'outer')
print(merged_df)
print("----------------------------")
