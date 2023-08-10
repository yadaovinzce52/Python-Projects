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
    'money': 0
}


def check_resources(coffee_type):
    if coffee_type not in MENU:
        return 'That is not on our menu, try again'

    for key, val in MENU[coffee_type]['ingredients'].items():
        if resources[key] < val:
            return f'Sorry there is not enough {key.lower()}'


while True:
    user_choice = input('What would you like? (Espresso/Latte/Cappuccino): ').lower()

    if user_choice == 'off':
        break
    elif user_choice == 'report':
        water = resources['water']
        milk = resources['milk']
        coffee = resources['coffee']
        money = resources['money']
        print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}')
    else:
        result = check_resources(user_choice)
        if result:
            print(result)
        print('Please insert coins.')
        quarters = 0.25 * int(input('How many quarters?: '))
        dimes = 0.1 * int(input('How many dimes?: '))
        nickles = 0.05 * int(input('How many nickles?: '))
        pennies = 0.01 * int(input('How many pennies?: '))
        total = quarters + dimes + nickles + pennies

        if total < MENU[user_choice]['cost']:
            print('Sorry that\'s not enough money. Money refunded.')
        else:
            resources['money'] += MENU[user_choice]['cost']
            change = round(total - MENU[user_choice]['cost'], 2)
            if change > 0:
                print(f'Here is ${change} in change.')

            for key, val in MENU[user_choice]['ingredients'].items():
                resources[key] -= val

            print(f'Here is your {user_choice}. Enjoy!')
