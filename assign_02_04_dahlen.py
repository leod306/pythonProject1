# Leo Dahlen
#CBIS 4210
#assignment 2.3
#8/31/2024

#create a customer relationship management system that allows the user to add customers,
# add purchases for customers,

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Customer:
    def __init__(self, name, email):
        """
        Initializes a Customer object with a name and email address.
        Purchases will be stored in a list.
        """
        self.name = name
        self.email = email
        self.purchases = []  # List of products purchased by the customer

    def add_purchase(self, product):
        """
        Adds a product to the customer's purchase list.
        """
        self.purchases.append(product)

    def list_purchases(self):
        """
        Lists all purchases made by the customer.
        """
        if self.purchases:
            print(f"Purchases by {self.name}:")
            for product in self.purchases:
                print(f"- {product}")
        else:
            print(f"{self.name} has not made any purchases yet.")


class CRM:
    def __init__(self):
        """
        Initializes the CRM system with an empty dictionary to store customers.
        """
        self.customers = {}

    def add_customer(self, name, email):
        """
        Adds a customer to the CRM. If the customer already exists, it notifies the user.
        """
        if email in self.customers:
            print(f"Customer with email {email} already exists.")
        else:
            customer = Customer(name, email)
            self.customers[email] = customer
            print(f"Added customer {name}.")

    def add_purchase(self, email, product):
        """
        Adds a purchase for a customer. If the customer doesn't exist, it prompts the user.
        """
        if email in self.customers:
            customer = self.customers[email]
            customer.add_purchase(product)
            print(f"Added purchase: {product} for {customer.name}")
            self.send_follow_up_email(customer, product)  # Send follow-up email
        else:
            print(f"No customer found with email {email}. Please add the customer first.")

    def send_follow_up_email(self, customer, product):
        """
        Sends a follow-up email to the customer after a purchase.
        """
        # Your email and password (should be stored securely, not in the code)
        sender_email = "youremail@example.com"
        sender_password = "yourpassword"

        # Create the email content
        subject = f"Thank You for Purchasing {product}, {customer.name}!"
        body = (f"Dear {customer.name},\n\n"
                f"Thank you for purchasing {product} from our store. "
                "We hope you enjoy it!\n\n"
                "If you have any questions, feel free to reply to this email.\n"
                "Best regards,\n"
                "Your Company Name")

        # Create a MIMEText object to represent the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = customer.email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail's SMTP server
            server.starttls()  # Start TLS for security
            server.login(sender_email, sender_password)  # Login to your email account
            text = msg.as_string()  # Convert the message to a string
            server.sendmail(sender_email, customer.email, text)  # Send the email
            server.quit()  # Terminate the session
            print(f"Follow-up email sent to {customer.email} for purchase: {product}")
        except Exception as e:
            print(f"Failed to send email to {customer.email}. Error: {e}")

    def list_customers(self):
        """
        Lists all customers in the CRM system.
        """
        if self.customers:
            print("List of customers:")
            for customer in self.customers.values():
                print(f"{customer.name} ({customer.email})")
                customer.list_purchases()
        else:
            print("No customers in the CRM system.")


def main():
    # Create an instance of the CRM system
    crm = CRM()

    while True:
        # Display menu options for the CRM
        print("\nCustomer Relationship Management (CRM)")
        print("1. Add Customer")
        print("2. Add Purchase for Customer")
        print("3. List All Customers and Purchases")
        print("4. Exit")

        # Get user input for the desired action
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Get input for new customer details
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")

            # Add the customer to the CRM
            crm.add_customer(name, email)

        elif choice == '2':
            # Get customer email and purchase details
            email = input("Enter customer email: ")
            product = input("Enter product purchased: ")

            # Add the purchase for the customer
            crm.add_purchase(email, product)

        elif choice == '3':
            # List all customers and their purchases
            crm.list_customers()

        elif choice == '4':
            # Exit the CRM system
            print("Exiting CRM system.")
            break

        else:
            print("Invalid choice. Please choose again.")


# Run the CRM system
if __name__ == "__main__":
    main()