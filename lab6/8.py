import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):  
        os.remove(path)  # Удаляем файл
        print(f"File at {path} has been deleted.")
    else:
        print("File does not exist or you do not have permission to delete it.")

path = input("Enter the file path to delete: ")
delete_file(path)
