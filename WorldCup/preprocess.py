import pandas as pd
import numpy as np
world_cups_matches = pd.read_csv("WorldCupMatches.csv")
world_cups_matches = world_cups_matches.replace('Germany FR', 'Germany')
world_cups_matches = world_cups_matches.replace('C�te d\'Ivoire', 'Côte d\'Ivoire')
world_cups_matches = world_cups_matches.replace('rn">Republic of Ireland',"Republic of Ireland")
world_cups_matches = world_cups_matches.replace('rn">Bosnia and Herzegovina',"Bosnia and Herzegovina")
world_cups_matches = world_cups_matches.replace('rn">Serbia and Montenegro',"Serbia and Montenegro")
world_cups_matches = world_cups_matches.replace('rn">Trinidad and Tobago',"Trinidad and Tobago")
world_cups_matches = world_cups_matches.replace('rn">United Arab Emirates',"United Arab Emirates")
world_cups_matches = world_cups_matches.replace("Soviet Union","Russia")
world_cups_matches = world_cups_matches.drop_duplicates()
home = world_cups_matches[['Home Team Name', 'Home Team Goals']]
away = world_cups_matches[['Away Team Name', 'Away Team Goals']]
goal_per_country = pd.DataFrame(columns=['countries', 'goals'])
goal_per_country = goal_per_country.append(home.rename(columns={'Home Team Name': 'countries', 'Home Team Goals': 'goals'}))
goal_per_country = goal_per_country.append(away.rename(columns={'Away Team Name': 'countries', 'Away Team Goals': 'goals'}))
goal_per_country = goal_per_country.groupby(['countries'])['goals'].sum().sort_values(ascending=False)
world_cups_matches = world_cups_matches[world_cups_matches['Year']==2014]
home_team_goal = world_cups_matches.groupby(['Home Team Name'])['Home Team Goals'].sum()
away_team_goal = world_cups_matches.groupby(['Away Team Name'])['Away Team Goals'].sum()
team_goal_2014 = pd.concat([home_team_goal, away_team_goal], axis=1)
team_goal_2014 = team_goal_2014.fillna(0)
team_goal_2014['goals'] = team_goal_2014['Home Team Goals'] + team_goal_2014['Away Team Goals']
team_goal_2014 = team_goal_2014.drop(['Home Team Goals', 'Away Team Goals'], axis=1)
team_goal_2014 = team_goal_2014['goals'].sort_values(ascending=False)
team_goal_2014.astype('int')
