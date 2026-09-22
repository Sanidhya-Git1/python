import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May']
sales = [12000,15000,18000,14000,16000]

plt.plot(months,sales)
#plt.show()

#plot line chart
#plt.plot(months,sales,marker='o', color = 'black',linewidth=1, linestyle='-.')

############## scatter chart
data = {
    'OrderId' : [1,2,3,4,5,6,7,8,9,10],
    'OrderQuantity' : [15,10,5,12,8,7,20,25,18,30],
    'TotalAmount' : [150,100,50,120,80,70,200,250,180,300]
}
orders_df = pd.DataFrame(data);
# plt.scatter(orders_df['OrderQuantity'], orders_df['TotalAmount'], marker = 'o')
# plt.title('Order Quantity Vs Total Amount')
# plt.xlabel('Order quantity')
# plt.ylabel('total amount ($)')
# plt.grid(True)
# plt.show()

######### Bubble chart
categories = ['grocery', 'health and beauty', 'office supplies','entertainment','clothing']
share = [0.1,0.2,0.4,0.2,0.1] # x axis data
avg_growth = [0.22,0.33,0.25,0.4,0.5] # y axis data
total_sales_sizes = [200,500,800,2000,500]  # bubble size
plt.scatter(share, avg_growth, color=['blue','green','yellow','cyan','magenta'] , s = total_sales_sizes )
# add category to each bubble
for i, category in enumerate(categories):
    plt.text(share[i], avg_growth[i], category , ha='center') # horizontal alignment

plt.title('E-commerce by category')
plt.xlabel('E-commerce share of total revenue')
plt.ylabel('Avg E-commerce growth')
plt.show()

## Please check for Histogram , Bar chart, Pie Chart,  HeatMap, Line Chart, 