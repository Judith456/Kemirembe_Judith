inventory = [
    {"id" : 1, "name" : "apple", "quantity" : 100},
    {"id" : 2, "name" : "oranges", "quantity" : 50},
    {"id" : 3, "name" : "lemons", "quantity" : 30},
    {"id" : 4, "name" : "mangoes", "quantity" : 70},
    {"id" : 5, "name" : "coffee", "quantity" : 50}
]

def display_inventory():
    print("\nCurrent Inventory:")
    print("-" * 40)
    
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']}   | Quantity: {item['quantity']}")
    
    print("-" * 40)
    

def update_stock():
    try:
        item_id = int(input("Enter the ID of the item to update: "))
        new_quantity = int(input("Enter the new quantity: "))
        print("\n")
        for item in inventory:
            if item['id'] == item_id:
                item['quantity'] = new_quantity
                print(f"{item['name']} quantity updated to {new_quantity}.")
                break
        else:
            print("Item ID not found.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Main menu loop
while True:
    print("\nInventory Management Menu")
    print("1. View Inventory")
    print("2. Update Inventory")
    print("3. Exit")
    print("\n")
    choice = input("Enter your choice (1-3): ")
    print("\n")

    if choice == '1':
        display_inventory()
    elif choice == '2':
        display_inventory()
        update_stock()
    elif choice == '3':
        print("Inventory Management System Exited.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


#https://github.com/Judith456/Kemirembe_Judith.git

