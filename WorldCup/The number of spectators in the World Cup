import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

world_cups = pd.read_csv("WorldCups.csv")

world_cups = world_cups[['Year', 'Attendance']]
print(world_cups)

plt.plot(world_cups['Year'], world_cups['Attendance'], marker='o', color='black')

plt.savefig("image.svg", format="svg")
elice_utils.send_image("image.svg")
