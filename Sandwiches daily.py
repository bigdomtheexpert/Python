again = "yes"
while again =="yes":


    print("Hi welcome to Sandwiches Daily")
    print("This is our menu for today")

    print(
        """


    \nOption 1
    Sandwiches of the week 
    Tuna and Cucumber $1.50
    Egg and Mayo $1.75
    Prawn cocktail $2.00
    \nOption 2
    Meat specials 
    Ham and Cheese $1.00
    Chicken fillet $2.50
    Steak and mayo $3.00

    """)

    sandwich = input("What Sandwich would you like ")
    
    if sandwich =="Tuna and Cucumber":
            print("\nOk that will cost you $1.50")
            again = input("Do you wnat to have anything else (yes/no) ")
    elif sandwich =="Egg and Mayo":
            print("\nOk that will cost you $1.75")
            again = input("Do you wnat to have anything else (yes/no) ")
    elif sandwich =="Prawn cocktail":
            print("\nOk that will cost you $2.00")
            again = input("Do you wnat to have anything else (yes/no) ")
    elif sandwich =="Ham and Cheese":
            print("\nOk that will cost you $1.00")
            again = input("Do you wnat to have anything else (yes/no) ")
    elif sandwich =="Chicken fillet":
            print("\nOk that will cost you $2.50")
            again = input("Do you wnat to have anything else (yes/no) ")
    elif sandwich =="Steak and Mayo":
            print("\nOk that will cost you $3.00")
            again = input("Do you wnat to have anything else (yes/no) ")
    else:
        again = input("Sorry that was not an option, do you want to order something else (yes or no)")

        
        



                
            

