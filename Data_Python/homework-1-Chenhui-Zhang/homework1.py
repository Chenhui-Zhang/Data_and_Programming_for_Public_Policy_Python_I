# PPHA 30535
# Spring 2021
# Homework 1

# YOUR CANVAS NAME Chenhui Zhang
# YOUR GITHUB USER NAME Chenhui-Zhang

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

my_list=['a','b','c','d','e']
for item in my_list:
    print('The value at '+str(my_list.index(item))+' is',item)


# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

the_input=input('Enter the word you want to test:')
def is_palindrome(the_input):
    the_letters=''
    for i in the_input:
        if i.isalpha():
            the_letters=''.join([the_letters,i])
    lower_letters=the_letters.lower()
    if (lower_letters==lower_letters[::-1]):
        print('This is a palindrome')
    else:
        print('This is not a palindrome')
is_palindrome(the_input) 
is_palindrome('radar')
is_palindrome('A man, a plan, a canal, Panama!')
is_palindrome('Apple')
is_palindrome("This isn't a palindrome")

# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
print('I have carrot, kale, radish, pepper')
while 1:
    choice = input('Please pick a vegetable I have available: ')
    if choice in available_vegetables:
        print('Yes! You can have the',choice)
        break
    else:
        print('Invalid choice. Please try again')
    continue

# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".

input_list=input('Please input your list of strings(separate by space)').split()
new_list=[item.lower() for item in input_list if (item[0]=='a'or item[0]=='b')]
print(new_list)


# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]

start_list = [3, 5, 7, 9, 11, 13]
target_list=[2*i for i in list(reversed(start_list))]
print(target_list)

# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']

dict_names={short_names[i]:long_names[i] for i in range(len(short_names))}
print(dict_names)
