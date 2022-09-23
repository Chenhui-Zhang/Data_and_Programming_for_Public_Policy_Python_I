#slide 2
val1 = True
val2 = 10 < 100

print(val1)
print(val2)

#slide 4
my_list = ['a', 'b', 'c', 'd']
val1 = 'a' in my_list
val2 = 'z' not in my_list

print(val1)
print(val2)

#slide 5
my_string = 'Hello world!'
val1 = my_string.startswith('H')
val2 = not my_string.isnumeric()

print(val1)
print(val2)

#slide 6
x = 10
y = 100
z = 'No'
val1 = (x > y) or (x == y and y != 101 and (y+1 == 101 or z == 'No'))
print(val1)

#slide 10
x = 10

if x == 11:
    print('This number is big.')
elif x > 100:
    print('Whoa, huge number.')
elif x == 0:
    print('Basically no number.')
else:
    print('What happened?')
    
#slide 16
my_list = ['a', 'b', 'c', 'd', 'e']

for letter in my_list:
    print('The letter is:', letter)
    
for i in range(5):
    print('In the loop.')
print('Not in the loop')

#slide 21
my_list = ['a', 'b', 'c', 'd', 'e']
for letter in my_list:
    if letter == 'c':
        print('I see the c.')
    else:
        print('Not it...')
        
my_list = ['a', 'b', 'c', 'd', 'e']
for letter in my_list:
    if letter == 'c':
        print('I see the c.')
        break
    else:
        print('Not it...')
        
my_list = ['a', 'b', 'c', 'd', 'e']
for letter in my_list:
    if letter == 'c':
        continue
    else:
        print('I see the', letter)
    print('Done with that iteration...')
print('Where did the "c" go??')

#slide 25
x = 0
while x < 5:
    print('x is', x)
    x += 1
    
#slide 26
letters = ['a', 'b', 'c', 'd', 'e']

mapped = [l.upper() for l in letters]
print(mapped)

filtered = [l for l in letters if l != 'c']
print(filtered)

mapped_and_filtered = [l.upper() for l in letters if l != 'c']
print(mapped_and_filtered)

#slide 30
my_dict = {'a':100, 'b':200, 'c':300, 'd':400}

for key in my_dict.keys():
    print('First key:', key)
    
for val in my_dict.values():
    print('First value:', val) 
    
x, y= [10, 20]
print(x)
print(y)

for key, val in my_dict.items():
    print('First key:', key)
    print('First value:', val)
    
list(my_dict.items())

#slide 34
my_dict = {'a':100, 'b':200, 'c':300, 'd':400}

new_dict = {key:val*2 for key, val in my_dict.items()}
print(new_dict)

start_list = ['a', 'b', 'c', 'd', 'e']
new_dict = {key.upper():None for key in start_list}
print(new_dict)

