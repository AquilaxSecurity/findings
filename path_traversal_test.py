import os

def vulnerable_file_read(user_input):
    # Vulnerable to Path Traversal
    with open("/var/www/html/" + user_input, 'r') as f:
        return f.read()
