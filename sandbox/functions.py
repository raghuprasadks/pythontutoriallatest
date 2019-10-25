# -*- coding: utf-8 -*-


def simpleInterest(principal,rate,time):
    si = principal*rate*time/100
    return si

principal = float(input('Enter principal amount'))
rate = float(input('Enter rate of interest '))
time = float(input('Enter time of interest '))
si = simpleInterest(principal,rate,time)
print('simple interest ',si)

