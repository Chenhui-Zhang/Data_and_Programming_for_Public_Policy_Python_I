from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = random.choice(choices)
p2 = random.choice(choices)

class Agent():
    def __init__(self,choice,p2):
        self.choice=choice
        self.p2=p2
        pass
    def compare_it(self,choice):
        if self.choice==self.p2:
            print("This is a tie.")
        elif self.choice=='rock' and self.p2=='paper':
            print("You lose.")
        elif self.choice=='rock' and self.p2=='scissors':
            print("You win. ")
        elif self.choice=='paper' and self.p2=='rock':
            print("You win.")
        elif self.choice=='paper' and self.p2=='scissors':
            print("You lose.")
        elif self.choice=='scissors' and self.p2=='rock':
            print("You lose.")
        elif self.choice=='scissors' and self.p2=='paper':
            print("You win.")
        pass
   
    
test_instance=Agent(p1,p2)    
test_instance.compare_it(p1)

#Try dictionary to tell the comparing logic
        


