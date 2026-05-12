class Product:
    """Class representing a single item in the warehouse."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Prettifies the output when the object is printed."""
        return f"{self.name:15} | Price: ${self.price:>7.2f} | Qty: {self.quantity:>4}"


class Warehouse:
    """Class managing a collection of Product objects."""

    def __init__(self):
        self.inventory = []

    def add_product(self, name, price, quantity):
        for item in self.inventory:
            if item.name.lower() == name.lower():
                item.quantity += quantity
                print(f"Updated quantity for '{name}'.")
                return

        new_item = Product(name, price, quantity)
        self.inventory.append(new_item)
        print(f"Added '{name}' to the inventory.")

    def remove_product(self, name):
        """Removes a product from the inventory by name."""
        for item in self.inventory:
            if item.name.lower() == name.lower():
                self.inventory.remove(item)
                print(f"Removed '{item.name}' from the inventory.")
                return True
        print(f"Error: Product '{name}' not found.")
        return False

    def show_inventory(self):
        print("\n" + "=" * 45)
        print("CURRENT INVENTORY STATUS")
        print("=" * 45)

        if not self.inventory:
            print("The warehouse is empty.")
        else:
            total_value = 0
            for item in self.inventory:
                print(item)
                total_value += item.price * item.quantity
            print("-" * 45)
            print(f"Total Warehouse Value: ${total_value:.2f}")


def main_menu():
    my_warehouse = Warehouse()

    while True:
        print("\n<<< Warehouse Management System >>>")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Inventory")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            try:
                name = input("Product Name: ")
                price = float(input("Price per unit: "))
                quantity = int(input("Quantity: "))
                my_warehouse.add_product(name, price, quantity)
            except ValueError:
                print("Error: Price and Quantity must be numeric values!")

        elif choice == "2":
            name_to_remove = input("Enter the name of the product to remove: ")
            my_warehouse.remove_product(name_to_remove)

        elif choice == "3":
            my_warehouse.show_inventory()

        elif choice == "4":
            print("Shutting down...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
