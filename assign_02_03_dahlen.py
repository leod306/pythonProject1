# Leo Dahlen
#CBIS 4210
#assignment 2.3
# 9/3/2024

#create an inventory management system that allows the user to add products, remove products,
# check stock, and list all products

# Global dictionary to store products
products = {}

def add_product():
    """
    Adds a new product to the inventory. If the product already exists, updates the stock.
    """
    name = input("Enter product name: ")
    quantity = int(input("Enter product quantity: "))
    price_per_unit = float(input("Enter price per unit: "))

    # Check if the product already exists in the inventory
    if name in products:
        print(f"{name} already exists in the inventory. Updating stock instead.")
        products[name]['quantity'] += quantity  # Update stock if product exists
    else:
        # Add new product as a dictionary with name, quantity, and price per unit
        products[name] = {
            'name': name,
            'quantity': quantity,
            'price_per_unit': price_per_unit
        }
        print(f"Added {name} to the inventory.")

def remove_product():
    """
    Removes a product from the inventory if it exists.
    """
    name = input("Enter product name to remove: ")

    # Check if the product exists, then remove it
    if name in products:
        del products[name]
        print(f"Removed {name} from the inventory.")
    else:
        print(f"{name} does not exist in the inventory.")

def check_stock():
    """
    Checks the stock level of a product. If the product doesn't exist, it notifies the user.
    """
    name = input("Enter product name to check stock: ")

    # Check if the product exists in the inventory
    if name in products:
        stock = products[name]['quantity']
        print(f"{name} has {stock} units in stock.")
    else:
        print(f"{name} is not found in the inventory.")

def list_products():
    """
    Lists all products in the inventory with their details.
    """
    if products:
        print("Inventory List:")
        # Loop through each product and print its details
        for product in products.values():
            print(f"Product: {product['name']} | Price: ${product['price_per_unit']:.2f} | Stock: {product['quantity']}")
    else:
        print("No products in the inventory.")

def main():
    """
    Main function to handle the menu-driven inventory management system.
    """
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

        # Call the appropriate function based on user choice
        if choice == '1':
            add_product()  # Add a new product
        elif choice == '2':
            remove_product()  # Remove an existing product
        elif choice == '3':
            check_stock()  # Check the stock of a product
        elif choice == '4':
            list_products()  # List all products in the inventory
        elif choice == '5':
            print("Exiting the inventory management system.")
            break  # Exit the loop to end the program
        else:
            print("Invalid choice. Please choose again.")  # Handle invalid input

# Entry point of the program
if __name__ == "__main__":
    main()

