from datetime import datetime, timedelta 
import random
import re
#date = input("Enter a date in the format YYYY-MM-DD:").strip() #<-- activate this line, stripping whitespace from the input

def get_days_from_today(date): #exercise 1
    i = 1
    while i == 1: #infinite loop to keep asking for a valid date until the user inputs it correctly
    
        try: #catching ValueError if the user inputs an invalid date format
            date_str = datetime.strptime(date, '%Y-%m-%d').date() #converting the input string to a date object
            i = 0
            today = datetime.now().date() #getting today's date
            return (date_str - today).days #difference in days between the input date and today's date
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.") #if the user inputs an invalid date format, print an error message and ask for the input again
            date = input("Enter a date in the format YYYY-MM-DD:").strip()
        
#print(str(get_days_from_today(date)) + " days") #<-- activate this line


def get_numbers_ticket(min:int, max:int, quantity:int):  #exercise 2
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int):
        print("Invalid input, please enter integers.")
        return []
    if min < 1 or max > 1000 or quantity > max or min > max:
        print("Invalid input. Please enter a minimum value greater than 0, a maximum value less than or equal to 1000, and a quantity, minimum value less than max.")
        return []
    population = range(min, max + 1)
    return sorted(random.sample(population, quantity))
#print(get_numbers_ticket(1, 500, 10)) #<-- activate this line


phone_number = "38050-111-22-22"
def normalize_phone(phone_number): #exercise 3
    if phone_number.startswith("+"): #for international codes and ukrainian as well
        phone_number = phone_number
    elif phone_number.startswith("380"): #for ukrainian number without code
        phone_number = "+" + phone_number
    else: #for every number without code
        phone_number = "+38" + phone_number
    pattern = r'\D' #deleting all non-digit characters from the phone number
    formatted_number = re.sub(pattern, '', phone_number)
    normalized_number = "+" + formatted_number #adding plus for it to be a standart format
    return normalized_number
#print(normalize_phone(phone_number)) #<-- activate this line

users = [
    {"name": "John Doe", "birthday": "1985.01.24"},
    {"name": "Jane Smith", "birthday": "1990.10.27"}
]

def get_upcoming_birthdays(users): #exercise 4
    upcoming_birthdays = [] #creating a list to store upcoming birthdays
    today = datetime.now().date() #using variable to store today's date
    for user in users: #iterating through the list of users
        birth_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date() #converting the birthday string to a date object
        birthday_this_year = birth_date.replace(year=today.year) #replacing the year of the birthday with the current year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1) #if the birthday has already passed this year, replace the year with the next year
        delta = (birthday_this_year - today).days #calculating the difference in days between the birthday and today's date
        if 0 <= delta <= 7: #if the birthday is within the next 7 days, check if it falls on a weekend
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)
            upcoming_birthdays.append({"name": user["name"], 'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")}) #adding the user's name and the congratulation date to the list of upcoming birthdays
    return upcoming_birthdays

#print(get_upcoming_birthdays(users)) <-- activate this line
