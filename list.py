#creating a empty

names=[]

while True:
    #Display the menu
    print("\n Menu: ")
    print("1. Add a name to the list ")
    print("2. change a name in th list ")
    print("3. delete a name from the list ")
    print("4. views the name in the list ")
    print("5. end the program ")

    #prompt the user to make a choice
    choice=input("Enter your choice(1-5)")
    
    if choice=="1":
        new_name=input("Enter the name to be added to the list:")
        names.append(new_name)
        print("The new name is added to the list")

    elif choice=="2":
        old_name=input("enter the name you want to change")
        if old_name in names:
            new_name=input("Enter the new name to be changed")
            index=names.index(old_name)
            names[index]=new_name
            print("The name is changed in the list")
        else:
            print("this name does not exist in the list")
    elif choice=="3":
        name_delete=input("Enter the name you want  to be deleted")
        if name_delete in names:
            names.remove(name_delete)
            print(" the name is deleted from the list")
        else:
            print("this name does not exist in the list")

    elif choice=="4":
        if names:
            print(names)
        else:
            print(" the list is empty")

    elif choice=="5":

        print("Ending the program, Goodbye!!")
        break

    else:
        print("Invalid Choice")             

            
        