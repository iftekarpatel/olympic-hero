# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns = {'Total':'Total_Medals'},inplace = True)
data.head(10)


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer']>=data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] =np.where(data['Total_Summer'] ==data['Total_Winter'],'Both',data['Better_Event']) 
better_event = data['Better_Event'].value_counts().idxmax()


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(axis=0, index=146,inplace = True)

top_10_summer = ['United States', 'Soviet Union', 'Great Britain', 'France', 'Germany', 'Italy', 'Sweden', 'Hungary', 'China', 'Australia']
top_10_winter = ['Norway', 'United States', 'Austria', 'Germany', 'Soviet Union', 'Canada', 'Finland', 'Sweden', 'Switzerland', 'Russia']
top_10 = ['United States', 'Soviet Union', 'Great Britain', 'Germany', 'France', 'Italy', 'Sweden', 'China', 'East Germany', 'Russia']
common = ['United States', 'Sweden', 'Germany', 'Soviet Union']


# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
import matplotlib.pyplot as plt
summer_df.plot(x='Country_Name', y='Total_Summer', kind='bar',title='summer_df')
winter_df.plot(x='Country_Name', y='Total_Winter', kind='bar',title='winter_df')
top_df.plot(x='Country_Name', y='Total_Medals', kind='bar',title='top_df')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_df.set_index('Country_Name', inplace=True)
summer_country_gold = summer_df['Golden_Ratio'].idxmax()
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_df.set_index('Country_Name', inplace=True)
winter_country_gold = winter_df['Golden_Ratio'].idxmax()
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_df.set_index('Country_Name', inplace=True)
top_country_gold = top_df['Golden_Ratio'].idxmax()


# --------------
#Code starts here
data_1=data[:-1]
#data_1 = data.drop(axis=0, index=146,inplace = True)


data_1['Total_Points'] = ((data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']))
most_points=max(data_1['Total_Points']) 
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
#most_points=5684
#best_country= 'United States'



# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar',stacked=True, figsize=(15,20),fontsize=12)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


