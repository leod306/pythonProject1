# Leo Dahlen
#CBIS 4210
#assignment 1.1
#8/30/2024


# calculate the two numbers and sum them together
def calculate_sum(num1, num2):
    return num1 + num2

# get twp inputs from a user and sum them together
def main():

    # get the first number from the user
    number1 = int(input("Enter a number: "))
    # get the second number from the user
    number2 = int(input("Enter another number: "))

    # Sum the two numbers together
    sum = calculate_sum(number1, number2)


    # print the sum
    print("The sum of the two numbers is ", sum)

#call the main function
main()

