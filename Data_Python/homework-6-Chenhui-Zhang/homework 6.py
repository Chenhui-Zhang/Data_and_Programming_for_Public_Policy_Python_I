# PPHA 30535
# Spring 2022
# Homework 6

# YOUR NAME HERE
# Chenhui Zhang

# YOUR CANVAS NAME HERE
# Chenhui Zhang
# YOUR GITHUB USER NAME HERE
# Chenhui-Zhang

# Due date: Sunday May 15th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_plot.png", "q2_plot.png", etc. If a question calls
# for more than one plot, name them "q1a_plot", "q1b_plot", etc.

#NOTE: If no specific library is called for by the question, then you may freely
# use Matplotlib, Pandas, Seaborn, or a combination to answer the question.

# Question 1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis labels are legible.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

fig, ax=plt.subplots()
ax.scatter(x,y1,color='pink',label='y1')
ax.plot(x,y2,color='blue',label='y2')
ax.legend(loc='best')
fig.savefig('q1_plot.png')


# Question 2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.

fig,ax=plt.subplots()
x=np.linspace(0,8,100)
y1=x
y2=8.5-x
ax.plot(x,y1,color='blue',label='Blue')
ax.plot(x,y2,color='red',label='Red')
ax.legend(loc='center left')
ax.set_title('X marks the spot')
x_ticks=np.arange(0,10,2)
y_ticks=np.arange(0,10,2)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
ax.spines['left'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.set_facecolor('none')
fig.savefig('q2_plot.png')

# Question 3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.

mpg=pd.read_csv('D:\Spring2022\Data_Python\homework-6-Chenhui-Zhang\mpg.csv')
fig, ax=plt.subplots()
x=mpg['displacement']
y=mpg['mpg']
ax.scatter(x,y)
ax.set_title('Displacement and Gas Mileage')
ax.set_xlabel('Displacement')
ax.set_ylabel('Gas Mileage')
fig.savefig('q3a_plot.png')

fig,ax=plt.subplots()
x=mpg['horsepower']
y=mpg['mpg']
ax.scatter(x,y)
ax.set_title('Horsepower and Gas Mileage')
ax.set_xlabel('Horsepower')
ax.set_ylabel('Gas Mileage')
fig.savefig('q3b_plot.png')

fig,ax=plt.subplots()
x=mpg['weight']
y=mpg['mpg']
ax.scatter(x,y)
ax.set_title('Weight and Gas Mileage')
ax.set_xlabel('Weight')
ax.set_ylabel('Gas Mileage')
fig.savefig('q3c_plot.png')    

# Question 4: Continuing from question 3, create a scatter plot with mpg
# on the y-axis and cylinders on the x-axis.  Explain what is wrong with this
# plot with a one-line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.

fig,ax=plt.subplots()
x=mpg['cylinders']
y=mpg['mpg']
ax.scatter(x,y)
ax.set_title('Cylinders and Gas Mileage')
ax.set_xlabel('Cylinders')
ax.set_ylabel('Gas Mileage')
fig.savefig('q4a_plot.png')
# We cannot tell the relationship between cylinders and mpg clearly from this scatterplot. 

import seaborn as sns
plt.figure()
seaborn_plot=sns.boxplot(data=mpg,x=mpg['cylinders'],y=mpg['mpg'])
seaborn_plot.set_title('Cylinders and Gas Mileage')
seaborn_plot.set_xlabel('Cylinders')
seaborn_plot.set_ylabel('Gas Mileage')
fig=seaborn_plot.get_figure()
fig.savefig('q4b_plot.png')

#Ref: https://stackoverflow.com/questions/32244753/how-to-save-a-seaborn-plot-into-a-file

# Question 5: Continuing from question 3, create a two-by-two grid of
# subplots, where each one has mpg on the y-axis and one of displacement,
# horsepower, weight, and acceleration on the x-axis.  To clean up this 
# plot, remove the y-axis labels on the right two plots - the scale will 
# already be aligned because the mpg values are the same.

x1=mpg['displacement']
x2=mpg['horsepower']
x3=mpg['weight']
x4=mpg['acceleration']
y=mpg['mpg']
fig,ax=plt.subplots(2,2)
ax[0][0].scatter(x1,y)
ax[0][0].set_xlabel('displacement')
ax[0][0].set_ylabel('mpg')
ax[0][1].scatter(x2,y)
ax[0][1].set_xlabel('horsepower')
ax[0][1].yaxis.set_visible(False)
ax[1][0].scatter(x3,y)
ax[1][0].set_xlabel('weight')
ax[1][0].set_ylabel('mpg')
ax[1][1].scatter(x4,y)
ax[1][1].set_xlabel('acceleration')
ax[1][1].yaxis.set_visible(False)
fig.tight_layout()
fig.savefig('q5_plot.png')

# Question 6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot.
plt.figure()
sns.set()
ax=sns.boxplot(x=mpg['origin'],y=mpg['mpg'],palette='pastel')
fig=ax.get_figure()
fig.savefig('q6_plot.png')
# According to the boxplot, cars from the USA are the least fuel efficient on average. 


# Question 7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
plt.figure()
sns.set()
x=mpg['displacement']
y=mpg['mpg']
ax=sns.scatterplot(x,y,hue=mpg['origin'])
fig=ax.get_figure()
fig.savefig('q7_plot.png')
