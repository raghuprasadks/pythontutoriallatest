#https://www.w3schools.com/python/python_json.asp

# 1 -Parse JSON - Convert from JSON to Python

import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x: y is dictionary
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# 2 - Convert from a Python object (dict) to json:
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


'''
3 - You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
'''

print(json.dumps({"name": "John", "age": 30}))

lstjson = json.dumps(["apple", "bananas"]) 

print(type(lstjson))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''
4 - When you convert from Python to JSON, 
Python objects are 
converted into the JSON (JavaScript) equivalent:
Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
    
    
'''

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

'''
You can also define the separators, default value is (", ", ": "), which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:
    
    
'''
# use . and a space to separate objects, and a space, 
#a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

print(json.dumps(x, indent=4, sort_keys=True))
