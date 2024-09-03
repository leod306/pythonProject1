# Leo Dahlen
#CBIS 4210
#assignment 2.3
# 9/3/2024

#create a customer relationship management system that allows the user to add customers,
# add purchases for customers,

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Global dictionary to store customers
customers = {}

def add_customer():
    """
    Adds a new customer to the CRM. If the customer already exists, notifies the user.
    """
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")

    # Check if the customer already exists in the CRM
    if email in customers:
        print(f"Customer with email {email} already exists.")
    else:
        # Add new customer to the customers dictionary
        customers[email] = {
            'name': name,
            'email': email,
            'purchases': []  # Empty list to store purchases for the customer
        }
        print(f"Added customer {name}.")

def add_purchase():
    """
    Adds a purchase for an existing customer. If the customer doesn't exist, notifies the user.
    """
    email = input("Enter customer email: ")
    product = input("Enter product purchased: ")

    # Check if the customer exists in the CRM
    if email in customers:
        customers[email]['purchases'].append(product)  # Add the product to the customer's purchases
        print(f"Added purchase: {product} for {customers[email]['name']}")
        send_follow_up_email(customers[email], product)  # Send follow-up email
    else:
        print(f"No customer found with email {email}. Please add the customer first.")

def send_follow_up_email(customer, product):
    """
    Sends a follow-up email to the customer after a purchase.
    (Simulated email sending function without actual server interaction for simplicity.)
    """
    print(f"Sending follow-up email to {customer['email']} for purchase: {product}")
    print(f"Email: 'Thank you, {customer['name']}, for purchasing {product}.'")

def list_customers():
    """
    Lists all customers in the CRM system and their purchases.
    """
    if customers:
        print("List of customers:")
        for customer in customers.values():
            print(f"{customer['name']} ({customer['email']})")
            if customer['purchases']:
                print("Purchases:")
                for product in customer['purchases']:
                    print(f"- {product}")
            else:
                print("No purchases yet.")
    else:
        print("No customers in the CRM system.")

def main():
    """
    Main function to handle the menu-driven CRM system.
    """
    while True:
        # Display menu options for the CRM
        print("\nCustomer Relationship Management (CRM)")
        print("1. Add Customer")
        print("2. Add Purchase for Customer")
        print("3. List All Customers and Purchases")
        print("4. Exit")

        # Get user input for the desired action
        choice = input("Enter your choice (1-4): ")

        # Call the appropriate function based on user choice
        if choice == '1':
            add_customer()  # Add a new customer
        elif choice == '2':
            add_purchase()  # Add a purchase for an existing customer
        elif choice == '3':
            list_customers()  # List all customers and their purchases
        elif choice == '4':
            print("Exiting CRM system.")
            break  # Exit the loop to end the program
        else:
            print("Invalid choice. Please choose again.")  # Handle invalid input

# Entry point of the program
if __name__ == "__main__":
    main()
