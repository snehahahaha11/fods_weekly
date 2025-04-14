#Write a function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature for each day of the week, a temperature value, and the day of the week for the recorded temperature. The function should then add the temperature to the dictionary only if 
#it does not already contain a temperature for that day. The function should return the resulting dictionary, whether it is updated or not
    
def add_daily_temp(temps_dict, temp, day):
    # Add temperature if day is not already in the dictionary
    if day not in temps_dict:
        temps_dict[day] = temp
    return temps_dict

if __name__ == "__main__":
    # Example usage
    daily_temps = {}
    # Sample calls (or you can prompt the user)
    daily_temps = add_daily_temp(daily_temps, 75.5, "Monday")
    daily_temps = add_daily_temp(daily_temps, 80.0, "Tuesday")
    # Attempting to add temperature for Monday again (should not update)
    daily_temps = add_daily_temp(daily_temps, 78.0, "Monday")
    print("Daily Temperatures:", daily_temps)