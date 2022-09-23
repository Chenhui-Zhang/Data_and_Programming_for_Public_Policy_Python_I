import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = range(300)
y = np.random.choice([-1, 0, 1], 300)
y = np.cumsum(y) # random walk

fig, ax = plt.subplots()
ax.plot(x, y)

#slide 8
fig, ax = plt.subplots()
ax.plot(x, y, color='red', linestyle='solid')

fig, ax = plt.subplots()
ax.plot(x, y, color='black', linestyle='dashed')

fig, ax = plt.subplots()
ax.plot(x, y, color='green', linestyle='solid', marker='o', linewidth=2, 
        markersize=5, markerfacecolor='red', markeredgecolor='black')

fig, ax = plt.subplots()
ax.plot(x, y, 'r-')

fig, ax = plt.subplots()
ax.plot(x, y, 'k--')

#slide 12
fig, ax = plt.subplots()
ax.plot(x, y, 'r-', label='A red line')
ax.legend(loc='best')

fig, ax = plt.subplots()
ax.plot(x, y, 'r-', label='A red line')
ax.plot(x, y[::-1], 'b-', label='A blue line')
ax.legend(loc='best')

#slide 19
fig, ax = plt.subplots()
ax.plot(x, y, 'b-')

ax.set_ylabel('Hello Y axis')
ax.set_xlabel('X Axis is here')
ax.set_title('The plot title says hi')

#slide 20
fig, ax = plt.subplots()
ax.plot(x, y, 'b-')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.axvline(150, color='k', linestyle=':')
ax.axhline(5, color='k', linestyle=':')

#slide 22
plt.plot(x, y, 'b-')

fig, ax = plt.subplots()
ax.plot(x, y, 'b-')

#slide 24
df = pd.DataFrame({'values_x':x, 'values_y':y})
df

df.plot(x='values_x', y='values_y')

#slide 26
ax = df.plot(x='values_x', y='values_y')
ax.axvline(150, color='k', linestyle=':')

