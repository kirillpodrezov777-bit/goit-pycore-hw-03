from datetime import datetime

date = input("Enter a date in the format YYYY-MM-DD:").strip() #stripping whitespace from the input
def get_days_from_today(date): #exercise 1  
    try: #catching ValueError if the user inputs an invalid date format
        date_str = datetime.strptime(date, '%Y-%m-%d').date() #converting the input string to a date object
        today = datetime.now().date() #getting today's date
        return (date_str - today).days #difference in days between the input date and today's date
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.") #if the user inputs an invalid date format, print an error message and ask for the input again
        date = input("Enter a date in the format YYYY-MM-DD:").strip()
        
print(str(get_days_from_today(date)) + " days") 