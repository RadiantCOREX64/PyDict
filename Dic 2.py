car = {"Brand": "Ford", "Model": "Mustang", "year": 1965, "colors": ["Blue", "red"]}

##For at undgå error til objekter som ikke findes i listen kan man definere dem som som ny objekter
print(car.get("city" , "Nadaram"))

print(car.get("Name" , "Nist"))

car.clear()

print(car)
