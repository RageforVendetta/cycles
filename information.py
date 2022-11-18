for num in range(5):
    print(num)
for num in range(5,10): #int 1 start int 2 final
    print(num)
for num in range(2,15,3): #Slice int 3 step
    print(num)
for i in range(3):
    for j in range(3):
        print(i,j) # purvo se izvurshva purviq inside cicle
# 0 , 0 , 0 , 1 , 0 , 2 > 1,0 1,1 ,1,2
for i in range(1,11):
    if i == 4:
        continue
    print(i) # continue propuska obuznachenieto
for i in range(1,11):
    if i == 5:
        break
    print(i) # break priklyuchva na obuznachenieto
#TODO: 421421
#FIXME: 42315215
# Infinite loop game
import random
hidden_number = random.randint(0,10)
while True:
    num = int(input("Enter a number\n"))
    if num == hidden_number:
        print("You win")
        break
    else:
        print("Try Again")
print("Thank you for playing")

i = 1
while i<=10:
    print(i)
    i +=1

i = 0
while i < 2:
    j = 0
    while j <3:
        print(i,j)
        j +=1
    i += 1