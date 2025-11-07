print("Welcome to the food divery service   !")
# Get user details
name=input("What's your name: ")
age=input("Hello "+name+"  How old are you: ")
def choose_time():
    print("Choose time:")
    print("1: 12:00 PM")
    print("2: 3:00 PM")
    print("3: 6:00 PM")
choice = input("Enter 1, 2, or 3: ")


if choice == ("1","2","3"):
        print("Time selected Successful!")
else:
    print ("Synatax Error")
return choice
menu = {
    1: ("Big Burger", 7.99),
    2: ("Chicken Sandwich", 6.49),
    3: ("Fries", 2.99),
    4: ("Soda", 1.49),
    5: ("Ice Cream", 3.49)
}
while True:
choice = int(input("Enter the number of the item you'd like to order: "))


print("Would you like your order to be:")
print("1. Delivered")
print("2. Picked up")

method = input("Enter 1 or 2: ")

