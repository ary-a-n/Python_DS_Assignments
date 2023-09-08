'''Write a program that inputs a string and print following information about that string:
Number of alphabets
Number of digits
Number of symbols
Number of uppercase alphabets
Number of lowercase alphabets'''


str1 = input()
list1 = []
digi, symb, ualpha, lalpha = 0, 0, 0, 0

for i in str1:
    list1.append(ord(i))

for j in list1:
    if (65 <= j <= 90):
        ualpha += 1
    elif (97 <= j <= 122):
        lalpha += 1
    elif (48 <= j <= 57):
        digi += 1
    else:  # including space character
        symb += 1

alpha = ualpha+lalpha
print("Total alphabets: ", alpha)
print("Total lower_alphabets: ", lalpha)
print("Total upper_alphabets: ", ualpha)
print("Total digits: ", digi)
print("Total symbols: ", symb)