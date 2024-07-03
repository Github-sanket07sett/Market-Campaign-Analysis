# Onyx Marketing Campaign Analysis
This repository contains the analysis of the Onyx marketing campaign data, focusing on the performance of different ad campaigns across various cities and channels. The analysis leverages Python for data manipulation and visualization to derive insights from the data.
## TABLE OF CONTENTS
- [Project overview](#project-overview)
- [Methodology](#methodology)
- [CODE SNIPPETS](#code-snippets)
- [Key Insights](#key-insights)
## Project overview
The Onyx Marketing Campaign Analysis project aims to provide insights into the effectiveness of various ad campaigns conducted on different channels such as Facebook. The data includes metrics such as impressions, clicks, conversions, and more, segmented by date, city, and device.
## Objectives
The main objectives of this project are:
1. Analyze Campaign Performance: Evaluate the performance of ad campaigns based on key metrics like impressions, clicks, and conversions.
2. Channel Comparison: Compare the effectiveness of different marketing channels in reaching and engaging the audience.
3. Device Analysis: Understand how the type of device influences user interaction and conversion rates.
4. City-Wise Insights: Identify which cities have the highest engagement and conversion rates.
5. Cost Efficiency: Determine the cost-effectiveness of ad spends and identify opportunities for optimization.
## Dataset
The dataset includes the following columns:
1. Campaign: The campaign season (e.g., Spring).
2.Month: The month of the campaign.
3. Day of the Week: The day of the week.
4. Date: The specific date of the campaign.
5. City: The city where the campaign was run.
6. Channel: The marketing channel (e.g., Facebook).
7. Device: The type of device used (e.g., Desktop).
8. Ad: The type of ad.
9. Impressions: The number of times the ad was shown.
10. CTR: Click-through rate.
11. Clicks: The number of clicks on the ad.
12. Daily Average CPC: Daily average cost per click.
13. Spend, GBP: The amount spent in GBP.
14. Conversions: The number of conversions.
15. Total conversion value, GBP: The total value of conversions in GBP.
16. Likes (Reactions): The number of likes or reactions.
17. Shares: The number of shares.
18. Comments: The number of comments.

## Methodology
1. Data Loading: Loads the dataset and displays the first few rows.
2. Data Cleaning: Handles missing values and formats the data.
3. Exploratory Data Analysis (EDA): Generates visualizations to understand the distribution of key metrics.
4. Performance Metrics: Analyzes the performance of campaigns by channel, city, and device.
5. Insights: Provides actionable insights based on the data analysis.

## CODE SNIPPETS
![s1](https://github.com/Github-sanket07sett/Market-Campaign-Analysis/assets/137095374/98ec7d93-338a-40d2-bc98-2734f9fe5f75)![s2](https://github.com/Github-sanket07sett/Market-Campaign-Analysis/assets/137095374/26d42165-4641-4f3b-a11c-3f9674052cbe)
![s3](https://github.com/Github-sanket07sett/Market-Campaign-Analysis/assets/137095374/6e2a21b1-c7db-40bc-a02c-94d202681f94)
![s4](https://github.com/Github-sanket07sett/Market-Campaign-Analysis/assets/137095374/8364901f-9ba0-489b-bd7d-8c8c2fda3325)
![s7](https://github.com/Github-sanket07sett/Market-Campaign-Analysis/assets/137095374/4e981e9a-bb35-4de6-9165-2328b08004ba)
## Key insights
some of the Insights are here. Please Go through the ## Market.ipynb file for detailed analysis.
![Screenshot 2024-07-01 110928](https://github.com/Github-sanket07sett/Market-Campaign-Analysis/assets/137095374/6a58100e-7415-4e3a-823f-5faf7fcc6d0b)
![Screenshot 2024-07-01 110947](https://github.com/Github-sanket07sett/Market-Campaign-Analysis/assets/137095374/83949619-a8f4-440d-a68e-d1cbad89e1a9)
## Key Visualisations
 ### Correlation Matrix
#### Description: This heatmap visualizes the correlation between different social media engagement metrics: Likes (Reactions), Shares, and Comments.
#### Insights:
1. Likes and Shares have a moderate positive correlation (0.3).
2. There is a weak positive correlation between Likes and Comments (0.061).
3. Shares and Comments have a negligible correlation (-0.0084).
### Scatter Plot: Impressions vs. Clicks by Campaign
#### Description: This scatter plot shows the relationship between the number of impressions and clicks for different campaigns (Spring, Summer, Fall).
#### Insights:
1. There is a positive correlation between impressions and clicks across all campaigns.
2. Spring campaign has the highest spread of impressions and clicks, indicating a wide range of engagement.
3. Summer campaign shows lower impressions and clicks compared to Spring and Fall.
4. Fall campaign also shows a strong positive correlation, but with a slightly lower range compared to Spring.
### Bar Chart: Total Sales per Month
#### Description: This bar chart shows the total sales conversion values per month in GBP.
#### Insights:
1. November has the highest total sales, followed by October and September.
2. The summer months (June, July, August) have relatively lower sales compared to the fall months.
3. There is a noticeable increase in sales starting from September, peaking in November.

