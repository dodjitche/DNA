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

sql = CREATE TABLE IF NOT EXISTS Person
                (PID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(100),
                HEIGHT INT)

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








#
#
#
#
#
# from Tkinter import *
#
# # replaced  ATG (start codon): Met(M) by Start codon
#
# code = {     'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
#              'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
#              'tta': 'L', 'tca': 'S', 'taa': '*stop*', 'tga': '*stop*',
#              'ttg': 'L', 'tcg': 'S', 'tag': '*stop*', 'tgg': 'W',
#              'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
#              'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
#              'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
#              'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
#              'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
#              'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
#              'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
#              'atg': '*start*', 'acg': 'T', 'aag': 'K', 'agg': 'R',
#              'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
#              'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
#              'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
#              'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
#         }
# # Amino Acid(Aacid)
#
# def genprotein ():
#     cdnaseq = Entry.get()
#     Aacid = []
#     cdnaseq = cdnaseq.lower()
#     for i in xrange(0, len(cdnaseq), 3):
#         codon = cdnaseq[i:i + 3]
#         if codon in code:
#             Aacid.append(code[codon])
#         proteinseq = ''.join(Aacid)
#         # proteinseq = '\n'.join([proteinseq[i:i+100] for i in range(0,len(proteinseq), 100)])
#         # ProteinSequence['text'] = proteinseq
#         # next line : important
#         proteinseq = '*stop*\n'.join(proteinseq.split('*stop*'))
#         ProteinSequence.insert(END, proteinseq)
#     # ProteinSequence.configure(state="disabled")  # disable imput
#
#
# def ClearSearch ():
#     Entry.delete(0, END)
#
# root = Tk()
#
# OriginalEntry = Frame(root)
# OriginalEntry ['bg'] = 'light blue'
# OriginalEntry.place(x=100, y=100, width= 400)
#
# EntryLabel = Label(OriginalEntry)
# EntryLabel ['text']= 'Enter CDNA sequence'
# EntryLabel.pack()
#
# Entry = Entry (OriginalEntry)
# Entry.pack(fill = BOTH)
#
#
#
#
# ActionFrame = Frame(root)
# ActionFrame ['bg'] = 'yellow'
#
# generate = Button (ActionFrame)
# generate ["text"] = "Generate"
# generate ['command']= genprotein
# generate.pack()
#
# clear = Button (ActionFrame)
# clear ['text'] = 'Entry new sequence'
# clear ['command'] = ClearSearch
# clear.pack(side = BOTTOM)
#
#
#
#
# # ResultFrameLabel = Label (ResultFrame)
# # ResultFrameLabel ['text']= 'The protein sequence is:'
# # ResultFrameLabel.pack(side = LEFT)
#
#
#
#
#
#
#
#
#
# ResultFrame = Frame(root, width=600, height=600)
# ResultFrame.pack( side = RIGHT,  anchor = E)
# ResultFrame.grid_propagate(False)
# ResultFrame.grid_rowconfigure(0, weight=1)
# ResultFrame.grid_columnconfigure(0, weight=1)
#
# # create a Text widget
# ProteinSequence = Text(ResultFrame, borderwidth=3, relief="sunken")
# ProteinSequence.config(font=("consolas", 12), undo=True, wrap='word')
# ProteinSequence.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
#
# # create a Scrollbar and associate it with txt
# scrollb = Scrollbar(ResultFrame, command=ProteinSequence.yview)
# scrollb.grid(row=0, column=1, sticky='nsew')
# ProteinSequence['yscrollcommand'] = scrollb.set
#
#
#
#
#
# '''
# ProteinSequence = Label(ResultFrame)
# ProteinSequence.pack( side = RIGHT,  anchor = E)
# '''
#
#
# '''ProteinSequence = Label(ResultFrame, anchor = W, wraplengt = 700)
# # w = Scrollbar(ResultFrame)
# ProteinSequence.pack( side = TOP)
#
# '''
#
#
# OriginalEntry.pack(side = LEFT, expand=YES, fill=BOTH )
# # ResultFrame.pack(side=RIGHT, expand=YES, fill=BOTH)
# ActionFrame.pack(side = TOP, expand= YES, fill=BOTH )
#
#
# mainloop()
#
#
#
#
#
#
#
# '''
# import Tkinter as tki # Tkinter -> tkinter in Python3
#
# class App(object):
#
#     def __init__(self):
#         self.root = tki.Tk()
#
#     # create a Frame for the Text and Scrollbar
#         txt_frm = tki.Frame(self.root, width=600, height=600)
#         txt_frm.pack(fill="both", expand=True)
#         # ensure a consistent GUI size
#         txt_frm.grid_propagate(False)
#         # implement stretchability
#         txt_frm.grid_rowconfigure(0, weight=1)
#         txt_frm.grid_columnconfigure(0, weight=1)
#
#     # create a Text widget
#         self.txt = tki.Text(txt_frm, borderwidth=3, relief="sunken")
#         self.txt.config(font=("consolas", 12), undo=True, wrap='word')
#         self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
#
#     # create a Scrollbar and associate it with txt
#         scrollb = tki.Scrollbar(txt_frm, command=self.txt.yview)
#         scrollb.grid(row=0, column=1, sticky='nsew')
#         self.txt['yscrollcommand'] = scrollb.set
#
# app = App()
# app.root.mainloop()
# '''
#
#
#
#
#
# from Tkinter import *
#
# master = Tk()
#
# listbox = Listbox(master)
# listbox.pack()
#
# listbox.insert(END, "a list entry")
#
# for item in ["one", "two", "three", "four"]:
#     listbox.insert(END, item)
#
# mainloop()




#
# from tkinter import *
#
# def func1():
#     print("in func1")
#
# def func2():
#     print("in func2")
#
# def selection():
#     try:
#         dictionary[listbox.selection_get()]()
#     except:
#         pass
#
# root = Tk()
#
# frame = Frame(root)
# frame.pack()
#
# dictionary = {"1":func1, "2":func2}
#
# items = StringVar(value=tuple(sorted(dictionary.keys())))
#
# listbox = Listbox(frame, listvariable=items, width=15, height=5)
# listbox.grid(column=0, row=2, rowspan=6, sticky=("n", "w", "e", "s"))
# listbox.focus()
#
# selectButton = Button(frame, text='Select', underline = 0, command=selection)
# selectButton.grid(column=2, row=4, sticky="e", padx=50, pady=50)
#
# root.bind('<Double-1>', lambda x: selectButton.invoke())
#
# root.mainloop()














#
# import sqlite3
#
# conn = sqlite3.connect("mydatabase.db")
# # conn.row_factory = sqlite3.Row
# cursor = conn.cursor()
#
# sql = "SELECT * FROM albums WHERE artist=?"
# cursor.execute(sql, [("Red")])
# print cursor.fetchall()  # or use fetchone()
#
# print "\nHere's a listing of all the records in the table:\n"
# for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
#     print row
#
# print "\nResults from a LIKE query:\n"
# sql = """
# SELECT * FROM albums
# WHERE title LIKE 'The%'"""
# cursor.execute(sql)
# print cursor.fetchall()


#
# from Tkinter import *
#
# root = Tk()
#
# # replaced  ATG (start codon): Met(M) by Start codon
#
# code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
#         'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
#         'tta': 'L', 'tca': 'S', 'taa': '*stop*', 'tga': '*stop*',
#         'ttg': 'L', 'tcg': 'S', 'tag': '*stop*', 'tgg': 'W',
#         'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
#         'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
#         'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
#         'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
#         'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
#         'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
#         'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
#         'atg': '*start*', 'acg': 'T', 'aag': 'K', 'agg': 'R',
#         'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
#         'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
#         'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
#         'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
#         }
# # Amino Acid(Aacid)
#
# import sqlite3
#
# conn = sqlite3.connect('Allsequences.db')
# c = conn.cursor()
#
#
# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS PStable (DNAname TEXT, DNASequence TEXT, AminoAcidSequence TEXT) ')
#
#
# create_table()
#
#
# def genprotein():
#     global cdnaseq
#     global proteinseqconv
#     cdnaseq = SequenceEntry.get()
#     Aacid = []
#     cdnaseq = cdnaseq.lower()
#     # Activating the text result
#     ProteinSequence.config(state=NORMAL)
#     for i in xrange(0, len(cdnaseq), 3):
#         codon = cdnaseq[i:i + 3]
#         if codon in code:
#             Aacid.append(code[codon])
#         proteinseq = ''.join(Aacid)
#
#         # proteinseq = '\n'.join([proteinseq[i:i+100] for i in range(0,len(proteinseq), 100)])
#         # ProteinSequence['text'] = proteinseq
#         # next line : important
#         proteinseq = '*stop*\n'.join(proteinseq.split('*stop*'))
#         ProteinSequence.insert(END, proteinseq)
#     # desactivating the text result
#
#     # ProteinSequence.configure(state="disabled")  # disable imput
#     proteinseqconv = '*stop*'.join(proteinseq.split('*stop*\n'))
#     # print(proteinseqconv)
#     cdnaseq = ''.join(cdnaseq.split())
#     ProteinSequence.config(state=DISABLED)
#
#
# def SaveData():
#     global title
#     ProteinSequence.config(state=NORMAL)
#     cdnaseq = SequenceEntry.get()
#     title = titleEntry.get()
#     getVAR = [title, cdnaseq, proteinseqconv]
#     # MessageBox = ''
#     # if title== '':
#     #     tkMessageBox.showinfo('test 1','test 2')
#     # print ('coding sequence', cdnaseq)
#     # print ('protein sequence' , proteinseq)
#     c.execute("INSERT INTO PStable VALUES (?,?,?)", getVAR)
#     conn.commit()
#     ProteinSequence.config(state=DISABLED)
#     # c.close()
#     # conn.close()
#
#     #         Listbox
#
#     # listbox.insert(END, title)
#
#
# # Delete Entry and Result
# def ClearSearch():
#     ProteinSequence.config(state=NORMAL)
#     SequenceEntry.delete(0, END)
#     titleEntry.delete(0, END)
#     ProteinSequence.delete("1.0", END)
#     ProteinSequence.config(state=DISABLED)
#
#
# # ****************************************
#
# OriginalEntry = Frame(root)
# OriginalEntry['bg'] = 'light blue'
# OriginalEntry.place(x=100, y=100, width=400)
#
# EntryLabel = Label(OriginalEntry)
# EntryLabel['text'] = 'Enter CDNA sequence'
# EntryLabel.pack(fill=X)
#
# SequenceEntry = Entry(OriginalEntry)
# SequenceEntry.pack(fill=X)
#
# titleEntry = Entry(OriginalEntry)
# titleEntry.pack(fill=X, side=BOTTOM)
#
# titleLab = Label(OriginalEntry)
# titleLab['text'] = 'Enter the name of the sequence'
# titleLab.pack(fill=X, side=BOTTOM)
#
# # titleEntry.place(relx=.5, rely=.5, anchor="center")
#
# # ****************************************
#
#
# ActionFrame = Frame(root)
# ActionFrame['bg'] = 'yellow'
#
#
# # Quiting the UI
# def FQuit():
#     global root
#     root.destroy()
#
#
# quit = Button(ActionFrame, text="Quit", bg='red', fg='red', command=FQuit)
# quit.pack(fill=X, side=BOTTOM)
#
# generate = Button(ActionFrame, bg="white")
# generate["text"] = "Generate"
# generate['command'] = genprotein
# generate.pack(fill=X)
#
# Save = Button(ActionFrame)
# Save['text'] = 'Save'
# Save['command'] = SaveData
# Save.pack(fill=X, side=BOTTOM)
#
#
# # #########
#
# def RefreshList():
#     for row in c.execute("SELECT DNAname FROM PStable"):
#         listbox.insert(END, row)
#
#
# Refresh = Button(ActionFrame)
# Refresh['text'] = 'Refresh the List'
# Refresh['command'] = RefreshList
# Refresh.pack(fill=X, side=BOTTOM)
#
# clear = Button(ActionFrame)
# clear['text'] = 'Entry new sequence'
# clear['command'] = ClearSearch
# clear.pack(fill=X, side=TOP)
#
# # ResultFrameLabel = Label (ResultFrame)
# # ResultFrameLabel ['text']= 'The protein sequence is:'
# # ResultFrameLabel.pack(side = LEFT)
#
#
# # ****************************************
#
# ResultFrame = Frame(root, width=300, height=300)
# ResultFrame.pack(side=RIGHT, anchor=E)
# ResultFrame.grid_propagate(False)
# ResultFrame.grid_rowconfigure(0, weight=1)
# ResultFrame.grid_columnconfigure(0, weight=1)

# create a Text widget
ProteinSequence = Text(ResultFrame, borderwidth=3, relief="sunken")
ProteinSequence.config(font=("consolas", 12), undo=True, wrap='word')
ProteinSequence.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

# ProteinSequence.config(state=DISABLED)
#
# create a Scrollbar and associate it with txt
scrollb = Scrollbar(ResultFrame, command=ProteinSequence.yview)
scrollb.grid(row=0, column=1, sticky='nsew')
ProteinSequence['yscrollcommand'] = scrollb.set

# # ****************************************
#
#
StoredSeq = Frame(root, width=100, height=100)
StoredSeq['bg'] = 'green'
StoredSeq.pack(fill=X, side=BOTTOM)

#  the list scrollbar
scrollbar = Scrollbar(StoredSeq, orient=VERTICAL)
listbox = Listbox(StoredSeq, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
#
#
# # List button
#
# # def Dclick():
# #     print ('works!!!!!')
# #
# # doubleclick = Button (ActionFrame)
# # doubleclick ['text'] = 'Double click'
# # doubleclick['command'] = Dclick
# # doubleclick.pack(side =BOTTOM)
# #
# # listbox.bind('<Double-1>', lambda x: doubleclick.invoke() )
#
#
#
# def bind(widget, event):
#     def decorator(func):
#         widget.bind(event, func)
#         return func
#
#     return decorator
#
#
# if __name__ == '__main__':
#     frame = Frame()
#     frame.master.title("The Data")
#     frame.pack()
#
# doubleclick = Button(ActionFrame)
# doubleclick['text'] = 'Double click'
# doubleclick['command'] = Dclick
# doubleclick.pack(side=BOTTOM)
#
# listbox.bind('<Double-1>', lambda x: doubleclick.invoke())
#
# '''
# ProteinSequence = Label(ResultFrame)
# ProteinSequence.pack( side = RIGHT,  anchor = E)
# '''
#
# '''ProteinSequence = Label(ResultFrame, anchor = W, wraplengt = 700)
# # w = Scrollbar(ResultFrame)
# ProteinSequence.pack( side = TOP)
#
# '''
#
# OriginalEntry.pack(side=LEFT, expand=YES, fill=BOTH)
# # ResultFrame.pack(side=RIGHT, expand=YES, fill=BOTH)
# ActionFrame.pack(side=LEFT, expand=YES, fill=BOTH)
#
# mainloop()
#
#
#











# trying sqlite3

# import sqlite3
#
# conn = sqlite3.connect ('Allsequences.db')
# c = conn.cursor()
#
# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS PStable (DNAname TEXT, DNASequence TEXT, AminoAcidSequence TEXT) ')
#
# # def table_values ():
# #     c.execute("INSERT INTO PStable VALUES ('ewweewdew', 'cdnaseq', 'ProteinSequence' ) ")
# #     conn.commit()
# #     c.close()
# #     conn.close()
#
# create_table()
# table_values ()










# from Tkinter import *
#
# def bind(widget, event):
#     """Write the body of this function"""
#
# if __name__ == '__main__':
#     frame = Frame()
#     frame.master.title("Event binding with decorators")
#     frame.pack()
#
#     lb = Listbox(frame, name='lb')
#     for s in ['One', 'Two', 'Three', 'Four']:
#         lb.insert(END, s)
#     lb.pack()
#
#     bind(lb, '<<ListboxSelect>>')
#     def onselect(evt):
#         w = evt.widget
#         index = int(w.curselection()[0])
#         value = w.get(index)
#         print 'You selected item %d: "%s"' % (index, value)
#
#     frame.mainloop()






from Tkinter import *


def bind(widget, event):
    def decorator(func):
        widget.bind(event, func)
        return func

    return decorator


if __name__ == '__main__':
    frame = Frame()
    frame.master.title("Event binding with decorators")
    frame.pack()
    #         the lisbox

    lb = Listbox(frame, name='lb')
    for s in ['One', 'Two', 'Three', 'Four']:
        lb.insert(END, s)
    lb.pack()


    @bind(lb, '<<ListboxSelect>>')
    def onselect(evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print 'You selected item %d: "%s"' % (index, value)


    frame.mainloop()




#
# from Tkinter import *
# import Tkinter
#
# def immediately(e):
#     print Lb1.curselection()
#
#
# top = Tk()
#
# Lb1 = Listbox(top)
# Lb1.insert(1, "Python")
# Lb1.insert(2, "Perl")
# Lb1.insert(3, "C")
# Lb1.insert(4, "PHP")
# Lb1.insert(5, "JSP")
# Lb1.insert(6, "Ruby")
#
# Lb1.pack()
#
#
# Lb1.bind('<<ListboxSelect>>', immediately)
# top.mainloop()

























StoredSeq = Frame(root, width=200, height=200)
StoredSeq['bg'] = 'green'
StoredSeq.pack(fill=X, side=BOTTOM)

showdataframe = Frame(StoredSeq, width=300, height=300)
showdataframe.pack(side=RIGHT, anchor=E)
showdataframe.grid_propagate(False)
showdataframe.grid_rowconfigure(0, weight=1)
showdataframe.grid_columnconfigure(0, weight=1)


# create a Text widget
showdata = Text(showdataframe, borderwidth=3, relief="sunken")
showdata.config(font=("consolas", 12), undo=True, wrap='word')
showdata.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

# create a Scrollbar and associate it with txt
scrollb = Scrollbar(showdataframe, command=showdata.yview)
scrollb.grid(row=0, column=1, sticky='nsew')
showdata['yscrollcommand'] = scrollb.set

# ---------------------------------
#
# showAAdataframe = Frame(StoredSeq, width=200, height=200)
# showAAdataframe.pack(side=BOTTOM, anchor=E)
# showAAdataframe.grid_propagate(False)
# showAAdataframe.grid_rowconfigure(0, weight=1)
# showAAdataframe.grid_columnconfigure(0, weight=1)
#
# # create a Text widget for the Amino acid sequence
# showAAdata = Text(showAAdataframe, borderwidth=3, relief="sunken")
# showAAdata.config(font=("consolas", 12), undo=True, wrap='word')
# showAAdata.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
#
#
#
# # create a Scrollbar and associate it with txt
# scrollb = Scrollbar(showAAdataframe, command=showAAdata.yview)
# scrollb.grid(row=0, column=1, sticky='nsew')
# showAAdata['yscrollcommand'] = scrollb.set
#


def bind(widget, event):
    def decorator(func):
        widget.bind(event, func)
        return func
    return decorator

if __name__ == '__main__':
    StoredSeq.master.title("Converter")
    StoredSeq.pack(fill=X, side=BOTTOM)

    lb = Listbox(StoredSeq, name='lb')
    for row in c.execute("SELECT DNAname FROM PStable"):
        lb.insert(END, row)
    lb.pack(side = LEFT)



    @bind(lb, '<<ListboxSelect>>')
    def onselect(evt):
        showdata.delete("1.0", END)
        gg = []
        global val
        w = evt.widget
        index = int(w.curselection()[0])
        val = w.get(index)
        val = ''.join(val)
        val = unicodedata.normalize('NFKD', val).encode('ascii','ignore')
        c.execute("SELECT AminoAcidSequence FROM PStable  WHERE DNAname = '%s'" % val)
        for line in c.fetchmany():
            gg += line
        gg = ''.join(gg)
        showdata.insert(END, gg)









        # print 'You selected item %d: "%s"' % (index, value)


#

# doubleclick = Button (ActionFrame)
# doubleclick ['text'] = 'Double click'
# doubleclick['command'] = Dclick
# doubleclick.pack(side =BOTTOM)

# listbox.bind('<Double-1>', lambda x: doubleclick.invoke() )



'''
ProteinSequence = Label(ResultFrame)
ProteinSequence.pack( side = RIGHT,  anchor = E)
'''

'''ProteinSequence = Label(ResultFrame, anchor = W, wraplengt = 700)
# w = Scrollbar(ResultFrame)
ProteinSequence.pack( side = TOP)

'''

OriginalEntry.pack(side=LEFT, expand=YES, fill=BOTH)
# ResultFrame.pack(side=RIGHT, expand=YES, fill=BOTH)
ActionFrame.pack(side=LEFT, expand=YES, fill=BOTH)

mainloop()






















