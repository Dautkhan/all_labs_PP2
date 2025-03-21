def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:  
        for item in data:
            file.write(item + '\n')  

data = ['Apple', 'Banana', 'Cherry']
file_path = "output.txt"
write_list_to_file(file_path, data)
print(f"List has been written to {file_path}")
