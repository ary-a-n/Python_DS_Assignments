'''Write a program that takes an integer as
 an input and generates its binary equivalent'''

decimal = int(input("Enter a decimal number: "))
# Normal method
temp = decimal
binary = ""
while temp > 0:
    remainder = temp % 2
    binary = str(remainder) + binary
    temp = temp // 2

print("Binary number is ", binary, " for ", decimal)

#By recursion
def dectobin(decimal):
    if(decimal > 0):
        dectobin((int)(decimal/2))
        print(decimal%2, end='')  
        
dectobin(decimal)