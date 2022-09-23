class MyClass():
    a = 10
    b = 20
    x = a + b
    
mc_instance = MyClass()
mc_instance.x

#slide 11
class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = a + b
        
mc_instance = MyClass(10, 20)
mc_instance.x

mc_instance_2 = MyClass(20, 20)
mc_instance_2.x

#slide 19
class HouseValues():
    def __init__(self, num_bedrooms, num_baths, sqft):
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths
        self.sqft = sqft
    
    def estimate_value(self):
        #add 10% per num of bedrooms over 1
        bedroom_mod = ((self.num_bedrooms - 1) * 0.1) + 1
        
        #add 5% per num of baths over 1
        bath_mod = ((self.num_baths - 1) * 0.05) + 1
        
        self.value = (self.sqft * 400) * bedroom_mod * bath_mod
        print(f'I estimate this house will be worth ${round(self.value, 2)}')
        
house1 = HouseValues(2, 2, 950)
house2 = HouseValues(1, 1, 700)
house1.estimate_value()
house2.estimate_value()

#slide 23
from numpy import random

class HouseValues():
    def __init__(self, num_bedrooms, num_baths, sqft):
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths
        self.sqft = sqft
    
    def pick_a_neighborhood(self):
        value = random.normal(1, 0.1)
        if value > 1.2:
            print('Whoa, you got an expensive neighborhood!')
        elif value > 1:
            print('Fairly pricy neighborhood.')
        elif value < 1:
            print('Maybe not the nicest neighborhood.')
        return value
        
    def estimate_value(self):
        #add 10% per num of bedrooms over 1
        bedroom_mod = ((self.num_bedrooms - 1) * 0.1) + 1
        
        #add 5% per num of baths over 1
        bath_mod = ((self.num_baths - 1) * 0.05) + 1
        
        n_mod = self.pick_a_neighborhood()
        
        self.value = (self.sqft * 400) * bedroom_mod * bath_mod * n_mod
        print(f'I estimate this house will be worth ${round(self.value, 2)}')
        
house1 = HouseValues(2, 2, 950)
house2 = HouseValues(1, 1, 700)
house1.estimate_value()
house2.estimate_value()

