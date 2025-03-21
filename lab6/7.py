def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:  # Открываем исходный файл в режиме чтения
            contents = src_file.read()
        with open(destination, 'w') as dest_file:  # Открываем целевой файл в режиме записи
            dest_file.write(contents)
        print(f"Contents copied from {source} to {destination}")
    except FileNotFoundError:
        print("Source file not found!")

source = input("Enter the source file path: ")
destination = input("Enter the destination file path: ")
copy_file(source, destination)
