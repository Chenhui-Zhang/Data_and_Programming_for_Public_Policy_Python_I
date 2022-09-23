import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#fig.show()
#fig.savefig('plot.png')
#fig.clear()

x = range(300)
y = np.random.choice([-1, 0, 1], 300)
y = np.cumsum(y) # random walk

fig, ax = plt.subplots()
ax.plot(x, y, 'b-', label='Blue line')
ax.legend(loc='upper center')

new_y = y[::-1] * 100
ax2 = ax.twinx()
ax2.plot(x, new_y, 'r-', label='Not the blue line')

#slide 12
fig, ax = plt.subplots()
ax.plot(x, y, 'b-', label='Blue line')
ax.plot(np.NaN, 'r-', label='Not the blue line')
ax.legend(loc='lower center')

ax2 = ax.twinx()
ax2.plot(x, new_y, 'r-', label='Not the blue line')

#slide 13
df = pd.DataFrame({'values_y1':y, 'values_y2':new_y})
ax = df.plot(secondary_y='values_y2')

#slide 14
fig, ax = plt.subplots(1, 1)
print(ax)

fig, ax = plt.subplots(2, 1)
print(ax)

fig, ax = plt.subplots(1, 2)
print(ax)

fig, ax = plt.subplots(2, 2)
print(ax)

#slide 18
def gen_ys(obs):
    y = np.random.choice([-1, 0, 1], obs)
    return np.cumsum(y) # random walk

fig, axs = plt.subplots(2, 2)

axs_flat = [s for sublist in axs for s in sublist]
ys = [gen_ys(300) for _ in range(4)]

for ax, y in zip(axs_flat, ys):
    ax.plot(x, y)
    
#slide 21
df = pd.DataFrame({'values_y1':gen_ys(300), 'values_y2':gen_ys(300), 
                  'values_y3':gen_ys(300), 'values_y4':gen_ys(300)})
df.plot(subplots=True)

#slide 22
fig, ax = plt.subplots()
ax.plot(range(100), gen_ys(100), linestyle='', marker='.', markersize=5)

fig, ax = plt.subplots()
ax.scatter(range(100), gen_ys(100))

#slide 24
x = [ 2,  4,  6,  8, 10]
y = [1., .2, .4, .7, .6]

fig, ax = plt.subplots()
ax.bar(x, y)

#slide 25
x = [np.random.normal(10, 2, 100),
     np.random.normal(11, 1, 100),
     np.random.normal(15, 4, 100)]

fig, ax = plt.subplots()
ax.boxplot(x)

#slide 26
df = pd.DataFrame(np.array(x).T, columns=['first', 'second', 'third'])
df.head()

sns.set()
sns.boxplot(data=df)

#slide 28
tips = sns.load_dataset('tips')
tips.head()

ax = sns.boxplot(x='day', y='total_bill',
                 hue='smoker', palette=['m', 'g'],
                 data=tips)

ax.set_ylabel('Total bill')
ax.set_xlabel('Day')
ax.set_title('Tips left by diners')
