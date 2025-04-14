def find_and_replace(filename, word_to_find, replacement_word):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        occurrences = content.count(word_to_find)
        if occurrences == 0:
            print(f"The word '{word_to_find}' was not found in the file.")
            return 0
        modified_content = content.replace(word_to_find, replacement_word)
        with open(filename, 'w') as file:
            file.write(modified_content)    
        print(f"Successfully replaced {occurrences} occurrence(s) of '{word_to_find}' with '{replacement_word}'")
        return occurrences    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return 0
    except PermissionError:
        print(f"Error: Permission denied. Check if you have proper access rights.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
def main():
    filename = input("Enter the filename: ")
    word_to_find = input("Enter the word to find: ")
    replacement_word = input("Enter the replacement word: ")
    find_and_replace(filename, word_to_find, replacement_word)
if __name__ == "__main__":
    main()