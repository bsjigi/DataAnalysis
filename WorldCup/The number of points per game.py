import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
world_cups = pd.read_csv("WorldCups.csv")


world_cups = world_cups[['Year', 'GoalsScored', 'MatchesPlayed']]
world_cups["GoalsPerMatch"] = world_cups["GoalsScored"] / world_cups["MatchesPlayed"]
print(world_cups)

# 첫 번째 그래프 출력
fig, axes = plt.subplots(2, 1, figsize=(4,8))

axes[0].bar(x=world_cups['Year'], height=world_cups['GoalsScored'], color='grey', label='goals')

axes[0].plot(world_cups['Year'], world_cups['MatchesPlayed'], marker='o', color='blue', label='matches')

axes[0].legend(loc='upper left')


# 두 번째 그래프 출력
axes[1].grid(True)
axes[1].plot(world_cups['Year'], world_cups['GoalsPerMatch'], marker='o', color='red', label='goals_per_matches')

axes[1].legend(loc='lower left')

plt.savefig("image.svg", format="svg")
