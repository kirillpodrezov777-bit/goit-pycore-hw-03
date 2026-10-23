from datetime import datetime, timedelta

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

print(get_upcoming_birthdays(users))