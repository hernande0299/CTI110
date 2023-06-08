#This program calculates and displays travel expenses
#6/2/2023
#CTI-110 P1HW2 - Travel Expense
#Eric Hernandez
#
#User inputs their budget, travel destination, and expected cost of gas, accomodation ,and food
#This program calculates and displays travel expenses
#Output of the program displays user's input and remaining balance after costs are calculated
print('This program calculates and displays travel expenses')
print()
# User enters budget
print('Enter Budget:', end=' ')
initial_budget = int(input())
print()
# User enters their travel destination
print('Enter your travel destination:', end=' ')
location = input()
print()
# User enters their expected cost on gas
print('How much do you think you will spend on gas?', end=' ')
fuel = int(input())
print()
# User enters their expected cost for accomodation
print('Approximately, how much will you need for accomodation/hotel?', end=' ')
accomodation = int(input())
print()
# User enters their expected cost for food
print('Last, how much do you need for food?', end=' ')
food = int(input ())
print()
print('------------Travel Expenses------------')
# Program displays user's location input
print('Location:', location)
# Program displays user's initial budget
print('Initial Budget:', initial_budget)
print()
# Program displays user's fuel cost
print('Fuel:', fuel)
# Program displays user's accomodation cost
print('Accomodation:', accomodation)
# Program displays user's food cost
print('Food:', food)
print()
# Program calculates and displays user's reamaining balance
print('Remaining Balance:', initial_budget - (fuel + accomodation + food))










