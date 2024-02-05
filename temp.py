# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script
"""

import pandas as pd 

file_path = "movie_dataset.csv"
df = pd.read_csv(file_path)
print(df)

df['Revenue(Millions)'] = pd.to_numeric(df['Revenue(Millions)'], errors= 'coerce')
df['Revenue(Millions)'] = df['Revenue(Millions)'].fillna(df['Revenue'].mean())

highest_rated_movie = df.loc[df['Rating'].idxmax()]['Title']
print(highest_rated_movie)
                
average_revenue= df['Revenue(Millions)'].mean() 
print(average_revenue)

Average_revenue_2015_2017= df[(df['Year']>= 2015) & (df['Year']<=2017)]['Revenue(Millions)'].mean() 
print(Average_revenue_2015_2017)    
            
movies_2016 = df[df['Director']== 'christopher Nolan'].shape[0]
print(movies_2016)

high_rated_movies = df[df['Rating'] >= 8.0].shape[0]
print(high_rated_movies)

median_rating_nolan = df[df['Director'] == 'Christopher Nolan']['Rating'].median()
print(median_rating_nolan)

year_highest_avg_rating = df.groupby('Year')['Rating'].mean().idxmax()
print(year_highest_avg_rating)

movies_2006 = df[df['Year'] == 2006].shape[0]
movies_2016 = df[df['Year'] == 2016].shape[0]
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(movies_2006 )

most_common_actor = df['Actors'].str.split(', ').explode().mode()[0]
print(most_common_actor)

unique_genres_count = df['Genre'].str.split(', ').explode().nunique()
print(unique_genres_count)

import seaborn as sns
import matplotlib.pyplot as plt

numerical_columns = df. select_dtypes(include=['float64','int64']).columns
numerical_features_df= df[numerical_columns]

correlation_matrix = numerical_features_df.corr()
print("correlation Matrix:")
print(correlation_matrix)

print("\nInsights:")
print(correlation_matrix.unstack().sort_values(ascending=False).drop_duplicates().head(6))


plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True,cmap ='coolwarm',linewidths=.5)
plt.tittle('Correlation Matrix of numerical Features')
print.show()















