print("Welcome to the food divery service   !")
# Get user details
name=input("What's your name: ")
age=input("Hello "+name+"  How old are you: ")

#Give time fo
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
time_choice = choose_time()

# Order process
menu = {
    1: ("Big Burger", 7.99),
    2: ("Chicken Sandwich", 6.49),
    3: ("Fries", 2.99),
    4: ("Soda", 1.49),
    5: ("Ice Cream", 3.49)
}
while True:
choice = int(input("Enter the number of the item you'd like to order: "))
if choice == "0":
        break
    elif choice == "1":
        order_list.append("Big Burger")
        total += 7.99
    elif choice == "2":
        order_list.append("Chicken Sandwich")
        total += 6.49
    elif choice == "3":
        order_list.append("Fries")
        total += 2.99
    elif choice == "4":
        order_list.append("Soda")
        total += 1.49
    elif choice == "5":
        order_list.append("Ice Cream")
        total += 3.49
    else:
        print("Invalid choice. Please try again.")

#Pickup method
print("Would you like your order to be:")
print("1. Delivered")
print("2. Picked up")

method = input("Enter 1 or 2: ")

if method == "1":
    delivery_method = "Delivery"
else:
    delivery_method = "Pickup"
# Summary

