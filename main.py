print("Welcome to the food delivery service   !")
# Get user details
name=input("What's your name: ")
age=input("Hello "+name+"  How old are you: ")

#Give time for delivery
print("Choose time:")
print("1: 12:00 PM")
print("2: 3:00 PM")
print("3: 6:00 PM")
def choose_time():
    choice = input("Enter 1, 2, or 3: ")
    return 
    if choice in ("1","2","3"):
        print("Time selected Successful!")
    else:
        print ("Synatax Error")
time_choice = choose_time()
# Order process
order_list = []
total = 0.0


menu = {
    1: ("Big Burger", 7.99),
    2: ("Chicken Sandwich", 6.49),
    3: ("Fries", 2.99),
    4: ("Soda", 1.49),
    5: ("Ice Cream", 3.49)
}
for key, (item, price) in menu.items():
    print(f"{key}. {item} - ${price:.2f}")

while True:
    choice = int(input("Enter the number of the item you'd like to order: "))
    choice = input("Enter the number of the item you'd like to order (0 to finish): ")
    if choice == ("0"):
        break
    elif choice.isdigit() and int(choice) in menu:
        item_name, item_price = menu[int(choice)]
        order_list.append(item_name)
        total+= item_price
        print(item_name, "added")
    else:
        print("Invalid choice. Please try again.")

#Pickup method
print("Would you like your order to be:")
print("1. Delivered")
print("2. Picked up")

method = input("Enter 1 or 2: ")

if method == "1":
    delivery_method = ("Delivery")
    location= input ('Give your location for Drop off: ')
else:
    delivery_method = ("Pickup")
    location=("in resturant")

# Summary
print("Order Summary:")
print("Name:", name)
print("Age:", age)
print("Delivery Time Option:", time_choice)
print("Order Method:", f"{delivery_method} ({location})")
print("Order Method:", delivery_method+location)
print("Items Ordered:", ",".join(order_list))
print("Total: $", round(total, 2))
print("Thank you for ordering!")
