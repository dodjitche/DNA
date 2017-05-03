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

#lower case of  the sequence of cdna
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



#incomplete definition of the file
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

#***code***
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










#tkinter, practice
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
        # proteinseq = '\n'.join([proteinseq[i:i+100] for i in range(0,len(proteinseq), 100)])
        proteinseq = '*stop*\n'.join(proteinseq.split('*stop*'))
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
ActionFrame.place(width= 800)


generate = Button (ActionFrame)
generate ["text"] = "Generate"
generate ['command']= genprotein
generate.pack()





clear = Button (ActionFrame)
clear ['text'] = 'Entry new sequence'
clear ['command'] = ClearSearch
clear.pack(side = BOTTOM)









ResultFrame = Frame(root)
ResultFrame ['bg'] = 'green'



ResultFrameLabel = Label (ResultFrame)
ResultFrameLabel ['text']= 'The protein sequence is:'
ResultFrameLabel.pack(side = TOP, anchor = W)

ProteinSequence = Label(ResultFrame, anchor = W, wraplengt = 700)
# w = Scrollbar(ResultFrame)
ProteinSequence.pack( side = TOP)



OriginalEntry.pack(side = LEFT, expand=YES, fill=BOTH )
ResultFrame.pack(side=RIGHT, expand=YES, fill=BOTH)
ActionFrame.pack(side = TOP, expand= YES, fill=BOTH )


mainloop()



#trying sqlite3
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

'''
import sqlite3

conn = sqlite3.connect ('Allsequences.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS PStable (DNAname TEXT, DNASequence TEXT, AminoAcidSequence TEXT) ')

def table_values ():
    c.execute("INSERT INTO PStable VALUES ('ewweewdew', cdnaseq, ProteinSequence ) ")
    conn.commit()
    c.close()
    conn.close()

create_table()
table_values ()

'''