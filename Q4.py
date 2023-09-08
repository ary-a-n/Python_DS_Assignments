'''Write a program for insertion and deletion of elements in a list. On selection of deletion 
option, a submenu should be displayed to ask if the element is to be deleted by value or 
by position or a slice of elements has to be deleted and accordingly the output is 
generated. '''

def insert_element(lst):
    n = int(input("Enter the number of elements you want to enter: "))
    while(n>0):
        value = input("Enter the value to insert: ")
        lst.append(value)
        n-=1

def delete_element(lst):
    print("Select a deletion option:")
    print("1. Delete by value")
    print("2. Delete by position")
    print("3. Delete a slice of elements")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        value_to_delete = input("Enter the value to delete: ")
        if value_to_delete in lst:
            lst.remove(value_to_delete)
            print(f"{value_to_delete} has been deleted from the list.")
        else:
            print(f"{value_to_delete} not found in the list.")

    elif choice == 2:
        position = int(input("Enter the position to delete: "))
        if 0 <= position < len(lst):
            deleted_value = lst.pop(position)
            print(f"Element at position {position} ({deleted_value}) has been deleted.")
        else:
            print("Invalid position. Deletion failed.")

    elif choice == 3:
        start = int(input("Enter the start index for slice deletion: "))
        end = int(input("Enter the end index for slice deletion: "))
        if 0 <= start < len(lst) and 0 <= end < len(lst) and start <= end:
            del lst[start:end + 1] # +1 beacause del removes 1 less
            print(f"Slice from index {start} to {end} has been deleted.")
        else:
            print("Invalid slice indices. Deletion failed.")

    else:
        print("Invalid choice. Please select a valid option.")

def main():
    my_list = []

    while True:
        print("\nList:", my_list)
        print("Menu:")
        print("1. Insert Element")
        print("2. Delete Element")
        print("3. Print list")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            insert_element(my_list)
        elif choice == 2:
            delete_element(my_list)
        elif choice == 3:
            print(my_list)
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
