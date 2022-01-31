f = open('9. Chapter 9/sample.txt')
# read first line
data = f.readline()
print(data)

# read second line
data = f.readline()
print(data)

# read third line 
data = f.readline()
print(data)

# read fourth line
data = f.fileno()
print(data)

f.close()