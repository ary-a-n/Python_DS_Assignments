'''Write a program to input a string of numbers separated by a space “ “. 
Generate a list of numbers from this string and sort the list 
using selection sort. '''


def s_sort(a):
    for i in range(len(a)):
        min_id = i
        for j in range(i+1, len(a)):
            if a[min_id] > a[j]:
                min_id = j
        a[i], a[min_id] = a[min_id], a[i]

def main():
    list1 = input().split()
    numlist = []
    for i in list1:
        numlist.append(int(i))
    print("Original List: ",list1)
    s_sort(numlist)
    print("Sorted list: ",numlist)


if __name__ == "__main__":
    main()
