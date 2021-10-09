import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import preprocess
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


# 1. 데이터 전처리 과정
world_cups_matches = preprocess.world_cups_matches


# 2. 홈 경기 기록과 원정 경기 기록 저장
home = world_cups_matches[['Home Team Name', 'Home Team Goals']]
away = world_cups_matches[['Away Team Name', 'Away Team Goals']]


# 3. 홈 경기와 원정 경기 통합
goal_per_country = pd.DataFrame(columns=['countries', 'goals'])
goal_per_country = goal_per_country.append(home.rename(columns={'Home Team Name': 'countries', 'Home Team Goals': 'goals'}))

goal_per_country = goal_per_country.append(away.rename(columns={'Away Team Name': 'countries', 'Away Team Goals': 'goals'}))


# 4. 국가별 골 기록 집계
goal_per_country = goal_per_country.groupby(['countries'])['goals'].sum().sort_values(ascending=False)
goal_per_country = goal_per_country.astype(int)
print(goal_per_country)

oal_per_country = preprocess.goal_per_country
goal_per_country = goal_per_country[:10]

# x, y값 저장
x = goal_per_country.index
y = goal_per_country.values

#그래프 그리기
fig, ax = plt.subplots()

ax.bar(x, y, width = 0.5)

# x축 항목 이름 지정, 30도 회전
plt.xticks(x, rotation=30)
plt.tight_layout()

#그래프 출력
plt.savefig("image.svg", format="svg")
