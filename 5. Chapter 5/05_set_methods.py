# Creating an empty set
b = set()
# print(b)

# Adding value to empty set
b.add(3)
b.add(4)
b.add(4) #repeatedly putting same data won't change the set
b.add(5)
# b.add({1,2,3,4,5})


# Accessing the elements 
# b.add({4:5}) # cannot add a list or dict to sets
# print(b)

# len of the set
# print(len(b))

#Removal of an Item
# b.remove(5)
# b.remove(15) # throws an error 'cause 15 isn't in the set
b.pop()
print(b)






3






























# ## Accessing Elements
# # b.add({4:5}) # Cannot add list or dictionary to sets
# print(b)

# ## Length of the Set
# print(len(b)) # Prints the length of this set
# b = set()
# print(type(b))
# b.add(4)
# b.add(5)
# b.add(5) # Adding a value repeatedly does not changes a set
# b.add((4, 5, 6))

# ## Removal of an Item
# b.remove(5) # Removes 5 fromt set b
# # b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
# print(b)

# print(b.pop())
# print(b)