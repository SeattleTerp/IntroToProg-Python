# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RKramer,5.10.2021,Added display, add and delete tasks
# RKramer,5.11.2021,Added save and exit tasks
# RKramer,5.11.2021,Removed amend file option
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# File to List
objFile = open(objFile, "r")
for line in objFile:
    lstRow = line.split(",") # Returns a list!
    dicRow = {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("The current ToDo List items are:")
        for objRow in lstTable:
            print(objRow["Task"] + " | " + objRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        while(True):
            strTask = str(input("Task: ")).strip()
            strPriority = str(input("Priority: ")).strip()
            lstTable.append({"Task": strTask, "Priority": strPriority})
            strChoice = input("Exit?('y/n'):")
            if strChoice.lower() == 'y':
                break
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        while(True):
            strItem = input("Task to Remove: ")
            for row in lstTable:
                if row["Task"].lower() ==strItem.lower():
                    lstTable.remove(row)
                    print("row removed")
                else:
                    print("row not found")
            strChoice = input("Exit?('y/n')")
            if strChoice.lower() == 'y':
                break
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", 'w')
        # Use for loop to add list table, row by row
        for dicRow in lstTable:
            # Write in the row column by column then start new line
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        # Close file
        objFile.close()
        # Exit while loop and end program
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # Exit the program