## Bruges til at tilføje værdier til vores nøgler fra to separat lister, her bruger man funktionen dict(zip)

keys = ["a" , "b" , "c" , "d" , "e"]

values = [1 , 2 , 3 , 4 , 5]

myDict = dict(zip(keys , values))

print(myDict)

Names = ["Lars" , "Rasmus" , "Chris" , "Jonas"]

City = ["København" , " Næstved" , "Roskilde" , "Borup"]

myDict = dict(zip(Names , City))

print(myDict)