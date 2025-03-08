# To find the give data type 
a = {"apple", "Mango"}
print(type(a))

# To remove element in set
a.remove("apple")
print(a)
a.discard("orange") # Remove the element and there no that element should no show the error
print(a)

# Add the element in set
b = a
b.update("banana")
print(b)
a.update({"apple"})
print(a)

# Operation in set
s1 = {1,2,3,4,5}
s2 = {2,8,7,6,4}
print(s1|s2) # No repeated element
print(s1&s2) # Only repeated element
print(s1-s2) # difference in first element
print(s1^s2) # different element in both inputs