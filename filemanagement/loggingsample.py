# -*- coding: utf-8 -*-

#https://www.machinelearningplus.com/python/python-logging-guide/

import logging
logging.basicConfig(level=logging.INFO)

def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5
'''
a = 3
b = 4
c = 0
'''
logging.info("Hypotenuse of {a}, {b} is {c}".format(a=3, b=4, c=hypotenuse(3,4)))

#The printed log message has the following default format: {LEVEL}:{LOGGER}:{MESSAGE}.
'''
The 5 levels of logging

DEBUG: Detailed information, for diagnosing problems. Value=10.
INFO: Confirm things are working as expected. Value=20.
WARNING: Something unexpected happened, or indicative of some problem. But the software is still working as expected. Value=30.
ERROR: More serious problem, the software is not able to perform some function. Value=40
CRITICAL: A serious error, the program itself may be unable to continue running. Value=50

'''
logging.basicConfig(level=logging.WARNING)

def hypotenuse(a, b):
    """Compute the hypotenuse"""
    return (a**2 + b**2)**0.5

kwargs = {'a':3, 'b':4, 'c':hypotenuse(3, 4)}

logging.debug("a = {a}, b = {b}".format(**kwargs))
logging.info("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
logging.warning("a={a} and b={b} are equal".format(**kwargs))
logging.error("a={a} and b={b} cannot be negative".format(**kwargs))
logging.critical("Hypotenuse of {a}, {b} is {c}".format(**kwargs))

'''
 How to log to a file instead of the console
 
'''
logging.basicConfig(level=logging.INFO, file='sample.log')
logging.debug("a = {a}, b = {b}".format(**kwargs))
logging.info("Hypotenuse of {a}, {b} is {c}".format(**kwargs))
logging.warning("a={a} and b={b} are equal".format(**kwargs))

'''
How to change the logging format


'''
logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')
logging.info("Just like that!")
 

# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.WARNING)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')

'''
Trace back
'''

# Create or get the logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.INFO)

def divide(x, y):
    try:
        out = x / y
    except ZeroDivisionError:
        logger.exception("Division by zero problem")
    else:
        return out

# Logs
logger.error("Divide {x} / {y} = {c}".format(x=10, y=0, c=divide(10,0)))
