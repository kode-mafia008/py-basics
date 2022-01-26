myDict = {
    'fast': 'In a Quick Manner',
    'Erus': 'A coder',
    'Marks': [0, 1, 2, 3],
    'anotherdict': {'erus': 'kodemafia'},
    1: 2
}
# myDict['Marks'] = [5,4,3]
# print(myDict['Marks'][2])
# print(myDict)
# print(type(myDict.keys())) #Prints the keys of the dictionary
# print(list(myDict.values())) #prints the values of the dictionary
# print(list(myDict.items())) #prints the (key,value) for all the contents of the dictionary
print(myDict)
updateDict = {
    'hero': 'jet',
}
# updates the dictionary by adding key-value pairs for all the content of list
myDict.update(updateDict)
print(myDict)

# The difference between .get and [] syntax dictionayes
# throws an error as kodegod is not present in the list
print(myDict["kodegod"])
print(myDict.get)
