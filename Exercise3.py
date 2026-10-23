import re

phone_number = "  +38 ++(050)_)+ 123-45-67"
def normalize_phone(phone_number): #exercise 3
    pattern = r'[^0-9+]'
    formatted_number = re.sub(pattern, '', phone_number)
    if formatted_number.startswith("+"): #for international codes and ukrainian as well
        phone_number = formatted_number
    elif formatted_number.startswith("380"): #for ukrainian number without code
        phone_number = "+" + formatted_number
    else: #for every number without code
        phone_number = "+38" + formatted_number
    pattern = r'[+]' #deleting all plus characters after all checks
    formatted_number = re.sub(pattern, '', phone_number)
    normalized_number = "+" + formatted_number #adding plus for it to be a standart format
    return normalized_number
print(normalize_phone(phone_number))
