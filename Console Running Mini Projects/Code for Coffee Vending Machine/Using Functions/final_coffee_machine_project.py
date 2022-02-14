import sys
from menu_and_resources_coffee_machine import menu_list, resources
sys.path.append("C:\VScode_workspace\python_vscode")
from clear import clear
clear()

# tip : If we want to Turn off the Machine Type 'OFF'
def make_coffee(price):
    '''This function is to start the process to make the coffee.'''
    print("To know about the available resources Type 'report'.")
    print("To know about the Prices of items available Type 'price'.")
    items=['espresso','latte','cappuccino'] # this is the list of items available to loop through inside the program

    choice_end=False
    while choice_end is False:
        global end # to use this variable everywhere in the program, we are using global keyword.
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'report':
            print(f"""
Resources Available:
WATER : {resources["water"]}ml
MILK : {resources["milk"]}ml
COFFEE BEANS : {resources["coffee_beans"]}g
    """)
            print("To know about the Prices of items available Type 'price'.")
        elif choice == 'price':
            print(f'''
Price List:
ESPRESSO : {price["espresso"]}$
LATTE : {price["latte"]}$
CAPPUCCINO : {price["cappuccino"]}$ 
    ''')
            print("To know about the available resources Type 'report'.")
        elif choice == 'off': # to turn the machine off.
            print("Machine Turned OFF") 
            end=True
            break
        elif choice in items:
            choice_end=True
        else:
            print("Kindly type valid text.")
            print()
            continue
    if end!=True:
        check_resources(choice,resources) # after getting the item name as a input, we are calling this function



def check_resources(choice,resources):
    '''This function is to check the available, resources and report the user if it's available or not'''
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        needed_water = menu_list[choice]['ingredients']['water']
        needed_milk = menu_list[choice]['ingredients']['milk']
        needed_coffee_beans = menu_list[choice]['ingredients']['coffee_beans']
        needed_resources=[needed_water,needed_milk,needed_coffee_beans]

        # print(needed_coffee_beans,needed_milk,needed_water)
    if needed_coffee_beans > resources["coffee_beans"]:
        print(f"There is not enough COFFEE_BEANS, to make {choice}.")
    elif needed_milk > resources['milk']:
        print (f"There is not enough MILK, to make {choice}.")
    elif needed_water > resources["water"]:
        print(f"There is not enough WATER, to make {choice}.")
    else:
        check_price(choice,price) # calling function

    count = 0 
    for i in resources: # to update the resources available.
        resources[i] -= needed_resources[count]
        count+=1
    # print(resources)


def check_price(choice,price):
    global end
    '''This function is to check the price, if the needed price is not enough it will again ask to give the amount.'''
    while True:
        coins= {
        "quarters":0.25,
        "dimes":0.10,
        "nickles":0.05,
        "pennies":0.01,
        }

        amount_given=0
        for i in coins: # to get the coins from user.
            number_of_coins = input(f"Enter how many {i} $({coins[i]}) dollar coins: ").lower() # Here also you can type 'off' to turn off the Machine.
            if number_of_coins == 'off':
                end = True
                print("Machine Turned OFF.")
                break
            amount_given+=coins[i] * int(number_of_coins)
            # print(coins[i])
        if end == True:
            break

        if amount_given < price[choice]:
            print("Sorry that's not enough money.")
            print(f"""You have given ${round(amount_given,2)} dollars,
But it's {price[choice]}. """)
            print()
        elif amount_given > price[choice]:
            remaining = round(amount_given - price[choice],2)
            print(f"Here is your ${remaining} dollars in change.")
            coffee_ready(choice)
            break


def coffee_ready(choice):
    '''If all the payment is complete and all the resources are available, this function will execute to make the coffee'''
    print()
    print(f"Here is your {choice} ☕️. Enjoy :)")


price={
    "espresso":1.50,
    "latte":2.50,
    "cappuccino":3.5,
}

end = False
while True: # this loop is to run the program again and again
    make_coffee(price) # Here, we are calling the main() function called make_coffee

    if end == True:
        break

    print()

    again_needed=input("""Type 'y' if you want another, or
Type 'n' or something else to exit : """).lower()
    if again_needed == 'y':
        clear()
        continue
    else:
        print("Exited.")
        break
    