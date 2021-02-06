import random

ordlisteFil = open("ordliste.txt","r")

alleOrd=[]
for word in ordlisteFil:
    alleOrd.append(word)

print("antall ord:" + str(len(alleOrd)))
print(random.choice(alleOrd))