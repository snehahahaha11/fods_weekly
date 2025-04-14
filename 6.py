def count_file_statistics(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            char_count = len(content)
            file.seek(0)
            lines = file.readlines()
            line_count = len(lines)
            word_count = len(content.split())
            
            return (line_count, word_count, char_count)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return (0, 0, 0)
    except Exception as e:
        print(f"An error occurred: {e}")
        return (0, 0, 0)
def main(): 
    filename = input("Enter the filename to analyze: ")
    lines, words, chars = count_file_statistics(filename)
    if lines > 0 or words > 0 or chars > 0:
        print("\nFile Statistics:")
        print("-" * 20)
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        print(f"Number of characters: {chars}")
if __name__ == "__main__":
    main()