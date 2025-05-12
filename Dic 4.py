countries = {"Russia" : "Moscow" , "China" : "Beijing" , "India" : "Dehlie" , "Turkey" : "Ankara"}
## Bruges til print både nølgen og værdien
print (countries)
##Bruges til kun print nøglen
x = countries.keys()

print(x)

print(type(countries))

print(type(x))

##Bruges til fjern enkelt nøgle fra listen
del countries["China"]