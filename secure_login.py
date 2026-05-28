
correct_username = "Sakshi"
correct_password = "12345"

print("=== Secure Login System ===")


username = input("Enter Username: ")
password = input("Enter Password: ")


if username == correct_username and password == correct_password:
    print("\nLogin Successful!")
else:
    print("\nInvalid Username or Password!")