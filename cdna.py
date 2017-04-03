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
from tkinter import *

root = Tkt()
'''

from Tkinter import *



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

def genprotein (cdnaseq):
    Aacid = []
    for i in xrange(0, len(cdnaseq), 3):
        codon = cdnaseq[i:i + 3]
        if codon in code:
            Aacid.append(code[codon])
        proteinseq = ''.join(Aacid)
    return proteinseq


root = Tk()

generate = Button (root)
generate ["text"] = "Generate"
generate ["command"] = generate

generate.pack()

mainloop()