# PPHA 30535
# Spring 2021
# Homework 3

# YOUR NAME HERE
# Chenhui Zhang

# YOUR CANVAS NAME: Chenhui Zhang
# YOUR GITHUB USER NAME: Chenhui-Zhang

# Due date: Sunday April 24th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Begin with the class below and do the following:
#   a) Modify the what_to_watch method so that it takes an optional keyword
#       argument that allows the user to narrow down the random selection by
#       category (e.g. select only from movies with category 'action'), but
#       defaults to the entire list of titles as it does now.
#   b) The what_to_watch method currently raises a ValueError if you use it
#       before entering any movies. Modify it using try/except so that it tells
#       the user what they did wrong instead of raising an error.
#   c) Create a new class called InteractiveMovieDataBase that inherits MovieDataBase.
#   d) Override the add_movie method in your new class so that if it is called
#       without arguments, it instead asks for user input to add a title/year/
#       category/stars, but if it is called with arguments it behaves as before
#   e) Add some appropriate error checking to InteractiveMovieDatabase on the user 
#       input, so that they can't enter something that makes no sense (e.g. title=None
#       or year='dog')
#   f) Add a new method to InteractiveMovieDataBase named movie_rankings, which
#       returns a list of all the titles in the database currently, ordered
#       highest ranking (by stars) to lowest
#
# NOTE: Your final submission should have only TWO classes: one (modified)
#       MovieDataBase, and the new InteractiveMovieDataBase

from numpy import random

class MovieDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}
    def add_movie(self,title,year,category,stars):
        self.titles.append(title)
        self.movies[title] = {'year':year, 'category':category, 'stars':stars}
        print(f'{title} ({year}) added to the database.')
    def what_to_watch(self,cat=None):
        try:
            print(self.titles[0])
        except:
            print("No movies yet. Add movies to get started.") 
        choice = random.choice(self.titles)
        movie = self.movies[choice]
        if cat is None:
            print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['category']}, and was given {movie['stars']} stars.")
        else:            
            while movie['category']!=cat:
                choice = random.choice(self.titles);
                movie = self.movies[choice];
            print(f"Your movie today is {choice} ({movie['year']}), which is a {movie['category']}, and was given {movie['stars']} stars.")

#Create instances for the class
test=MovieDataBase()
test.add_movie("Title_1","1998","Romantic","1")
test.add_movie("Title_2","1999","Action","2")
test.add_movie("Title_3","2000","Action","3")
test.add_movie("Title_4","2001","Romantic","4")
test.add_movie("Title_5","2002","Humorous","5")
test.add_movie("Title_6","2003","Documentary","6")
test.add_movie("Title_7","2004","Humorous","7")


#Question a
#Examples to test question a
test.what_to_watch("Action")
test.what_to_watch("Romantic")
test.what_to_watch("Humorous")
test.what_to_watch()

#Question b
#Added the following code as try/except
#try:
#    print(self.titles[0])
#except:
#    print("No movies yet. Add movies to get started.") 

#Question c
#Reference: https://www.w3schools.com/python/python_inheritance.asp

class InteractiveMovieDataBase(MovieDataBase):
    def __init__(self):
        super().__init__()
    def add_movie(self,title=None,year=None,category=None,stars=None):
        if title is None:
            title=input('Please input the title:')
            while len(title)==0:
                title=input('Please do not enter empty values. Please input the title again:')
            year=input('Please input the year:')
            while year.isdigit()==False:
                year=input('Please input numbers. Please input the year again:')
            category=input('Please input the category:')
            while category.isdigit()==True:
                category=input('Please do not input numbers. Please input the category again:')
            stars=input('Please input the stars:')
            while stars.isdigit()==False:
                stars=input('Please input numbers. Please input stars again:')
            self.titles.append(title)
            self.movies[title] = {'year':year, 'category':category, 'stars':stars}
            print(f'{title} ({year}) added to the database.')
        else:
            MovieDataBase.add_movie(self, title, year, category, stars)       
    def movie_rankings(self):
        stars_list=[]
        title_list=[]
        combined_dict={}
        for item in self.titles:
            stars_list.append(self.movies[item]['stars'])
            title_list.append(item)
        combined_dict=dict(zip(title_list,stars_list))
        a=print(sorted(combined_dict.items(),key=lambda item:item[1],reverse=True))
        return a
    
    

#Question d
#Create an instance for class InteractiveMovieDataBase
test_int=InteractiveMovieDataBase()
#Add movies to InteractiveMovieDatabase
test_int.add_movie("Title_1","1998","Romantic","1")
test_int.add_movie("Title_2","1999","Action","2")
test_int.add_movie("Title_3","2000","Action","3")
test_int.add_movie("Title_4","2001","Romantic","4")
test_int.add_movie("Title_5","2002","Humorous","5")
test_int.add_movie("Title_6","2003","Documentary","6")
test_int.add_movie("Title_7","2004","Humorous","7")

test_int.add_movie()


#Question e
#Added error checking for:
#Title： No empty value
#Year: Must be numbers
#Category: Cannot be numbers
#Stars: Must be numbers

#Question f
#Reference: https://blog.csdn.net/qq_33567641/article/details/80946035
test_int.movie_rankings()
