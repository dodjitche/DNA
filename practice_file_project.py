#practice file 
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


'''
import random
colors = ['red', 'blue']
print random.choice (colors)

random.shuffle(colors)

'''
'''


for i in xrange (3):
    print (i)
'''
#1
'''
from Tkinter import *

root = Tk()

w = Label(root, text = "Hello, World")
w.pack()

root.mainloop()
'''
#2
'''
from Tkinter import *

class App:
    def _init_ (self, master):
        frame = Frame(master)
        frame.pack ()

        self.button = Button(
            frame, text = "QUIT", fg = "red", command=frame.quit
            )
        
        self.button.pack(side = LEFT)

        self.hi_there = Button (frame, text = "Hello", comand= self.say_hi)
        self.hi_there.pack(side = LEFT)

    def say_hi (self):
        print ("hi there, everyone!")
        

root = Tk()
app = App(root)

root.mainloop()


'''


'''
from Tkinter import *

root = Tk()

e = Button (root)
e.pack(side = LEFT )

root.mainloop()
'''

'''

class Song (object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song (self):
        for line in self.lyrics:
            print (line)

happy_bday = Song (["happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
bulls_on_parade = Song (["They rally around that family",
                         "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

'''


from Tkinter import *

class Application (Frame):
    def say_hi (self) :
        print "hi there, everyone!"
    def createWidgets (self):
        self.QUIT = Button (self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack ({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there ["text"]= "Hello",
        self.hi_there["command"] = self.say_hi()

        self.hi_there.pack ({"side": "left"})

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master = root)
app.mainloop()
root.destroy()