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

#Total Sales per day
Total_sales_per_day=df["Total conversion value, GBP"].groupby(df["Day of the Week"]).sum()
print(Total_sales_per_day)
plt.pie(Total_sales_per_day,labels=Total_sales_per_day.index,autopct='%1.1f%%')
plt.title('Total Sales per Day')
plt.show()

#Total sales By Campaign type
Total_sales_Campaign=df['Total conversion value, GBP'].groupby(df["Campaign"]).sum()
print(Total_sales_Campaign)
plt.bar(Total_sales_Campaign.index,Total_sales_Campaign.values)
plt.title('Total Sales per Campaign')
plt.show()

#Total sales per channel
Total_sales_channel=df["Total conversion value, GBP"].groupby(df["Channel"]).sum()
print(Total_sales_channel)
plt.pie(Total_sales_channel,labels=Total_sales_channel.index,autopct='%1.1f%%')
plt.title('Total Sales per Channel')
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

#Total Spend Per Channel
total_spend_channel=df['Spend, GBP'].groupby(df["Channel"]).sum()
print(total_spend_channel)
plt.pie(total_spend_channel,labels=total_spend_channel.index,autopct='%1.1f%%')
plt.title('Total Spend per Channel')
plt.show()

#Total Sales per channel
Total_sales_channel=df['Total conversion value, GBP'].groupby(df["Channel"]).sum()
print(Total_sales_channel)
plt.pie(Total_sales_channel,labels=Total_sales_channel.index,autopct='%1.1f%%')
plt.title('Total Sales per Channel')
plt.show()

#Total Sales from Device Type
total_sales_per_device=df['Total conversion value, GBP'].groupby(df["Device"]).sum()
print(total_sales_per_device)
plt.pie(total_sales_per_device,labels=total_sales_per_device.index,autopct='%1.1f%%')
plt.title('Total Sales per Device')
plt.show()

#Total sales per ad
total_sales_per_ads = df['Total conversion value, GBP'].groupby(df["Ad"]).sum()
print(total_sales_per_ads)
plt.pie(total_sales_per_ads,labels=total_sales_per_ads.index,autopct='%1.1f%%')
plt.title('Total Sales from Ad types')
plt.show()


#Calculate Roas
ROAS=df['Total conversion value, GBP'].sum()/df['Spend, GBP'].sum()
print("Return of Ad Spend:",ROAS)
#ROAS Per Month
ROAS_per_month=df['Total conversion value, GBP'].groupby(df["Month"]).sum()/df['Spend, GBP'].groupby(df["Month"]).sum()
print(ROAS_per_month)
months = ROAS_per_month.index
roas = ROAS_per_month.values
plt.bar(months,roas)
plt.xlabel('Month')
plt.ylabel('ROAS')
plt.title('ROAS per Month')
plt.show()

#Roas per City
ROAS_per_city=df['Total conversion value, GBP'].groupby(df["City"]).sum()/df['Spend, GBP'].groupby(df["City"]).sum()
print(ROAS_per_city)
plt.pie(ROAS_per_city,labels=ROAS_per_city.index,autopct='%1.1f%%')
plt.title('ROAS per City')
plt.show()

#relation between Clicks vs conversions
plt.scatter(df['Clicks'],df['Conversions'])
plt.xlabel('Clicks')
plt.ylabel(' conversion value, GBP')
plt.title('Clicks vs conversion ')
plt.show()


conversion_rate=(df['Conversions'].sum()/df['Clicks'].sum())*100
print("conversion rate:",conversion_rate)

conversion_city=df['Conversions'].groupby(df["City"]).sum()/df['Clicks'].groupby(df["City"]).sum()*100
print("Conversion from  city",conversion_city)

conversion_device=df['Conversions'].groupby(df["Device"]).sum()/df['Clicks'].groupby(df["Device"]).sum()*100
print("conversion from device",conversion_device)


conversion_month=df['Conversions'].groupby(df["Month"]).sum()/df['Clicks'].groupby(df["Month"]).sum()*100
print("conversion from month",conversion_month)

profit_city=df['Total conversion value, GBP'].groupby(df["City"]).sum()-df['Spend, GBP'].groupby(df["City"]).sum()
print("profit from city:",profit_city)
plt.bar(profit_city.index,profit_city.values)
plt.xlabel('City')
plt.ylabel('Profit')
plt.title('Profit from City')
plt.show()

profit_channel=df['Total conversion value, GBP'].groupby(df["Channel"]).sum()-df['Spend, GBP'].groupby(df["Channel"]).sum()
print("profit from channel:",profit_channel)
plt.bar(profit_channel.index,profit_channel.values)
plt.xlabel('Channel')
plt.ylabel('Profit')
plt.title('Profit from Channel')
plt.show()

profit_month=df['Total conversion value, GBP'].groupby(df["Month"]).sum()-df['Spend, GBP'].groupby(df["Month"]).sum()
print("profit from campaign:",profit_month)
plt.bar(profit_month.index,profit_month.values)
plt.xlabel('Month')
plt.ylabel('Profit')
plt.title('Profit from Month')
plt.show()

#CPC by Channel
cpc_channel=df['Daily Average CPC'].groupby(df["Channel"]).sum()

print("cpc from channel:",cpc_channel)
plt.barh(cpc_channel.index,cpc_channel.values)
plt.xlabel('CPC')
plt.ylabel('Channel')
plt.title('CPC from Channel')
plt.show()

