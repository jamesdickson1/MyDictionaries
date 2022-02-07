from multiprocessing import Value


person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

print(type(person["children"]))

print (type(person["pets"]))

# print child - "Betty"

childname = person['children'][1]
print(childname)

# print the pet name of the cat

petname = person['pets']['cat']
print(petname)

# use a for loop to print out all the children

for i in person["children"]:
    print(i)

# use a for loop to print out the type of pet and name of pet

for i in person["pets"]:
    print(i)
    print(person["pets"][i])