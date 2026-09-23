#Jason Luis
#Professor Ghaforyfard
#April 20, 2024
#Create a menu to allow the user to add, insert, remove, find the maximum, the minimum, and sort the list in decending order (Larger to a smaller value.) Declare your list as a list of strings. EX: studentFullName=["Mike Navarro", "Miguel Saba", "Maria Rami"]


#List 
from tkinter.tix import InputOnly


studentFullName = ["Mike Navarro" , "Miguel Saba", "Maria Rami"] 

print("\n\n", studentFullName)

print("\n====================================================")

#List Menu Inputs 

option = 1

while option != 8:

    option = int(input("\n1- Add an item to the list\n\n2- Remove an item from the list ==> ask for the name instead of the index\n\n3- Insert an item into the list\n\n4- Find the Maximum\n\n5- Find the Minimum\n\n6- Sort the list on decending order\n\n7- Display the list\n\n8-Quit the Program\n\nPlease enter your option: ")) 
        
    if option == 1:
        print("\nYou have selected Option #1")

        itemVal = input("\nAdd an item to the list: ")

        studentFullName.insert(-1, itemVal)

        print("\nNew list: ", studentFullName) 
        continue


    elif option == 2: 
        print("\nYou have selected Option #2") 

        itemVal = input("\nRemove an item from the list ==> ask for the name instead of the index: ") 

        studentFullName.remove(itemVal)

        print("\nNew list: ", studentFullName) 
        continue
        

    elif option == 3: 
        print("\nYou have selected Option #3")

        itemVal = input("\nAdd an item to the list: ")

        studentFullName.insert(-1, itemVal)

        print("\nNew list: ", studentFullName) 
        continue
       
    
    elif option == 4: 
        print("\nYou have selected Option #4")

        print("\nFind the Maximum")

        studentFullName[0]

        print("\nNew list: ", studentFullName[0])
        continue

    elif option == 5: 
         print("\nYou have selected Option #5")

         print("\nFind the Minimum")

         studentFullName[2]

         print("\nNew list: ", studentFullName[2]) 
         continue

         

    elif option == 6:
         print("\nYou have selected Option #6")

         print("\nSort the list on decending order")

         studentFullName.sort()

         print("\nNew list: ", studentFullName)
         continue

    elif option == 7:
         print("\nYou have selected option #7")

         print("\nDisplay the list")

         print("\nList: ", studentFullName)
         continue
    elif option == 8:
        break
    else: 
        option = int(input("\n1- Add an item to the list\n\n2- Remove an item from the list ==> ask for the name instead of the index\n\n3- Insert an item into the list\n\n4- Find the Maximum\n\n5- Find the Minimum\n\n6- Sort the list on decending order\n\n7- Display the list\n\n8-Quit the Program\n\nPlease enter your option: ")) 
       
