import random

class InventoryError(Exception):
    pass

class Item:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def update_quantity(self, quantity: int):
        """Update the quantity of the item."""
        if quantity < 0:
            raise InventoryError("Quantity cannot be negative.")
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the item."""
        return f"Item: {self.name}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, quantity: int):
        """Add a new item to the inventory."""
        if name in self.items:
            raise InventoryError("Item already exists.")
        self.items[name] = Item(name, quantity)

    def view_items(self):
        """Display all items in the inventory."""
        if not self.items:
            print("No items in inventory.")
            return
        for item in self.items.values():
            print(item)

    def update_item(self, name: str, quantity: int):
        """Update the quantity of an item."""
        if name in self.items:
            self.items[name].update_quantity(quantity)
        else:
            raise InventoryError("Item not found.")

    def delete_item(self, name: str):
        """Delete an item from the inventory."""
        if name in self.items:
            del self.items[name]
        else:
            raise InventoryError("Item not found.")

def main():
    inventory = Inventory()

    while True:
        name = input("Enter item name (or 'done' to finish adding in inventory): ")
        if name.lower() == 'exit':
            break
        try:
            quantity = int(input("Enter item quantity: "))
            inventory.add_item(name, quantity)
            print(f"Item '{name}' added successfully.")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
        except InventoryError as e:
            print(f"Error: {e}")

    while True:
        print("\nOptions:")
        print("1. View Items")
        print("2. Update Item Quantity")
        print("3. Delete Item")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            inventory.view_items()
        elif choice == '2':
            name = input("Enter item name to update: ")
            try:
                quantity = int(input("Enter new quantity: "))
                inventory.update_item(name, quantity)
                print(f"Item '{name}' updated successfully.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
            except InventoryError as e:
                print(f"Error: {e}")
        elif choice == '3':
            name = input("Enter item name to delete: ")
            try:
                inventory.delete_item(name)
                print(f"Item '{name}' deleted successfully.")
            except InventoryError as e:
                print(f"Error: {e}")
        elif choice == '4':
            print("Exiting Inventory Management System.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()