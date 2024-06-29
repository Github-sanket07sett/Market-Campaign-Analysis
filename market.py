import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('/content/drive/MyDrive/Dataset/onyx data.csv',encoding='latin-1')
df.head(3)

df.info()

# Calculate the total conversion value
total_conversion_value = df['Total conversion value, GBP'].sum()

print("Total Conversion Value, GBP: ", total_conversion_value)

#average total sales
average_total_sales = df['Total conversion value, GBP'].mean()

print("Average Total Sales, GBP: ", average_total_sales)

#Calculate total sales per month
total_sales_monthly=df["Total conversion value, GBP"].groupby(df["Month"]).sum()
print(total_sales_monthly)
#bar chart
months = total_sales_monthly.index
sales = total_sales_monthly.values
plt.bar(months,sales)
plt.xlabel('Month')
plt.ylabel('Total conversion value, GBP')
plt.title('Total Sales per Month')
plt.show()

#Calculate total sales per city
total_sales_city=df["Total conversion value, GBP"].groupby(df["City"]).sum()
print(total_sales_city)

plt.pie(total_sales_city,labels=total_sales_city.index,autopct='%1.1f%%')
plt.title('total sales per city')
plt.show()

#calculate total Spend
total_spend = df['Spend, GBP'].sum()

print("Total Spend, GBP: ", total_spend)
#average spend
average_spend = df['Spend, GBP'].mean()

print("Average Spend, GBP: ", average_spend)

#total spend per city
total_spend_city = df["Spend, GBP"].groupby(df["City"]).sum()
print(total_spend_city)

plt.pie(total_spend_city,labels=total_spend_city.index,autopct='%1.1f%%')
plt.title('total spend per city')
plt.show()

#total spend per month
Total_spend_monthly=df["Spend, GBP"].groupby(df["Month"]).sum()
print(Total_spend_monthly)
months = Total_spend_monthly.index
spend = Total_spend_monthly.values
plt.bar(months,spend)
plt.xlabel('Month')
plt.ylabel('Spend, GBP')
plt.title('Total Spend per Month')
plt.show()

#calculate total clicks
Total_clicks=df['Clicks'].sum()
print("total Clicks:",Total_clicks)
#average clicks
average_clicks=df['Clicks'].mean()
print('average clicks:',average_clicks)
plt.bar(df['Month'],df['Clicks'])
plt.xlabel('Month')
plt.ylabel('Clicks')
plt.title('Total Clicks per Month')
plt.show()

#total Shares
total_shares=df['Shares'].sum()
print('Total Shares:',total_shares)
#average shares
average_shares=df['Shares'].mean()
print('average shares:',average_shares)
#total comments
total_comments=df['Comments'].sum()
print("total comments:",total_comments)
#average comments
average_comments=df['Comments'].mean()
print('average comments:',average_comments)
