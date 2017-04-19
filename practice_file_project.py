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

'''



'''
import sqlite3

connection = sqlite3.connect ('CSCI233/test.CSCI233')

cursor = connection.cursor()

sql = '''CREATE TABLE IF NOT EXISTS Person
                (PID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(100),
                HEIGHT INT) '''

cursor.execute(sql)


sql = "INSERT INTO Person (NAME, HEIGHT) VALUES ('Jayanam', 174) "
cursor.execute(sql)



connection.commit()


sql = 'SELECT * FROM Person'
cursor.execute()

rows = cursor.fetchall()

for row in rows :
    print(rows)

'''










'''

from Tkinter import *






# replaced  ATG (start codon): Met(M) by Start codon

code = {     'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
             'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
             'tta': 'L', 'tca': 'S', 'taa': '*stop*', 'tga': '*stop*',
             'ttg': 'L', 'tcg': 'S', 'tag': '*stop*', 'tgg': 'W',
             'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
             'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
             'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
             'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
             'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
             'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
             'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
             'atg': '*start*', 'acg': 'T', 'aag': 'K', 'agg': 'R',
             'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
             'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
             'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
             'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
        }
# Amino Acid(Aacid)

def genprotein ():
    cdnaseq = Entry.get()
    Aacid = []
    cdnaseq = cdnaseq.lower()
    for i in xrange(0, len(cdnaseq), 3):
        codon = cdnaseq[i:i + 3]
        if codon in code:
            Aacid.append(code[codon])
        proteinseq = ''.join(Aacid)
        ProteinSequence['text'] = proteinseq

def ClearSearch ():
    Entry.delete(0, END)

root = Tk()

OriginalEntry = Frame(root)
OriginalEntry ['bg'] = 'light blue'
OriginalEntry.place(x=100, y=100, width= 400)

EntryLabel = Label(OriginalEntry)
EntryLabel ['text']= 'Enter CDNA sequence'
EntryLabel.pack()

Entry = Entry (OriginalEntry)
Entry.pack(fill = BOTH)




ActionFrame = Frame(root)
ActionFrame ['bg'] = 'yellow'

generate = Button (ActionFrame)
generate ["text"] = "Generate"
generate ['command']= genprotein
generate.pack()

clear = Button (ActionFrame)
clear ['text'] = 'Entry new sequence'
clear ['command'] = ClearSearch
clear.pack(side = BOTTOM)





ResultFrame = Frame(root)
ResultFrame ['bg'] = 'white'

scrollbar = Scrollbar (ResultFrame)
scrollbar.pack( side = RIGHT, fill=Y )



ResultFrameLabel = Label (ResultFrame)
ResultFrameLabel ['text']= 'The protein sequence is:'
ResultFrameLabel.pack(side = LEFT)

ProteinSequence = Label(ResultFrame)
ProteinSequence.pack( side = RIGHT,  anchor = E)

OriginalEntry.pack(side = LEFT, expand=YES, fill=BOTH )
ResultFrame.pack(side=RIGHT, expand=YES, fill=BOTH)
ActionFrame.pack(side = TOP, expand= YES, fill=BOTH )


mainloop()



'''