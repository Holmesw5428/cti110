# This program will calculate the number of pizzas and slices needed
# 2-15-2022
# CTI-110 P1HW2 - Pizza Order
# William holmes

# variables to hold number of people
# input

numberPeople = int(input("how many students do you want to order pizza for? "))

# calculations
# get number of pizzas
numberPizzas = numberPeople / 2

# number of slices

numberSlices = numberPeople * 3

# display information

print("")
print("----Pizza Order--------")
print("Number of Students: ",numberPeople,sep='')
print("Pizza Slices Needed: ",numberSlices,sep='')
print("pizzas needed: ",numberPizzas,sep=' ')
