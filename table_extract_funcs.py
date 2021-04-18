from camelot import read_pdf
from pandas import concat
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from ntpath import split, basename
from os import getcwd

def path_leaf(path):
    head, tail = split(path)
    return head, (tail or basename(head))

def formatString(s):
    original = s
    s = s.replace('.', "")
    s = s.replace(',', ".")

    l = []

    for t in s.split():
        try:
            l.append(float(t))
        except:
            continue
    
    if(len(l) == 0):
        return original

    temp = str(l[0])
    return (temp.replace('.', ","))

def select_file(entry):
    filetypes = (
        ('PDF Files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open file',
        initialdir='/',
        filetypes=filetypes)

    entry.delete(0, 'end')
    entry.insert('end', filename)

def extract_tables(fileEntry, pageEntry, shouldFormat, formatEntry):
    fileName = fileEntry.get()
    pageNums = pageEntry.get().split(',')

    for ranges in pageNums:
        tables = read_pdf(fileName, pages=ranges)

        print("Total tables extracted:", tables.n)

        frames = []
        for table in tables:
            frames.append(table.df)
            print(table.parsing_report)

        result = concat(frames)

        nColumns = formatEntry.get()
        if((shouldFormat) and (nColumns != "")):
            col = [int(s) for s in formatEntry.get().split(',')]
            for c in col:
                result[c-1] = result[c-1].apply(formatString)

        head, tail = path_leaf(fileName)
        newName = getcwd() + "\extracted_tables\\" + tail[:-4] + "_" + ranges + "_tables.csv"
        result.to_csv(newName)
        mb.showinfo(title="Extraction succeeded", message="Table was extracted successfully at " + newName)

def toggleEntry(entry):
    if(entry['state'] == 'normal'):
        print("Desabling entry")
        entry.config(state='disabled')
    else: 
        print("Enabling entry")
        entry.config(state='normal')


