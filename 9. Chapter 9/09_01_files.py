# # Use open function to read the content of a file!
# # f = open('sample.txt', 'r')
# f = open('sample.txt') # by default the mode is r
# # data = f.read()
# data = f.read(5) # reads first 5 characters from the file
# print(data)
# f.close()

# f = open('sample.txt','r')
fw = open('9. Chapter 9/sample.txt', 'a')
fw.write('He should learn machine learning in future.')
fr = open('9. Chapter 9/sample.txt')

data = fr.read()
print(data)
fr.close()
fw.close()
