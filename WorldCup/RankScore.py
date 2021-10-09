import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

world_cups = pd.read_csv("WorldCups.csv")

winner = world_cups["Winner"]
runners_up = world_cups["Runners-Up"]
third = world_cups["Third"]
fourth = world_cups["Fourth"]

winner_count = pd.Series(winner.value_counts())
runners_up_count = pd.Series(runners_up.value_counts())
third_count = pd.Series(third.value_counts())
fourth_count = pd.Series(fourth.value_counts())


ranks = pd.DataFrame({"Winner" : winner_count,
                      "Runners_Up" : runners_up_count,
                      "Third" : third_count,
                      "Fourth" : fourth_count})

ranks = ranks.fillna(0).astype('int64')
ranks = ranks.sort_values(['Winner', 'Runners_Up', 'Third', 'Fourth'], ascending=False)


print(ranks)

ranks = preprocess.ranks

# x축에 그려질 막대그래프들의 위치입니다.
x = np.array(list(range(0, len(ranks))))

# 그래프를 그립니다.
fig, ax = plt.subplots()

# x 위치에, 항목 이름으로 ranks.index(국가명)을 붙입니다.
plt.xticks(x, ranks.index, rotation=90)
plt.tight_layout()

# 4개의 막대를 차례대로 그립니다.
ax.bar(x - 0.3, ranks['Winner'],     color = 'gold',   width = 0.2, label = 'Winner')
ax.bar(x - 0.1, ranks['Runners_Up'], color = 'silver', width = 0.2, label = 'Runners_Up')
ax.bar(x + 0.1, ranks['Third'],      color = 'brown',  width = 0.2, label = 'Third')
ax.bar(x + 0.3, ranks['Fourth'],     color = 'black',  width = 0.2, label = 'Fourth')



plt.savefig("image.svg", format="svg")

