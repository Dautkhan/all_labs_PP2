def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:  
            lines = file.readlines()
            print(f"Number of lines in the file: {len(lines)}")
    except FileNotFoundError:
        print("File not found!")

file_path = input("Enter the path to the text file: ")
count_lines(file_path)
