
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#1
ipl_data=pd.read_csv("/content/Final Dataset - IPL.csv")
print(ipl_data.info())
numerical_columns = ipl_data.select_dtypes(include=['float64', 'int64']).columns
categorical_columns = ipl_data.select_dtypes(include=['object']).columns
print(numerical_columns)
print(categorical_columns)



#2
print("No of missing values")
print(ipl_data.isnull().sum())
#As the dataset doesnt contain any missing values there is no need to fill
#or drop them
print("No of duplicate values")
print(ipl_data.duplicated().sum())
ipl_data.drop_duplicates(inplace=True)#this line is used to remove the duplicates if any

#3
print(ipl_data.describe())
print(ipl_data[numerical_columns].var())

#Output of this code gives us insight about central_tendency and variability of the data

numeric_df = ipl_data.select_dtypes(include='number')

#4
ipl_data

#this pie chart gives information about the distribution of matches in each stadium
ipl_data['venue'].value_counts().plot(kind='pie')

#This gives a visual representation fo venues and no of matches held there during each stage
sns.heatmap(
pd.DataFrame({
    x_label: grp['stage'].value_counts()
    for x_label, grp in ipl_data.groupby('venue')
}),annot=True)
plt.xlabel('venue')
plt.ylabel('stage')

#This scatter plot gives insights about how fist_ings_wickets impact the score
ipl_data.plot(kind='scatter', x='first_ings_score', y='first_ings_wkts')
#similarly can be done with second_ings_score and second_ings_wkts

#These charts shows distribution of results
ipl_data.groupby('won_by').size().plot(kind='bar')

#This chart helps to understand distribution of toss decisions
ipl_data.groupby('toss_decision').size().plot(kind='bar')

#This code gives box plots for all the numerical columns
for i in numerical_columns:
  plt.figure(figsize = (5,5))
  sns.boxplot(data=numeric_df[i])
  plt.title(i)
  plt.ylabel('Values')
  plt.xticks(rotation = 45)
  plt.show()

#5
numeric_df['toss_decision']=ipl_data['toss_decision'].replace(['Bat','Field'],[1,2])
numeric_df['venue']=ipl_data['venue'].replace(['Wankhede Stadium, Mumbai', 'Brabourne Stadium, Mumbai',
       'Dr DY Patil Sports Academy, Mumbai',
       'Maharashtra Cricket Association Stadium,Pune',
       'Eden Gardens, Kolkata', 'Narendra Modi Stadium, Ahmedabad'],[1,2,3,4,5,6])
print(numeric_df.corr())
sns.heatmap(numeric_df.corr(),annot=True)

#6
for i in numerical_columns:
  plt.figure(figsize = (5,5))
  sns.boxplot(data=numeric_df[i])
  plt.title(i)
  plt.ylabel('Values')
  plt.xticks(rotation = 45)
  plt.show()

def outliers_detection(df,columns):
  for col in columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    #define bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)].index
    print("########",col,"#######")
    print(outliers)
    #replace outliers with the median of column--To treat the outliers
    #median = df[col].median()
    #df[col] = np.where((df[col] < lower_bound) | (df[col] > upper_bound), median, df[col])
    #return df

#This function prints the index of outliers in each columm
outliers_detection(numeric_df,numerical_columns)

#Treating the outliers in this scenerio is like getting to know the information of abnormality in the IPL.

#7The output gives performance trends and venue impact
#Print them seperately to view the output and we can get better insights
ipl_data.groupby(["venue","team1"])['match_winner'].size()
ipl_data.groupby(["venue","top_scorer"])['player_of_the_match'].size()
ipl_data.groupby(["venue","best_bowling"])['player_of_the_match'].size()
ipl_data.groupby(["venue",'stage',"team1"])['match_winner'].size()
ipl_data.groupby(["venue",'stage',"top_scorer"])['player_of_the_match'].size()
ipl_data.groupby(["venue",'stage',"best_bowling"])['player_of_the_match'].size()

#8
#Player of the match often
top_players=ipl_data['player_of_the_match'].value_counts()

#Lets consider top 3 players in the list and analyse
#Top player-kuldeep-yadav
print(top_players.index[0])
print("No of wickets taken")
print(ipl_data[ipl_data['player_of_the_match']==top_players.index[0]]['best_bowling_figure'].str[0].astype(int))
print("Total wickets for the team")
print(ipl_data[ipl_data['player_of_the_match']==top_players.index[0]]['best_bowling_figure'].str[0].astype(int).sum())
print(ipl_data[ipl_data['player_of_the_match']==top_players.index[0]]['match_winner'])

#top2
print("Scores")
print(ipl_data[ipl_data['player_of_the_match']==top_players.index[1]]['highscore'])
print("Total runs for the team")
print(ipl_data[ipl_data['player_of_the_match']==top_players.index[1]]['highscore'].sum())
print("Batting average")
print(ipl_data[ipl_data['player_of_the_match']==top_players.index[1]]['highscore'].mean())

print(ipl_data[ipl_data['player_of_the_match']==top_players.index[1]]['match_winner'])

#This template can be used for all the players to know their impact in the team\
#Their consistent performance is the reason for them winning player of the match award and also for their team to win

#9

#Inference
#CONSISTENCY OF PLAYERS:
In Sports always consistency is the key
Consistent performance of players collectively contribute to the success of the team
In 8th question we can understand that the consistent good performance have fetched the players player of match award and
also their team won the matches.

#Favourable conditions
Based on 7th question we can infer about the impact of home stadium for the home teams
and also for the individual performers of the team