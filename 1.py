def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
            with open(destination_file, 'w') as destination:
                destination.write(content)   
            print(f"File copied successfully from '{source_file}' to '{destination_file}'")
            return True        
    except FileNotFoundError:
        print(f"Error: Source file '{source_file}' not found.")
        return False
    except PermissionError:
        print(f"Error: Permission denied. Check if you have proper access rights.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
def main():
    source = input("Enter the source filename: ")
    destination = input("Enter the destination filename: ")
    copy_file(source, destination)
if __name__ == "__main__":
    main()