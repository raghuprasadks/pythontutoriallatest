# -*- coding: utf-8 -*-

units = int(input("Enter units consumed"))

amt = 0
if (units <= 50):
    amt = units * .5
elif (units >50 and units<=100):
    amt = 50 *.5 + (units - 50)*1
elif (units >100 and units<=200):
    amt = 50 *.5 + 50 * 1 + (units - 100)*2
elif (units >200 and units<=300):
    amt = 50 *.5 + 50 * 1 + 100 * 2 + (units - 200)*3
elif (units >300):
    amt = 50 *.5 + 50 * 1 + 100 * 2 + 100 * 3 + (units - 300)*4

print('Bill amount',amt)


