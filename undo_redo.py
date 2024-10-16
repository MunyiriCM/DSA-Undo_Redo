hapaNames=[]
redo_stack=[]

for i in range (4):
    dsaName=input(f"Enter the names you want {i+1}: ")
    



    if dsaName.lower()== "z":
        if hapaNames:
            removed=hapaNames.pop() #remove the last item
            redo_stack.append(removed)
            print(f"last entry {removed} removed.")
        else:
            print(hapaNames)


    elif dsaName.lower()=="w":
        if redo_stack:
            added=redo_stack.pop()
            hapaNames.append(added)
            print(f"{added} has been added")
        else:
            print (hapaNames)

    else:
        hapaNames.append(dsaName)
        redo_stack.clear()

print("Final data entered: ", hapaNames)