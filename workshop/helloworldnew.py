# -*- coding: utf-8 -*-

print(__name__)
def main1():
    print('hello world')
    otherfunction()
    
def otherfunction():
    print('This is another function')

if(__name__=='__main__'):
    main1()