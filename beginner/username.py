#username should not be more than 12 characters
#username must not contain spaces 
#username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username must not contain spaces")
elif not username.isalpha():
    print("Your username must not contain digits")
else:
    print(f"Welcome {username}")