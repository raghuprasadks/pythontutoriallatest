'''
OPERATORS AND EXPRESSIONS
'''

'''
4. Metric Conversion 
Develop and test a Python program that converts pounds
to grams, inches to centimeters, and  
kilometers to miles. The program should allow 
conversions both ways. 
Consider the one pound equal to 453.592 gram, 
one inch equal to 2.54 cm and 
one kilometers to 0.621371 miles. 
'''

def kmToMile(kms):
    return kms*0.621317

miles = kmToMile(100)
print("Km to Miles {0:.2f}".format(miles))

def mileToKm(mile):
    return mile/0.621317

kms = mileToKm(100)
print("Mile to kms {0:.2f}".format(kms))

