
available_toppings = [',mushrooms', 'olives', 'green peppers'
                      , 'pepperone', 'pineapple', 'extra cheese']


requested_toppings = [ 'pepperone', 'french fries', 'extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings in available_toppings:
        print(f"Adding {requested_toppings}.")
    else:
        print(f"Sorry we are out of {requested_toppings}.")
    
print("\nFinished making your pizza!")
    
