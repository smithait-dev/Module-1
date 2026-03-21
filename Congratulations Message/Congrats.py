name = input("What is your name? ")
medal = input("Did you get a gold medal? Yes or no? ").lower()

if medal == "yes":
    message = "congratulations"
    uppercaseword = message.upper()
    print(uppercaseword, name)
else:
    print("Keep trying, you'll get it next time!")