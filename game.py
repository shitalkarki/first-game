import random


print("welcome to the game")
random_number=random.randrange(5)
#print(x)
#user_input_number=int(input('please enter your guess:'))
#print(y)
chance=3
i=1

while(i<=chance):
    y=int(input('please enter your guess:'))


    if(x==y):
        print('win')
        break
    else:
    
        print('you lose')   
        i=i+1 
print('computer guess is' ,x)
