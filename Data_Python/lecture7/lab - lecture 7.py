
#1. will the code run, and if so, what will be the data types and values of a and b?
a, b = [10, 11]
#a=10,int, b=11,int

a, b = [10]
#doesn't work

a, b = [10, 11, 12]
#doesn't work

a, *b = [10, 11]
#a is 10, int, b is [11], list

a, *b = [10]
#a is 10, int
#b is [], list

a, *b = [10, 11, 12]
#a is 10, int
#b is [11,12], list

#2. what data type is args and kwargs inside the function, what are the values,
#and how would you use them?

#args is tuple
#kwargs is dictionary
def base_function(*args, **kwargs):
    args_is=args
    kwargs_is=kwargs
    print(args)
    print(kwargs)
    return args_is,kwargs_is

test1=base_function()
test2=base_function(['A', 'B'])
test3=base_function('Hello', 'World', '!')
test4=base_function(answer=True, question='No')
test5=base_function('a', 'b', c='value', d=10)



#3. write a lambda function that is passed into my_func, and performs a valid
#operation on a and b, without editing the contents of my_func at all.

def my_func(a, b, func):
    value = func(a, b)
    return value

func=lambda a,b: (a+b)**2

my_func(7,2,func)
