def insecure_function():
    user_input = input("Enter your password: ")
    exec(user_input)  # Insecure use of exec()
