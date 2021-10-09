import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import preprocess
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

world_cups_matches = preprocess.world_cups_matches

# 2014년 정보 추출
world_cups_matches = world_cups_matches[world_cups_matches['Year'] == 2014]

# 홈 팀 데이터와 원정 팀 데이터 저장
home_team_goal = world_cups_matches.groupby(['Home Team Name'])['Home Team Goals'].sum()
away_team_goal = world_cups_matches.groupby(['Away Team Name'])['Away Team Goals'].sum()

# 홈 팀 데이터와 원정 팀 데이터 병합
team_goal_2014 = pd.concat([home_team_goal, away_team_goal], axis=1).fillna(0)
team_goal_2014['goals'] = team_goal_2014['Home Team Goals'] + team_goal_2014['Away Team Goals']
team_goal_2014 = team_goal_2014.drop(['Home Team Goals', 'Away Team Goals'], axis=1)

# 골 데이터 정렬
team_goal_2014 = team_goal_2014['goals'].sort_values(ascending=False)

# 골 데이터 int로 변환
team_goal_2014 = team_goal_2014.astype('int')

print(team_goal_2014)

team_goal_2014 = preprocess.team_goal_2014

team_goal_2014.plot(x=team_goal_2014.index, y=team_goal_2014.values, kind="bar", figsize=(12, 12), fontsize=14)

fig, ax = plt.subplots()
ax.bar(team_goal_2014.index, team_goal_2014.values)
plt.xticks(rotation = 90)
plt.tight_layout()

plt.savefig("image.svg", format="svg")
