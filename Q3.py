'''Write a program with a function that inputs a string and the output has to be a new string 
with first letter of every word capitalized.'''

string = input()
# using inbuilt fuction
print(string.title())

# using ord and char
s = input()
s_split = s.split()

small_a = ord("a")
small_z = ord("z")
cap_a = ord("A")

delta = small_a - cap_a

for z in s_split:
    if small_a <= ord(z[0]) <= small_z:
        l = chr(ord(z[0])-delta)
        new = l + z[1:]
        print(new, end=" ")
    else:
        print(z, end=" ")
