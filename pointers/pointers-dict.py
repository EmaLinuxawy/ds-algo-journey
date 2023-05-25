dict1 = {
    'value': 11
    }

dict2 = dict1

print("Before updating values:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter updating values:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict3 = {
    'value': 33
    }
dict1 = dict3
dict2 = dict3

print("\nAdding new dict and updating dict2 values:")
print("dict1 =", dict1)
print("dict2 =", dict2)
print("dict3 =", dict3)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
print("dict3 points to:", id(dict3))