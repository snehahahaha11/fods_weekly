#Write a function named get_daily_temps that prompts the user for the average temperature for each day of the week and returns a
#dictionary containing the information the user entered. 

def get_daily_temps():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    temps = {}
    for day in days_of_week:
        while True:
            try:
                temp = float(input(f"Enter the average temperature for {day}: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        temps[day] = temp
    return temps

if __name__ == "__main__":
    daily_temps = get_daily_temps()
    print("Weekly Temperatures:", daily_temps)