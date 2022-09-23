# PPHA 30535
# Spring 2022
# Homework 2

# YOUR CANVAS NAME: Chenhui Zhang
# YOUR GITHUB USER NAME: Chenhui-Zhang

# Due date: Sunday April 17th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]
def arg_sum(start_list):
    output_list=[]
    for i in range(len(start_list)):
        a=start_list[i][0]
        b=start_list[i][1]
        sumab=a+b
        if sumab>10:
            output_list.append('big')
        elif sumab==10:
            output_list.append('just right')
        elif sumab<10:
            output_list.append('small')
    return output_list
end_result=arg_sum(start_list)        
#Reference: https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size 


# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 30
    return a + b
x = my_func()

def my_second_func(a):
    b = 30
    return a+b
y = my_second_func(10)
#The original function's purpose is to add 30 to a
#The new function can realize the same purpose to any value of a without changing global variables


# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.
#import random
#from numpy import random

import random
def gen_pass(pass_length,special_chars=True,if_numbers=True):
    upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    spec_char=['!','@','#','$','%','^','&','*']
    number_list=['0','1','2','3','4','5','6','7','8','9']
    if pass_length<8 or pass_length>16:
        print('Error! The length of the password should be between 8 and 16. Try again.')
        return
    if pass_length>=8 or pass_length<=16:
        if special_chars==True and if_numbers==True:
            pass_set=upper_case+lower_case+spec_char+number_list
        if special_chars==True and if_numbers==False:
            pass_set=upper_case+lower_case+spec_char
        if special_chars==False and if_numbers==True:
            pass_set=upper_case+lower_case+number_list
        if special_chars==False and if_numbers==False:
            pass_set=upper_case+lower_case
        password_list=random.sample(pass_set,pass_length)
        password=''.join(password_list)
    return(password)   
 
test=gen_pass(10,False,True)
#Reference: https://www.geeksforgeeks.org/default-arguments-in-python/
#https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output. 
     
  
  
# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 1, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes any number of these instances and 
# returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])


class Covid_Vac():
    def __init__(self, person_name, vac_type, no_doses, ever_covid):
        self.person_name=person_name
        self.vac_type=vac_type
        self.no_doses=no_doses
        self.ever_covid=ever_covid
    def get_record(self):
        if self.ever_covid==True:
           output_covid='ever'
        elif self.ever_covid==False:
           output_covid='never'
        print('%s has %s doses of %s and has %s had COVID.'%(self.person_name,self.no_doses,self.vac_type,output_covid))
    def same_shot(self,instance_who):
        vactype_a=self.vac_type
        vactype_b=instance_who.vac_type
        if vactype_a==vactype_b:
            print('They have the same kind of vaccines.')
        elif vactype_a!=vactype_b:
            print('They have different kinds of vaccines.')

def all_data(n):
    data_list=[]
    data_list.append([instance_Aaron.person_name,instance_Aaron.vac_type,instance_Aaron.no_doses,instance_Aaron.ever_covid])
    data_list.append([instance_Alison.person_name,instance_Alison.vac_type,instance_Alison.no_doses,instance_Alison.ever_covid])
    data_list.append([instance_Ashu.person_name,instance_Ashu.vac_type,instance_Ashu.no_doses,instance_Ashu.ever_covid])
    data_list.append([instance_Asma.person_name,instance_Asma.vac_type,instance_Asma.no_doses,instance_Asma.ever_covid])
    return data_list[0:n]
    
        
#Create instance for all four people
instance_Aaron=Covid_Vac('Aaron', 'Moderna', 1, False)
instance_Alison=Covid_Vac('Alison', 'none', 0, True)
instance_Ashu=Covid_Vac('Ashu', 'Pfizer', 2, False)
instance_Asma=Covid_Vac('Asma', 'Pfizer', 1, True)

#Print out one sentence summary
instance_Aaron.get_record()
instance_Alison.get_record()
instance_Ashu.get_record()
instance_Asma.get_record()

#Compare whether they have same vaccines
instance_Aaron.same_shot(instance_Ashu)
instance_Ashu.same_shot(instance_Asma)
instance_Asma.same_shot(instance_Aaron)

#Return a list of any number of the instances
all_data(1)
all_data(2)
all_data(3)
all_data(4)

#Reference: https://pynative.com/python-class-method/#:~:text=To%20make%20a%20method%20as,method%20as%20a%20class%20method.
#https://www.tutorialspoint.com/difference-between-method-and-function-in-python

