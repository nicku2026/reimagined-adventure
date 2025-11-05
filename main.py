print("Welcome to the food divery service   !")
name=input("What's your name: ")
age=input("Hello "+name+"  How old are you: ")
def menu():
    print("Choose a time to be pick up:")
    print("1")
    print("2")
    print("3")
chat = menu()
print(chat)
choice = input("Enter 1, 2, or 3: ")
if choice == ("1"):
    print('Goodbye!!')
elif choice == ("2"):
    print('Goodbye!!')
elif choice == ("3"):
    print("Goodbye!!")
else:
    print ("Synatax Error")
menu = {
    1: ("Big Burger", 7.99),
    2: ("Chicken Sandwich", 6.49),
    3: ("Fries", 2.99),
    4: ("Soda", 1.49),
    5: ("Ice Cream", 3.49)
}
choice = int(input("Enter the number of the item you'd like to order: "))


print("Would you like your order to be:")
print("1. Delivered")
print("2. Picked up")

method = input("Enter 1 or 2: ")

