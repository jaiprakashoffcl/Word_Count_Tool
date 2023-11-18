import string

def word_count(text):
    words = text.split()
    word_count_dict = {}

    for word in words:
        # Remove punctuation and convert to lowercase for better accuracy
        word = word.strip(string.punctuation)
        word = word.lower()

        if word:
            word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict

def character_count(text):
    return len(text)

def most_common_words(word_count_dict, n=5):
    sorted_words = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:n]

def unique_words_count(word_count_dict):
    return len(word_count_dict)

def process_text(input_text):
    result = word_count(input_text)
    char_count = character_count(input_text)
    unique_count = unique_words_count(result)

    print("\nWord count result:")
    for word, count in result.items():
        print(f"{word}: {count}")

    print(f"\nCharacter count: {char_count}")

    top_words = most_common_words(result)
    print(f"\nTop 5 most common words: {top_words}")

    print(f"\nUnique words count: {unique_count}")

if __name__ == "__main__":
    user_choice = input("Enter '1' to enter text or '2' to read from a file: ")

    if user_choice == '1':
        input_text = input("Enter the text: ")
        process_text(input_text)
    elif user_choice == '2':
        file_path = input("Enter the file path: ")

        try:
            with open(file_path, 'r') as file:
                file_text = file.read()
                process_text(file_text)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
    else:
        print("Invalid choice. Please enter '1' or '2'.")