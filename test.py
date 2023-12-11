L = ['I', 'like', 'programming', '!']
f = open('output.txt','w')
for item in L:
    f.write(str(item))
f.close()
f = open('output.txt', 'r')
print(f.readlines())
f.close()