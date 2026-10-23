import random

def get_numbers_ticket(min:int, max:int, quantity:int):  #exercise 2
    if not isinstance(min, int) or not isinstance(max, int) or not isinstance(quantity, int): #checking if the input values are integers
        print("Invalid input, please enter integers.")
        return []
    if min < 1 or max > 1000 or quantity > max or min > max or quantity > (max-min+1) or quantity < 1:
        print("Invalid input.")
        return []
    population = range(min, max + 1)
    return sorted(random.sample(population, quantity))
print(get_numbers_ticket(10, 15, 0)) 