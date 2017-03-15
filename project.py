'''
greeting = 'Hello World'

print "greeting[0:6] ", greeting[0:6]

'''
'''
names = ['Lyle PUENTE', 'Tyler Joseph', 'Josh Dun']
print names [0]
'''

'''
dict = {'Name' : 'Lyle Puente', 'age' : 53, 'Num_albums' : 6}

print "dict['Name'] = ", dict ['Name']
print dict ['age']
print dict.items();
print dict.keys();
print dict.values()
'''
'''
my_string = 'Adriana WISE'

if (my_string== 'Adriana WISE'):
    print  "My name is %s" % my_string

print "Good bye"
'''
'''
my_name = ' Adrina WISE'

for i in range (0,10):
    print my_name 
'''
'''
my_name = 'Adriana WISE'

i=0
while (i<10):
    print my_name
    i+=1
'''
'''

def printme(str):
    print str
    return
my_string = " My name."
printme (my_string)

'''

'''


def change ( original_list):
    original_list += ['Josh Dun']
    return

original_list = ['Lyle PUENTE', 'Tyler JOSEPH']

print original_list
change (original_list)
print original_list
'''

'''
def printinfo (arg1, *vartuple):
    print "output is: "
    print "arg1=", arg1
    for var in vartuple:
        print var
    return;

printinfo (10)
printinfo (70,60,50) 

'''

''' unit 6'''



import random
colors = ['red', 'blue']
print random.choice (colors)

random.shuffle(colors)







































