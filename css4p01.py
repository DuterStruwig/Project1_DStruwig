# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:18:05 2024

@author: duter
"""

# Project Option 1
# Düter Struwig
# NWU-PC

import pandas
import seaborn as sns
import matplotlib.pyplot as plt

# PRELIMINARY OPERATIONS:
    
# Loading the csv file
df = pandas.read_csv("movie_dataset.csv")

# Creating column variables for each of the columns containing strings
column1 = "Title"
column2 = "Genre"
column3 = "Description"
column4 = "Director"
column5 = "Actors"

# Replacing the spaces with underscores
df[column1] = df[column1].str.replace(" ", "_")
df[column2] = df[column2].str.replace(" ", "_")
df[column3] = df[column3].str.replace(" ", "_")
df[column4] = df[column4].str.replace(" ", "_")
df[column5] = df[column5].str.replace(" ", "_")

# Creating column variables for each of the columns containign integers
column6 = "Year"
column7 = "Runtime (Minutes)"
column8 = "Rating"
column9 = "Votes"
column10 = "Revenue (Millions)"
column11 = "Metascore"

# Removing NaN's in the data
df = df.dropna(subset = [column6])
df = df.dropna(subset = [column7])
df = df.dropna(subset = [column8])
df = df.dropna(subset = [column9])
df = df.dropna(subset = [column10])
df = df.dropna(subset = [column11])

print(df)

# Getting basic info

print(df.info())

"""
<class 'pandas.core.frame.DataFrame'>
Index: 838 entries, 0 to 999
Data columns (total 12 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   Rank                838 non-null    int64  
 1   Title               838 non-null    object 
 2   Genre               838 non-null    object 
 3   Description         838 non-null    object 
 4   Director            838 non-null    object 
 5   Actors              838 non-null    object 
 6   Year                838 non-null    int64  
 7   Runtime (Minutes)   838 non-null    int64  
 8   Rating              838 non-null    float64
 9   Votes               838 non-null    int64  
 10  Revenue (Millions)  838 non-null    float64
 11  Metascore           838 non-null    float64
dtypes: float64(3), int64(4), object(5)
memory usage: 85.1+ KB
"""

print(df.describe())

"""
              Rank        Year  ...  Revenue (Millions)   Metascore
count   838.000000   838.00000  ...          838.000000  838.000000
mean    485.247017  2012.50716  ...           84.564558   59.575179
std     286.572065     3.17236  ...          104.520227   16.952416
min       1.000000  2006.00000  ...            0.000000   11.000000
25%     238.250000  2010.00000  ...           13.967500   47.000000
50%     475.500000  2013.00000  ...           48.150000   60.000000
75%     729.750000  2015.00000  ...          116.800000   72.000000
max    1000.000000  2016.00000  ...          936.630000  100.000000
"""

# Answering questions

# QUESTION 1:

Rating = "Rating"
Title = "Title"

max_Rating = df[Rating].max() #Finding the maximum rating in the data
max_row = df.loc[df[Rating] == max_Rating] #Locating the row of the in which the maximum rating is present
max_Title = max_row[Title].iloc[0] #Locating the movie titla corresponding to the maximum rating

print("Maximum Rating:", max_Rating)
print("Title:", max_Title)

"""
Maximum Rating: 9.0
Title: The_Dark_Knight
"""

# QUESTION 2:

Rev_avg = df["Revenue (Millions)"].mean() #Finding the average revenue
    
print("Average Revenue:", Rev_avg)

"""
Average Revenue: 84.5645584725537
"""

# QUESTION 3:

year_range = df[(df["Year"] >= 2015) & (df["Year"] <= 2017)] #Creating a table containing the data in the year range specified

avg_rev_15_17 = year_range["Revenue (Millions)"].mean()

print(f"The average revenue from 2015 to 2017 is: {avg_rev_15_17}")

"""
The average revenue from 2015 to 2017 is: 64.49895765472313
"""

# QUESTION 4:

df2 = pandas.read_csv("movie_dataset.csv")

year_2016 = df2[df2["Year"] == 2016] #Finding all the movies made in 2016

count_2016 = len(year_2016) #Counting the number of movies made in 2016

print(f"{count_2016} movies were released in 2016")

"""
297 movies were released in 2016
"""

# QUESTION 5:

counts = df["Director"].value_counts() #Counting the number of movies directed by each director

nolan_count = counts.loc["Christopher_Nolan"] #Getting the number of movies directed by CN

print(f"{nolan_count} movies were directed by Cristopher Nolan")

"""
5 movies were directed by Cristopher Nolan
"""

# QUESTION 6:

rating_count = df2['Rating'].value_counts().sort_index()[8.0:].sum() #Finding the number of movies having a rating equal or higher than 8

print(f"{rating_count} have rating greater at of least 8.0")

"""
78 have rating greater at of least 8.0
"""

# QUESTION 7:

df_nolan = df[df["Director"] == "Christopher_Nolan"] #New table with the information of the movies directed by CN

median_nolan_rating = df_nolan["Rating"].median()

print(f"The median rating of movies directed by Christopher Nolan is {median_nolan_rating}")

"""
The median rating of movies directed by Christopher Nolan is 8.6
"""

# QUESTION 8:

mean_year_rating = df.groupby(df["Year"])["Rating"].mean() #Getting the mean rating for all the movies in each of the years

highest_year = mean_year_rating.idxmax()

print(f"The year with the highest average rating is {highest_year}")

"""
The year with the highest average rating is 2006
"""

# QUESTION 9:

df_2006 = df2[df2["Year"] == 2006] #All movies made in 2006
df_2016 = df2[df2["Year"] == 2016] #All movies made in 2016

count_2006 = len(df_2006) #Number of movies made in 2006
count_2016 = len(df_2016) #Number of movies made in 2016

print(f"The number of movies made in 2006 is {count_2006}")
print(f"The number of movies made in 2016 is {count_2016}")

perc_inc = (count_2016 - count_2006)/count_2006*100 #Calculating the percentage increase in movies made between the two years

print(f'The percentage increase in number of movies made between 2006 and 2016 is {perc_inc:.2f}%')

"""
The number of movies made in 2006 is 44
The number of movies made in 2016 is 297
The percentage increase in number of movies made between 2006 and 2016 is 575.00%
"""

# QUESTION 10:

actors_freq = df["Actors"].str.split(",").explode().value_counts() #Frequency of actors in movies

most_common_actor = actors_freq.idxmax() #Finding the most common actor in the list of movies

print(f"The most common actor in all the movies is: {most_common_actor}")

"""
The most common actor in all the movies is: Mark_Wahlberg
"""

# QUESTION 11:

df["Genre_list"] = df["Genre"].str.split(",") #Creating a list of all the genres

df_exploded = df.explode("Genre_list") #Seperating all the genres in a single movie into seperate columns

num_genres = df_exploded["Genre_list"].nunique() #Finding the number of unique genres (Number of different genres in all the movies present)

print(f"The number of unique genres in the dataset is: {num_genres}")

"""
The number of unique genres in the dataset is: 20
"""

# QUESTION 12:

num_df = df.select_dtypes(include='number') #New table with only integer data

corr_matrix = num_df.corr() #Creating a correlation matrix of the data columns

print(corr_matrix)
sns.heatmap(corr_matrix, annot=True)
plt.show()



