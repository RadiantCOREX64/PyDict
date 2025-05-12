##Range bruges til gentagelser eksempelvis et tal 
##start fra 5 til 20 1 ad gangen hvor 20 tælles ikke med

##stat, stop, step

dic1 = dict.fromkeys(range(5 , 20 , 1), False)
dic2 = dict.fromkeys(range(2 , 16 , 2), True)
dic3 = dict.fromkeys(range(0 , 90 , 3), "Thomas")

print(dic1)
print(dic2)
print(dic3)