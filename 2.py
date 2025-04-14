import csv
def display_csv(filename):
    try:
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            if not rows:
                print("The CSV file is empty.")
                return False
            col_widths = []
            for row in rows:
                while len(col_widths) < len(row):
                    col_widths.append(0)
                for i, cell in enumerate(row):
                    col_widths[i] = max(col_widths[i], len(str(cell)))
            print("\nCSV File Contents:")
            print("-" * (sum(col_widths) + 3 * len(col_widths) + 1))
            for i, row in enumerate(rows):
                row_str = "| "
                for j, cell in enumerate(row):
                    if j < len(col_widths):
                        row_str += str(cell).ljust(col_widths[j]) + " | "
                print(row_str)
                if i == 0:
                    print("-" * (sum(col_widths) + 3 * len(col_widths) + 1))
            
            print("-" * (sum(col_widths) + 3 * len(col_widths) + 1))
            return True        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return False
    except csv.Error as e:
        print(f"CSV Error: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
def main():
    filename = input("Enter the CSV filename to display: ")
    display_csv(filename)
if __name__ == "__main__":
    main()