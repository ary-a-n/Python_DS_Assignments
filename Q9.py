'''Write a program in python that takes a string as input to setup a password. Your entered 
password must meet the following requirements:
The password must be at least five characters long.
It must contain the symbol “&”.
It must contain at least one uppercase and one lowercase letter.'''

passw = input("Enter your password: ")

capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small="abcdefghijklmnopqrstuvwxyz"
specialchar="&"

lower,upper,sp = 0,0,0
if (len(passw) >= 5):
    for i in passw:

        if (i in small):
            lower+=1            

        if (i in capital):
            upper+=1           

        if(i in specialchar):
            sp+=1       

if (lower>=1 and upper>=1 and sp>=1):
    print("Valid Password")
else:
    print("Invalid Password")
