phone_balance = 4
bank_balance = 100

print(phone_balance, bank_balance)

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance, bank_balance)

n = 3
if n % 2 == 0:
    print("Number " + str(n) + " is even.")
else:
    print("Number " + str(n) + " is odd.")

print("Enter the season you are currently in: ")
season = input()
if season == 'spring' or season == 'Spring':
    print('Plant the garden!')
elif season == 'summer' or season == 'Summer':
    print('Water the garden!')
elif season == 'fall' or season == 'Fall':
    print('Harvest the garden!')
elif season == 'winter' or season == 'Winter':
    print('Stay indoors!')
else:
    print('Unrecognized season, please enter a valid season.')

age = 35

# age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)

# code that lets a competitor know which of these prizes they won based
# on the number of points they scored.

points = 60
if 1 < points < 50:
    prize = "wooden rabbit"
    result = "Congratulations! You have won a {}".format(prize)
elif 51 < points < 150:
    prize = "no prize"
    result = "Oh dear, no prize this time."
elif 151 < points < 180:
    prize = "wafer-thin mint"
    result = "Congratulations! You have won a {}".format(prize)
else:
    prize = "penguin"
    result = "Congratulations! You have won a {}".format(prize)

print(result)

