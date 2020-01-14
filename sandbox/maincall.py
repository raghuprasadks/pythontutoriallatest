def greet(name):
    '''
    greet function is used to greet
    '''
    print('Say Hello',name)    
def play():
    print("let's play")    
def mainfunc():
    print('inside mainfunc')
    greet('Rahul')
    play()
print('value of ',__name__)
if (__name__=='__main__'):
    mainfunc()
print(greet.__doc__)
print(dir(list))
'''
PEMDAS
'''