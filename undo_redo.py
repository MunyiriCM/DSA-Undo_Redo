#initialize an empty list to store the inputs
hapaNames=[]
redo_stack=[]

#loop to get 4 inputs from the user
for i in range (4):
    dsaName=input(f"Enter the names you want {i+1}: ")
    



    if dsaName.lower()== "z":
        #undo functionality
        if hapaNames:
            removed=hapaNames.pop() #remove the last item
            redo_stack.append(removed) #store it in the redo stack
            print(f"last entry {removed} removed.")
        else:
            print(hapaNames)


    elif dsaName.lower()=="w":
        #redo functionality
        if redo_stack:
            added=redo_stack.pop()#restore the last undone item
            hapaNames.append(added) #add it back to the hapaNames list
            print(f"{added} has been added")
        else:
            print (hapaNames)

    else:
        hapaNames.append(dsaName) #Append the input to the list
        redo_stack.clear() #clear the redo stack since we have new input 

print("Final data entered: ", hapaNames)