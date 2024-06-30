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

#Conversion rate
conversion_rate=(df['Conversions'].sum()/df['Clicks'].sum())*100
print("conversion rate:",conversion_rate)

#conversion Per city
conversion_city=df['Conversions'].groupby(df["City"]).sum()/df['Clicks'].groupby(df["City"]).sum()*100
print("Conversion from  city",conversion_city)

Conversion per device
conversion_device=df['Conversions'].groupby(df["Device"]).sum()/df['Clicks'].groupby(df["Device"]).sum()*100
print("conversion from device",conversion_device)

#conversion Per month
conversion_month=df['Conversions'].groupby(df["Month"]).sum()/df['Clicks'].groupby(df["Month"]).sum()*100
print("conversion from month",conversion_month)

#profit
profit=df['Total conversion value, GBP'].sum()-df['Spend, GBP'].sum()
print("profit:",profit)
#profit per city
profit_city=df['Total conversion value, GBP'].groupby(df["City"]).sum()-df['Spend, GBP'].groupby(df["City"]).sum()
print("profit from city:",profit_city)
plt.bar(profit_city.index,profit_city.values)
plt.xlabel('City')
plt.ylabel('Profit')
plt.title('Profit from City')
plt.show()

#profit per channel
profit_channel=df['Total conversion value, GBP'].groupby(df["Channel"]).sum()-df['Spend, GBP'].groupby(df["Channel"]).sum()
print("profit from channel:",profit_channel)
plt.bar(profit_channel.index,profit_channel.values)
plt.xlabel('Channel')
plt.ylabel('Profit')
plt.title('Profit from Channel')
plt.show()

#profit per month
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

# Create a pivot table
pivot_table = df.pivot_table(index='Channel', columns='Device', values='Daily Average CPC', aggfunc='sum')
print(pivot_table)
# Plot the stacked bar chart
pivot_table.plot(kind='bar', stacked=False)
plt.xlabel('Channel')
plt.ylabel('CPC')
plt.title('CPC from Channel and Device')
plt.show()

#CPC  from ad
cpc_ad=df['Daily Average CPC'].groupby(df["Ad"]).sum()
print("cpc from ad:",cpc_ad)
plt.pie(cpc_ad,labels=cpc_ad.index,autopct='%1.1f%%',startangle=90)
plt.title('CPC from Ad')
plt.legend(prop={'size': 8})
plt.show()

#CPC from Device
cpc_device=df['Daily Average CPC'].groupby(df["Device"]).sum()
print("cpc from device:",cpc_device)
plt.pie(cpc_device,labels=cpc_device.index,autopct='%1.1f%%',startangle=90)
plt.title('CPC from Device')
plt.legend(prop={'size': 8})
plt.show()

#total Impressions per month
total_impressions_month=df['Impressions'].groupby(df["Month"]).sum()
print("total impressions:",total_impressions_month)
plt.bar(total_impressions_month.index,total_impressions_month.values)
plt.xlabel('Month')
plt.ylabel('Total Impressions')
plt.title('Total Impressions per Month')
plt.show()

# Create a pivot table to aggregate impressions by city and device
impression_pivot = df.pivot_table(index='City', columns='Device', values='Impressions', aggfunc='sum')
# Plot the stacked bar chart
impression_pivot.plot(kind='barh', stacked=False)
plt.xlabel('City')
plt.ylabel('Impressions')
plt.title('Impressions by City and Device')
plt.show()

#Impression per channel
impression_channel= df['Impressions'].groupby(df["Channel"]).sum()
print("impression from channel:",impression_channel)
plt.pie(impression_channel,labels=impression_channel.index,autopct='%1.1f%%',startangle=90)
plt.title('Impression from Channel')
plt.legend(prop={'size': 8})
plt.show()

#impression distribution
plt.figure(figsize=(10, 6))
sns.boxplot(x='Channel', y='Impressions', hue='Device', data=df)
plt.xlabel('Channel')
plt.ylabel('Impressions')
_ = plt.title('Impressions Distribution by Channel and Device')

like_pivot = df.pivot_table(index='Channel', columns='Device', values='Likes (Reactions)', aggfunc='sum')
print(pivot_table)
# Plot the stacked bar chart
like_pivot.plot(kind='bar', stacked=False)
plt.xlabel('Channel')
plt.ylabel('Likes')
plt.title('Likes by Channel and Device')
plt.show()

Comment_Pivot = df.pivot_table(index='Channel', columns='Device', values='Comments', aggfunc='sum')
print(Comment_Pivot)
# Plot the stacked bar chart
Comment_Pivot.plot(kind='bar', stacked=False)
plt.xlabel('Channel')
plt.ylabel('Comments')
plt.title('Comments by Channel and Device')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='City', y='Impressions', hue='Device', data=df)
plt.xlabel('City')
plt.ylabel('Impressions')
_ = plt.title('Impressions Distribution by City and Device')

#impression vs Clicks
impression_clicks=df['Impressions'].groupby(df["Clicks"]).sum()
print("impression from clicks:",impression_clicks)
plt.scatter(df['Impressions'],df['Clicks'])
plt.xlabel('Impressions')
plt.ylabel('Clicks')
plt.title('Impressions vs Clicks')
plt.show()

impression_click_campaign=df['Impressions'].groupby(df["Campaign"]).sum()
print("impression from campaign:",impression_click_campaign)
sns.scatterplot(x='Impressions', y='Clicks', hue='Campaign', data=df)
plt.xlabel('Impressions')
plt.ylabel('Clicks')
plt.title('Impressions vs Clicks by Campaign')
plt.show()

#Correlation Matrix
corr_matrix=df[["Likes (Reactions)", "Shares", "Comments"]].corr()
print(corr_matrix)
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')
plt.show()
