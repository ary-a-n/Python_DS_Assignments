'''Write a program which takes email IDs of n students and stores in a tuple. Two new 
tuples are to be created from it- first one having the user names of the email IDs and the 
second one having the domain names only. The final output should display all three 
tuples'''

n = int(input("Enter the no.of students: "))

listi = []
username = []
domains = []

for i in range(0, n):
    x = input()
    listi.append(x)
    list1 = x.split('@')
    username.append(list1[0])
    domains.append(list1[1])

print(tuple(listi))
print(tuple(username))
print(tuple(domains))
