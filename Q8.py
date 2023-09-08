'''Write a program to find out longest common subsequence from an input string just 
having the consonants '''


list1=['a','e','i','o','u','A','E','I','O','U']

my_list=input().split()
final_list = []
for i in my_list:
    string=""
    for j in i:
        if(j not in list1):
            string+=j
    final_list.append(string)
mlength=0
string1=""
for i in final_list:
    if(len(i)>mlength):
        mlength=len(i)
        string1=i
print("Longest common subsequence is: ",string1)