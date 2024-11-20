import bcrypt

password = "password123"
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

if bcrypt.checkpw(input("Enter password: ").encode('utf-8'), hashed):
    print("Login successful!")
