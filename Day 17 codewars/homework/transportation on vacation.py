# After a hard quarter in the office you decide to get some rest on a vacation. 
# So you will book a flight for you and your girlfriend 
# and try to leave all the mess behind you.

# You will need a rental car in order for you to get around in your vacation. 
# The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, 
# you get $50 off your total. Alternatively, if you rent the car for 3 or more days, 
# you get $20 off your total.

# Write a code that gives out the total amount for different days(d).


def rental_car_cost(d):                 # we create a function
    one_day = 40                        # acording to exem one day cost 40$. We created a variable end it equals 40
    if d < 3:                           # acording to exem if employer rent car less then 3 day they pay 40$
        return d * one_day              # number of day will multiply 40$
    if d >= 3 and d < 7:                # if number of day is 3 and more also less then 7, there is discount 20$
        return (d * one_day) - 20       # number of day will multiply 40$ and will be subtracted 20$
    return (d * one_day) - 50           # but number of day is 7 and more we will multiply 40$ and will be subtracted 50$





# def rental_car_cost(d):
#     result = d * 40
#     if d >= 7:
#         result -= 50
#     elif d >= 3:
#         result -= 20
#     return result