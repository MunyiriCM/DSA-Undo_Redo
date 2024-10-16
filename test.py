# Initialize empty lists to store user inputs and redo data
user_data = []
redo_stack = []

# Loop to get input 3 times
for i in range(3):
    data = input(f"Enter data {i+1} (type 'Z' or 'z' to undo, 'Y' or 'y' to redo): ")

    if data.lower() == 'z':
        # Undo functionality
        if user_data:
            removed = user_data.pop()  # Remove the last item
            redo_stack.append(removed)  # Store it in the redo stack
            print(f"Last entry '{removed}' removed.")
        else:
            print("No data to undo.")

    elif data.lower() == 'y':
        # Redo functionality
        if redo_stack:
            restored = redo_stack.pop()  # Restore the last undone item
            user_data.append(restored)   # Add it back to the user_data list
            print(f"Entry '{restored}' restored.")
        else:
            print("No data to redo.")
    
    else:
        user_data.append(data)  # Append the input to the list
        redo_stack.clear()  # Clear redo stack since we have new input

# Print the final list to verify the inputs
print("Final Data entered:", user_data)
