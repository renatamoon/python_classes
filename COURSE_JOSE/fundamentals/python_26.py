# IF STATEMENTS

friend = "Rolf"
# user_name = input("Enter your name: ")

# that's the condition to the code to be executed
"""
if user_name == friend:
    print("Hello, Friend!")
else:
    print("Hello Stranger!") """

print("=-"*20)

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")


if user_name in friends:
    print("YOU ARE A FRIEND OF MINE")
elif user_name in family:
    print("You are a family member!")
else:
    print("I DON'T KNOW WHO YOU ARE!")
