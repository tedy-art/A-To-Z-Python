source_filename = "fromcopy.txt"
destination_filename = "tocopy.txt"

with open(source_filename, 'r') as source_file:
    content = source_file.read()

with open(destination_filename, 'w') as destination_file:
    destination_file.write(content)
