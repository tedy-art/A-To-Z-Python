def calculate_word_frequency(file_path):
    # Step 1: Open the file
    with open(file_path, 'r') as file:
        # Step 2: Read the content and split into words
        content = file.read()
        words = content.split()

    # Step 3: Create a dictionary to store word frequencies
    word_freq = {}

    # Step 4: Count word frequencies
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Step 5: Display or save results
    for word, freq in word_freq.items():
        print(f'{word}: {freq} times')


# Example usage
file_path = 'tocopy.txt'
calculate_word_frequency(file_path)
