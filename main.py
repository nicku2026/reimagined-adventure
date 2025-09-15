print("Welcome to The Game!")
name=input("What's your name: ")
age=input("Hello "+name+"  How old are you: ")
def menu():
    print("Choose a setting:")
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
