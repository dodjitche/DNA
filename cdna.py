#Precious!
'''
filename = 'cdnatext.txt'
book = open (filename)
lines = book.readlines()
book.close()

lines = lines[8:]
count= 0
for line in lines:
    line = line[:-2]
    count += 1
    if 'f' in line:
        line = line [14:]
    print (count, line)

'''

#lower case of  the sequence od cdna 
'''
filename = 'cdnatext.txt'
book = open (filename)
lines = book.readlines()
book.close()

lines = lines[8:]
for line in lines:
    line = line[:-2]
    if 'f' in line:
        line = line [14:]
    line = line.lower()
    print (line)
'''




def lowerdna( file):
    filename = 'file'
    book = open (filename)
    lines = book.readlines()
    book.close()

    lines = lines[8:]

    for line in lines:
        line = line[:-2]
        if 'f' in line:
            line = line [14:]
        line = line.lower()
        line = cleantext

    return cleantext

for line in lowerdna(cdnatext.txt):
    print (line)

    
'''
    print (count,'***', line)
'''

'''
filename = 'cdnatext.txt'
book = open(filename)
lines = book.readlines()
book.close()

lines = lines[8:]

for line in lines:
    line = line.deode()[:-1]
    print (line)
'''

