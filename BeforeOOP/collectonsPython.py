  # collection = single variable used to store multiple values
  # List = [] ordered and changeable. DUPLICATES OK
  # Set = {} unordered (print garda jun order ma ni huna sakcha tei bara index print garda err) and immutable, but Add/Remove OK. No duplicates
  #
  # Tuple = () ordered and unchangeable. DUPLICATES OK. FASTER

fruits = ["apple","banana","orange","coconut","apple"]
print(fruits)
print(len(fruits))

#all the methods available
# print(help(fruits))
# print(dir(fruits))

fruits[0] = "kiwi"
print(fruits.count("banana"))

fruits.append("avocado")
fruits.remove("orange")
fruits.insert(0,"kera")
fruits.sort()
fruits.reverse()

fruits.clear()
for fruit in fruits:
    print(fruit)










