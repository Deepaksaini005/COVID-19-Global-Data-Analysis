import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset - covid_19_clean_complete.csv
data = pd.read_csv(r"C:\Users\saini\Downloads\archive (3)\covid_19_clean_complete.csv")

print(data.head())  # top 5 rows
print(data.info())  #  checking for the data types and missing values
print(data.describe())  # statistical summary of the dataset

#Anlaysis of  data

country_data = data.groupby('Country/Region').sum().reset_index()  # Grouping the data by 'Country/Region' .
print(country_data.head())  # top 5 rows of the grouped data


# top 5 contries with the highest number of confirmed cases

top_contries = country_data.sort_values(by='Confirmed', ascending=False).head(5)
print(top_contries[['Country/Region', 'Confirmed']])  # confirmed cases of top 5 countries


# Visualization of the top 5 countries with the highest number of confirmed cases
c = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300']  # colors for the pie chart
plt.figure(figsize=(10, 6))
plt.pie(top_contries['Confirmed'], labels= top_contries['Country/Region'] , autopct = '%1.1f%%', startangle=140 , colors=c , explode=[0.1, 0.0, 0.0, 0.0, 0.0])  # explode is used to separate the slices of the pie chart
plt.title('Top 5 Countries with Highest Confirmed Cases')
plt.savefig('top_country vs confirmed.png')  # Save the figure as a PNG file
plt.show()


# top 5 contries with the highest number of deaths
top_deaths = country_data.sort_values(by='Deaths', ascending=False).head(5)
print(top_deaths[['Country/Region', 'Deaths']])  # death cases of top 5 countries

# Visual through the line plot
sns.lineplot(data = top_deaths, x='Country/Region', y='Deaths', marker='o', alpha=0.7,color='red')
plt.title('Top 5 Countries with Highest Deaths')
plt.xlabel('Country/Region')
plt.ylabel('Number of Deaths')
plt.savefig('top_country vs deaths.png')  # Save the figure as a PNG file
plt.show()


# top 3 contries  with  the highest number of recoveries 

top_recovered = country_data.sort_values(by='Recovered', ascending=False).head(3)
print(top_recovered[['Country/Region', 'Recovered']])  # recovered cases of top 3 countries

# visual  through the bar plot
sns.barplot(data = top_recovered, x = 'Country/Region', y = 'Recovered', palette='viridis')
plt.title('Top 3 Countries with Highest Recoveries')
plt.xlabel('Country/Region')
plt.ylabel('Number of Recoveries')
plt.savefig('top_country vs recovered.png')  # Save the figure as a PNG file
plt.show()


# top 3 countries with the highest number of active cases

top_active =  country_data.sort_values(by = "Active" , ascending=False).head(3)
print(top_active[['Country/Region', 'Active']])  # active cases of top 3 countries

# visual through the bar plot -  #add counts of actives

ax = sns.barplot(
    data=top_active,
    x='Country/Region',
    y='Active',
    palette='magma'
)

for i, v in enumerate(top_active['Active']): # i and v are the index and value of the active cases respectively
    ax.text(i, v, str(v), ha='center', va='bottom')  # va is vertical alignment and ha is horizontal alignment

plt.title('Top 3 Countries with Highest Active Cases')
plt.xlabel('Country/Region')
plt.ylabel('Number of Active Cases')
plt.savefig('top_country vs active.png')  # Save the figure as a PNG file
plt.show()



# WHO region wise analysis


region_data = data.groupby('WHO Region').sum().reset_index()  # Grouping the data by 'WHO Region'
print(region_data.head())  # top 5 rows of the grouped data


# top 5 WHO regions with the highest number of confirmed cases

top_regions = region_data.sort_values(by='Confirmed', ascending=False).head(5)
print(top_regions[['WHO Region', 'Confirmed']])  # confirmed cases of top 5 regions

# visual through the area plot

plt.figure(figsize=(10, 6)) 
plt.fill_between(top_regions['WHO Region'], top_regions['Confirmed'], color='#871A04', alpha=0.5) # fill_between is used to create an area plot 
plt.plot(top_regions['WHO Region'], top_regions['Confirmed'], marker='o', color='red')  # line plot on top of the area plot
plt.title('Top 5 WHO Regions with Highest Confirmed Cases')
plt.xlabel('WHO Region')
plt.ylabel('Number of Confirmed Cases')
plt.savefig('top_regions vs confirmed.png')  # Save the figure as a PNG file
plt.show()




# Mortality rate by deaths and confirmed cases   (mortality rate = (deaths / confirmed cases) * 100)

country_data["Mortality Rate"] = (country_data["Deaths"] / country_data["Confirmed"]) * 100  # calculating the mortality rate
top_mortality = country_data.sort_values(by='Mortality Rate', ascending=False).head(5)  # top 5 countries with the highest mortality rate
print(top_mortality[['Country/Region', 'Mortality Rate']])  # mortality rate of top 5 countries


#Donut chart for mortality rate of top 5 countries

c = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300']

plt.figure(figsize=(10, 6))
plt.pie(top_mortality['Mortality Rate'], labels=top_mortality['Country/Region'], autopct='%1.1f%%', startangle=140, colors=c , explode=[0.2, 0.0, 0.0, 0.0, 0.0])  # explode is used to separate the slices of the pie chart
plt.title('Top 5 Countries with Highest Mortality Rate')

# Draw a white circle at the center to create a donut chart
centre_circle = plt.Circle((0, 0), 0.60, fc='white' )  # explode is used to separate the slices of the pie chart
fig = plt.gcf()  # Get the current figure
fig.gca().add_artist(centre_circle) # Add the circle to the plot to create the donut effect
plt.legend(top_mortality['Country/Region'], title='Countries', loc='upper left')  # Add a legend to the plot
plt.savefig('top_mortality_rate.png')  # Save the figure as a PNG file
plt.show()





# Correlation between confirmed cases and deaths

sns.scatterplot(data=country_data, x='Confirmed', y='Deaths',  color='orange')
plt.title('Correlation between Confirmed Cases and Deaths')
plt.xlabel('Number of Confirmed Cases')
plt.ylabel('Number of Deaths')
plt.savefig('correlation_confirmed_deaths.png')  # Save the figure as a PNG
plt.show()


# Correlation between confirmed cases and recoveries
sns.scatterplot(data=country_data, x='Confirmed', y='Recovered', color='green')
plt.title('Correlation between Confirmed Cases and Recoveries')
plt.xlabel('Number of Confirmed Cases')
plt.ylabel('Number of Recoveries')
plt.savefig('correlation_confirmed_recovered.png')  # Save the figure as a PNG
plt.show()


# heatmap to show the correlation between confirmed cases, deaths, recoveries and active cases
correlation_data = country_data[['Confirmed', 'Deaths', 'Recovered', 'Active']]    
correlation_matrix = correlation_data.corr()  # calculating the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)  # heatmap to show the correlation matrix
plt.title('Correlation Matrix of COVID-19 Cases')
plt.savefig('correlation_matrix.png')  # Save the figure as a PNG  
plt.show()


# Time series analysis of confirmed cases in the top 5 countries
top_countries_time_series = data[data['Country/Region'].isin(top_contries['Country/Region'])]  # filtering the data for the top 5 countries
plt.figure(figsize=(10, 6)) 
sns.lineplot(data=top_countries_time_series, x='Date', y='Confirmed', hue='Country/Region', marker='o')  # line plot to show the time series of confirmed cases in the top 5 countries
plt.title('Time Series of Confirmed Cases in Top 5 Countries')
plt.xlabel('Date')
plt.ylabel('Number of Confirmed Cases')
plt.legend(title='Country/Region')
plt.savefig('time_series_confirmed_cases.png')  # Save the figure as a PNG
plt.show()
