# Leo Dahlen
#CBIS 4210
#assignment 2.3
#8/31/2024

#create an inventory management system that allows the user to add products, remove products,
# check stock, and list all products

class Product:
    def __init__(self, name, quantity, price_per_unit):
        """
        Initializes a Product object with a name, quantity, and price per unit.
        """
        self.name = name
        self.quantity = quantity  # Available stock for the product
        self.price_per_unit = price_per_unit  # Price of one unit of the product

    def add_stock(self, amount):
        """
        Adds stock to the product's current quantity.
        """
        self.quantity += amount
        print(f"Added {amount} units to {self.name}. Current stock: {self.quantity}")

    def remove_stock(self, amount):
        """
        Removes stock from the product's current quantity.
        Checks if there is enough stock before removing.
        """
        if amount > self.quantity:
            print(f"Not enough stock to remove {amount} units of {self.name}. Current stock: {self.quantity}")
        else:
            self.quantity -= amount
            print(f"Removed {amount} units from {self.name}. Current stock: {self.quantity}")

    def get_stock(self):
        """
        Returns the current stock level of the product.
        """
        return self.quantity

    def display_product_info(self):
        """
        Displays the product details including name, price per unit, and stock quantity.
        """
        print(f"Product: {self.name} | Price: ${self.price_per_unit:.2f} | Stock: {self.quantity}")


class Inventory:
    def __init__(self):
        """
        Initializes the inventory with an empty dictionary to store products.
        """
        self.products = {}

    def add_product(self, name, quantity, price_per_unit):
        """
        Adds a new product to the inventory. If the product already exists, updates the stock.
        """
        if name in self.products:
            print(f"{name} already exists in the inventory. Updating stock instead.")
            self.products[name].add_stock(quantity)
        else:
            product = Product(name, quantity, price_per_unit)
            self.products[name] = product
            print(f"Added {name} to the inventory.")

    def remove_product(self, name):
        """
        Removes a product from the inventory if it exists.
        """
        if name in self.products:
            del self.products[name]
            print(f"Removed {name} from the inventory.")
        else:
            print(f"{name} does not exist in the inventory.")

    def check_stock(self, name):
        """
        Checks the stock level of a product. If the product doesn't exist, it notifies the user.
        """
        if name in self.products:
            stock = self.products[name].get_stock()
            print(f"{name} has {stock} units in stock.")
        else:
            print(f"{name} is not found in the inventory.")

    def list_products(self):
        """
        Lists all products in the inventory with their details.
        """
        if self.products:
            print("Inventory List:")
            for product in self.products.values():
                product.display_product_info()
        else:
            print("No products in the inventory.")


def main():
    # Create an instance of the inventory
    inventory = Inventory()

    while True:
        # Display the menu options
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Check Stock")
        print("4. List All Products")
        print("5. Exit")

        # Get user input for the action they want to perform
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Get input for new product details
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price_per_unit = float(input("Enter price per unit: "))

            # Add the product to the inventory
            inventory.add_product(name, quantity, price_per_unit)

        elif choice == '2':
            # Get the product name to remove
            name = input("Enter product name to remove: ")
            inventory.remove_product(name)

        elif choice == '3':
            # Get the product name to check stock
            name = input("Enter product name to check stock: ")
            inventory.check_stock(name)

        elif choice == '4':
            # List all products in the inventory
            inventory.list_products()

        elif choice == '5':
            # Exit the program
            print("Exiting the inventory management system.")
            break

        else:
            print("Invalid choice. Please choose again.")


# Run the inventory management system
if __name__ == "__main__":
    main()
