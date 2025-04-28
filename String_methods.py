#Strings are immutable

a = "harry!!!!!! harry"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("harry","Suman"))
print(a.split(" "))
print(a.capitalize())
print(len(a))
print(len(a.center(50)))
print(a.count("harry"))
print(a.endswith("!!"))
print(a.endswith("harry",5,29))
print(a.find("harry"))

print(a.isalnum())
print(a.islower())
print(a.isspace())
print(a.istitle())
print(a.swapcase())
print(a.title())