oMeuSet = {"maçã", "banana", "laranja"}

for set in oMeuSet:
    print(set)
    
oMeuSet.add("uva")
oMeuSet.remove("laranja")


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["model"])
thisdict["model"] = "Corvette"

print(thisdict["model"])

for key in thisdict:
    print(key)
    
for key in thisdict:
    print(thisdict[key])