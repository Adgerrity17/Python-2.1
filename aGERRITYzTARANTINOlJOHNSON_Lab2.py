#This program will determine the users annual consumption of gas in both MPG and KPL. Additionally, the program will calculate the users spending on gas
#and based upon mpg and spending the program will suggest if they need a new car or not

print('This program will calculate your MGP/ KPL, annual spending on gas, and make a suggestion as to whether or not you need a new car')

import math
name = input("Please enter your name: ")
print('hello', name)
home = input("where are you from (city and state): ")
user_car = input("What make model and year of car do you have? : ")
gal_str = input("how many gallons of gas do you use in a average week? : ")
gal_int = int(gal_str)
mile_str = input("and roughly how many miles do you drive? : ")
mile_int = int(mile_str)
mpg = round(mile_int/gal_int, 0)
kpl = round(0.425*mpg, 0)#according to google 1 MPG is equal to 0.425 KPL
gas_str = (2.302)#according to AAA this is the national average price of gas for 9/17/2015
gas_int = int(gas_str)
cost_mpg = round(gal_int*gas_int, 0)
year_gal = round(gal_int*52, 0)
year_cost = (gas_int*year_gal)
print('your car gets' ,mpg, 'mpg and', kpl, 'kpl')
print('this means you are spending', cost_mpg,'$ per week and', year_cost,'per year')
if (mpg < 30):
    print('you should consider getting a new car')
else:
    print('your car is fuel efficient')
