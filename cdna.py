# Precious!
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

# lower case of  the sequence of cdna
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

# incomplete definition of the file
'''
def lowerdna( file):
    filename = 'file'
    book = open (filename)
    lines = book.readlines()
    book.close()

    lines = lines[8:]
    cleantext = {}
    for line in lines:
        line = line[:-2]
        if 'f' in line:
            line = line [14:]
        line = line.lower()
        line = cleantext
    cleantext += line

    return cleantext

for line in lowerdna(cdnatext.txt):
    print (line)
'''

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

# ***code***
'''
filename = 'cdnatext.txt'
book = open (filename)
lines = book.readlines()
book.close()

lines = lines[8:]
cdnaseq = []
for line in lines:
    line = line[:-2]
    if 'f' in line:
        line = line [14:]
    line = line.lower()
    cdnaseq.append(line)
cdnaseq = ''.join(cdnaseq)

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
Aacid = []

for i in xrange(0,len(cdnaseq), 3):
    codon = cdnaseq [i:i+3] 
    if codon in code:
        Aacid.append(code[codon])
    proteinseq = ''.join(Aacid)
print (proteinseq)
'''

# tkinter, practice
'''

#  function to open a file
def openfile():
    with open('cdnatext.txt', 'r') as f:
        lines= f.readlines()

        lines = lines[8:]
        cdnaseq = []
        for line in lines:
            line = line[:-2]
            if 'f' in line:
                line = line[14:]
            line = line.lower()
            cdnaseq.append(line)
        cdnaseq = ''.join(cdnaseq)
    return cdnaseq



# Amino Acid(Aacid)

def genprotein (cdnaseq):
    Aacid = []
    for i in xrange(0, len(cdnaseq), 3):
        codon = cdnaseq[i:i + 3]
        if codon in code:
            Aacid.append(code[codon])
        proteinseq = ''.join(Aacid)
    return proteinseq

#*****
generate = Button (ActionFrame)
generate ["text"] = "Generate"
generate ["command"] = genprotein(openfile())
generate.pack()





ProteinSequence['text'] = 'The sequence is {0}'.format(proteinseq)

'''

from Tkinter import *
import unicodedata
root = Tk()

# replaced  ATG (start codon): Met(M) by Start codon

code = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
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

import sqlite3

conn = sqlite3.connect('Allsequences.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS PStable (DNAname TEXT, DNASequence TEXT, AminoAcidSequence TEXT) ')

create_table()




def genprotein():
    global cdnaseq
    global proteinseqconv
    cdnaseq = SequenceEntry.get()
    Aacid = []
    cdnaseq = cdnaseq.lower()
    # Activating the text result
    ProteinSequence.config(state=NORMAL)
    for i in xrange(0, len(cdnaseq), 3):
        codon = cdnaseq[i:i + 3]
        if codon in code:
            Aacid.append(code[codon])
    proteinseq = ''.join(Aacid)
    proteinseqconv = proteinseq
        # proteinseq = '\n'.join([proteinseq[i:i+100] for i in range(0,len(proteinseq), 100)])
        # ProteinSequence['text'] = proteinseq
        # next line : important
        proteinseq = '*stop*\n'.join(proteinseq.split('*stop*'))
    proteinseq = '*stop*\n'.join(proteinseq.split('*stop*'))
    ProteinSequence.insert(END, proteinseq)
        # proteinseqconv = '*stop*'.join(proteinseq.split('*stop*\n'))
    # desactivating the text result

    # ProteinSequence.configure(state="disabled")  # disable imput

    print(proteinseqconv)
    cdnaseq = ''.join(cdnaseq.split())
    ProteinSequence.config(state=DISABLED)








# Delete Entry and Result
def ClearSearch ():
    ProteinSequence.config(state=NORMAL)
    SequenceEntry.delete(0, END)
    titleEntry.delete(0,END)
    ProteinSequence.delete("1.0", END)
    ProteinSequence.config(state=DISABLED)
# delete data
# def ClearData ():
#     showdata.config(state=NORMAL)
#     showdata.delete("1.0", END)


# ****************************************

OriginalEntry = Frame(root)
OriginalEntry['bg'] = 'light blue'
OriginalEntry.place(x=100, y=100, width=400)

EntryLabel = Label(OriginalEntry)
EntryLabel['text'] = 'Enter CDNA sequence'
EntryLabel.pack(fill= X)

SequenceEntry = Entry(OriginalEntry)
SequenceEntry.pack(fill= X)


titleEntry = Entry (OriginalEntry)
titleEntry.pack(fill = X, side = BOTTOM)

titleLab = Label (OriginalEntry)
titleLab['text']= 'Enter the name of the sequence'
titleLab.pack(fill = X, side = BOTTOM)

# titleEntry.place(relx=.5, rely=.5, anchor="center")

# ****************************************


ActionFrame = Frame(root)
ActionFrame['bg'] = 'yellow'

# Quiting the UI
def FQuit():
    global root
    root.destroy()
quit = Button(ActionFrame, text="Quit",bg = 'red', fg = 'red', command=FQuit)
quit.pack(fill = X, side = BOTTOM)



def info_window():
    frame1= Toplevel(root, width=100, height=25)

    def SaveData():
        global title
        ProteinSequence.config(state=NORMAL)
        cdnaseq = SequenceEntry.get()
        title = titleEntry.get()
        getVAR = [title, cdnaseq, proteinseqconv]
        # MessageBox = ''
        # if title== '':
        #     tkMessageBox.showinfo('test 1','test 2')
        # print ('coding sequence', cdnaseq)
        # print ('protein sequence' , proteinseq)
        c.execute("INSERT INTO PStable VALUES (?,?,?)", getVAR)
        conn.commit()
        ProteinSequence.config(state=DISABLED)
        # c.close()
        # conn.close()

        #         Listbox

        # listbox.insert(END, title)
    SaveData()
    show1 = Label (frame1, text = "The sequences have been stored", width = 50, height= 12).pack()



generate = Button(ActionFrame, bg ="white" )
generate["text"] = "Generate"
generate['command'] = genprotein
generate.pack(fill = X )

Save = Button (ActionFrame)
Save ['text'] = 'Save'
# Save['command'] = SaveData
Save['command'] = info_window
Save.pack(fill = X, side = BOTTOM)


def info_window2():
    frame2= Toplevel(root)

    showdataframe = Frame(frame2, width=300, height=300)
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

    def bind(widget, event):
        def decorator(func):
            widget.bind(event, func)
            return func

        return decorator

    StoredSeq = Frame(frame2)
    StoredSeq['bg'] = 'green'
    StoredSeq.pack(fill=X, side=LEFT)

    if __name__ == '__main__':
        StoredSeq.master.title("Data")
        StoredSeq.pack(fill=X)

        # scrollbar = Scrollbar(StoredSeq, orient=VERTICAL)
        # listbox = Listbox(StoredSeq, yscrollcommand=scrollbar.set)
        # scrollbar.config(command=listbox.yview)
        # scrollbar.pack(side=RIGHT, fill=Y)
        # listbox.pack(side=LEFT, fill=BOTH, expand=1)

        scrollbar = Scrollbar(StoredSeq, orient=VERTICAL)
        lb = Listbox(StoredSeq, name='lb', yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        lb.pack(side=LEFT, fill=BOTH, expand=1)

        for row in c.execute("SELECT DNAname FROM PStable"):
            lb.insert(END, row)
        lb.pack(side=LEFT)

        # lb = Listbox(StoredSeq, name='lb')
        # for row in c.execute("SELECT DNAname FROM PStable"):
        #     lb.insert(END, row)
        # lb.pack(side=LEFT)

        @bind(lb, '<<ListboxSelect>>')
        def onselect(evt):
            showdata.delete("1.0", END)
            gg = []
            global val
            w = evt.widget
            index = int(w.curselection()[0])
            val = w.get(index)
            val = ''.join(val)
            val = unicodedata.normalize('NFKD', val).encode('ascii', 'ignore')
            c.execute("SELECT AminoAcidSequence FROM PStable  WHERE DNAname = '%s'" % val)
            for line in c.fetchmany():
                gg += line
            gg = ''.join(gg)
            showdata.insert(END, gg)





view = Button (ActionFrame)
view ['text'] = 'View stored sequences'
view['command'] = info_window2
view.pack(fill = X, side = BOTTOM)



# #########


# 99999999999999999999999

# def RefreshList():
#     for row in c.execute("SELECT DNAname FROM PStable"):
#         listbox.insert(END, row)
#
# Refresh = Button (ActionFrame)
# Refresh ['text'] = 'Refresh the List'
# Refresh['command'] = RefreshList
# Refresh.pack(fill = X, side = BOTTOM)

# 99999999999999999999999


clear = Button(ActionFrame)
clear['text'] = 'Entry new sequence'
clear['command'] = ClearSearch
clear.pack(fill = X, side= TOP)

# cleandata = Button(ActionFrame)
# cleandata['text'] = 'clear data'
# cleandata['command'] = ClearData
# cleandata.pack(fill = X, side= BOTTOM)
# ResultFrameLabel = Label (ResultFrame)
# ResultFrameLabel ['text']= 'The protein sequence is:'
# ResultFrameLabel.pack(side = LEFT)


# ****************************************

ResultFrame = Frame(root, width=500, height=500)
ResultFrame.pack(side=RIGHT, anchor=E)
ResultFrame.grid_propagate(False)
ResultFrame.grid_rowconfigure(0, weight=1)
ResultFrame.grid_columnconfigure(0, weight=1)

# create a Text widget
ProteinSequence = Text(ResultFrame, borderwidth=3, relief="sunken")
ProteinSequence.config(font=("consolas", 12), undo=True, wrap='word')
ProteinSequence.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)


ProteinSequence.config(state=DISABLED)

# create a Scrollbar and associate it with txt
scrollb = Scrollbar(ResultFrame, command=ProteinSequence.yview)
scrollb.grid(row=0, column=1, sticky='nsew')
ProteinSequence['yscrollcommand'] = scrollb.set


# ****************************************




#             #  the list scrollbar
# scrollbar = Scrollbar(StoredSeq, orient=VERTICAL)
# listbox = Listbox(StoredSeq, yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# listbox.pack(side=LEFT, fill=BOTH, expand=1)


             # List button

# def Dclick():
#     print ('works!!!!!')
#
# doubleclick = Button (ActionFrame)
# doubleclick ['text'] = 'Double click'
# doubleclick['command'] = Dclick
# doubleclick.pack(side =BOTTOM)
#
# listbox.bind('<Double-1>', lambda x: doubleclick.invoke() )





# StoredSeq = Frame(root, width=200, height=200)
# StoredSeq['bg'] = 'green'
# StoredSeq.pack(fill=X, side=BOTTOM)


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










'''
import sqlite3

conn = sqlite3.connect ('tutorial.db')
c = conn.cursor ()

def create_table ():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot (unix REAL, datestamp TEXT, keyword TEXT, value REAL )')



def data_entry():
    c.execute ("INSERT INTO stuffToPlot VALUES (23, '2016-01-01', 'Python', 5) ")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
'''
