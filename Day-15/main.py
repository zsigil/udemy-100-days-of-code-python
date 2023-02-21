#COFFEE MACHINE
#print report
#check resources - stop or make coffee
#process coins / quarters (0.25),dimes (0.1),nickels(0.05),pennies(0.01)
#check if transaction was successful - return coins or make coffee

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def report():
    print(f"Water: {resources['water']}ml") 
    print(f"Milk: {resources['milk']}ml") 
    print(f"Coffee: {resources['coffee']}g") 
    print(f"Money: ${money}") 

def check_resources(chosen_drink):
    for item in chosen_drink['ingredients']:
        if resources[item] < chosen_drink['ingredients'][item]:
            return {"text":f"Sorry, there is not enough {item}.", "success": False}
        else:
            return {"text":f"Please insert coins.", "success": True}


def deduct_resources(chosen_drink):
    for item in chosen_drink['ingredients']:
        resources[item] -= chosen_drink['ingredients'][item]


def check_coins(quarter, dime, nickel, penny, price):
    """
    Checks sum of coins, returns amount of money to be returned if more.
    Will be negative if money is not enough.
    """
    coins_payed = quarter*0.25 + dime*0.1 + nickel*0.05 + penny*0.01
    return coins_payed - price

def formatted_money(mon):
    return '{:.2f}'.format(mon)

is_on = True

while is_on:
    
    chosen = input("What would you like? (espresso/latte/cappuccino): ")
    if chosen == "off":
        print("Turning machine off.")
        is_on = False

    elif chosen == "report":
        report()

    else:
        #check resources
        print(check_resources(MENU[chosen])["text"])
        if check_resources(MENU[chosen])["success"]:
            
            #check money
            quarter = int(input("How many quarters: "))
            dime = int(input("How many dimes: "))
            nickel = int(input("How many nickels: "))
            penny = int(input("How many pennies: "))

            difference = check_coins(quarter, dime, nickel, penny, MENU[chosen]["cost"])

            if difference < 0:
                print("Sorry that's not enough money. Money refunded.")
                continue
            elif difference > 0:
                print(f"Here is ${formatted_money(difference)} dollars in change")
            else:
                print("Exact amount, thank you")

            #deduct ingredients
            #add money
            deduct_resources(MENU[chosen])
            money += MENU[chosen]["cost"]

            print(f"Here is your {chosen}. Enjoy!.")