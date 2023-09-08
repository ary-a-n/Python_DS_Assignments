#Write a program that takes two lists as an input and appends them. The second list could
#either be a single number or a list of numbers.

x = input()
list1 = x.split()
list3 = x.split()
list5 = x.split()
y = input()
list2 = y.split()
list4 = y.split()
list6 = y.split()

#loop approcah
for i in list2:
    list1.append(i)

print(list1)

#addition

print(list3+list4)

#extend function
list5.extend(list6)
print(list5)
