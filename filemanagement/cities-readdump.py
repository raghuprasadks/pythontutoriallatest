import pickle
f = open("cities_and_times.pkl", "rb")
content = pickle.load(f)
print(type(content))
print(content)
