import os

def check_access(path):
    print(f"Checking access for path: {path}")
    print(f"Path exists: {os.path.exists(path)}")
    print(f"Path is readable: {os.access(path, os.R_OK)}")
    print(f"Path is writable: {os.access(path, os.W_OK)}")
    print(f"Path is executable: {os.access(path, os.X_OK)}")

path = input("Enter the path to check: ")
check_access(path)
