import os

def vulnerable_command(user_input):
    # Vulnerable to Command Injection
    os.system("ping " + user_input)
