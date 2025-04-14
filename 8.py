import re
import string
def count_word_occurrences(filename):
    try:
        word_counts = {}
        with open(filename, 'r') as file:
            content = file.read().lower()
            for punct in string.punctuation:
                content = content.replace(punct, ' ')
            words = content.split()
            for word in words:
                word = re.sub(r'[^a-zA-Z0-9]', '', word)
                if not word:
                    continue
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
        return word_counts    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}
def display_word_counts(word_counts):
    if not word_counts:
        print("No words to display.")
        return
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    max_word_len = max(len(word) for word in word_counts.keys())
    print("\nWord Occurrences:")
    print("-" * (max_word_len + 15))
    print(f"{'Word'.ljust(max_word_len)} | Occurrences")
    print("-" * (max_word_len + 15))
    for word, count in sorted_counts:
        print(f"{word.ljust(max_word_len)} | {count}")
    print("-" * (max_word_len + 15))
    print(f"Total unique words: {len(word_counts)}")
def main():
    filename = input("Enter the filename to analyze: ")
    word_counts = count_word_occurrences(filename)
    display_word_counts(word_counts)
if __name__ == "__main__":
    main()