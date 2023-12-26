file_path = 'example.txt'

# write
with open(file_path, 'w') as file:
    file.write("Hello, this is sample text.")

# read
with open(file_path, 'r') as file:
    content = file.read()
    print(content)