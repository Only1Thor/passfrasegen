from random import *

ordlisteFil = open("ordliste.txt","r")

alleOrd=[]
for word in ordlisteFil:
    alleOrd.append(word)

print("antall ord:" + str(len(alleOrd)))
print( 
        alleOrd[ randint( 0, len(alleOrd) -1 ) ] 
    )