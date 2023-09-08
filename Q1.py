'''Write a program that asks the user to input marks of three subjects and computes the 
average for it. The average should then be compared 40, and the output display should 
be Pass/Fail depending upon whether the marks are greater/lesser than 40.'''

num1 = int(input())
num2 = int(input())
num3 = int(input())

avg = round((num1+num2+num3)/3,2) #using round to round-off
print("Average is: ",avg)
if(avg>=40):
    print("Pass")
else:
    print("Fail")