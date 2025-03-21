import os

def path_info(path):
    if os.path.exists(path):
        print(f"The path exists.")
        print(f"Directory portion: {os.path.dirname(path)}")
        print(f"File portion: {os.path.basename(path)}")
    else:
        print(f"The path does not exist.")

path = input("Enter a path: ")
path_info(path)
