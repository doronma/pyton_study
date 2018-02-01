# dictionary
fruit = {"orange" : "a sweet, orange, citrus fruit",
         "apple" : "good for making cider"}
print (fruit["apple"])

bike = {"make" : "Honda" , "model" : "250", "color" : "red"}
print(bike)
print (bike["color"])
bike["color"] = "green"
param = "make1"
print(bike.get(param))
if not param in bike:
    print("{} is not in bike...".format(param))
print(bike.get(param,"Param Not found"))    
bike["year"] = 1980
del bike["model"]
print(bike)
for key in bike:
    print("{0} - {1}".format(key,bike[key]))
print('')
keys = list(bike.keys())
keys.sort()
for key in keys:
    print("{0} - {1}".format(key,bike[key]))
print('')
for key in sorted(bike.keys()):
     print("{0} - {1}".format(key,bike[key]))
print('')
for val in bike.values() :
    print("value is {}".format(val))

print(bike.items())
f_tuple = tuple(bike.items()) # new tuple
print(f_tuple)

for item in f_tuple:
    key,value = item
    print("key - {0}, value - {1}".format(key,value))


bike['name']='unknown'
print(f_tuple)

print(dict(f_tuple))

# bike.clear()
# print(bike)


# lists
list1 = [1,2,5,8]
print (list1[2])