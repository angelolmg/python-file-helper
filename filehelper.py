import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import ntpath

filesToMerge = []

def path_leaf(path):
    head, tail = ntpath.split(path)
    '''
    print("path " + path)
    print("head " + head)
    print("tail " + tail)
    print("basehead " + ntpath.basename(head))
    '''
    return head, (tail or ntpath.basename(head))

def merge_pdf(fileList):

    if(len(fileList) < 2):
        return

    merger = PdfFileMerger()
    newName = ""

    for pdf in fileList:
        merger.append(pdf)
        h, t = path_leaf(pdf)
        newName += t[:-4] + "&"

    newName += ".pdf"

    merger.write(newName)
    merger.close()

def split_pdf(file, begin, end):
    inputpdf = PdfFileReader(open(file, "rb"))

    print("Num. de páginas: " + str(inputpdf.numPages))

    if(begin < 1 or end > inputpdf.numPages or begin > end):
        print("Deu ruim com o numero de páginas!")
        return

    output = PdfFileWriter()
    for i in range(begin-1, end):
        output.addPage(inputpdf.getPage(i))

    head, tail = path_leaf(file)
    newfilename = head + "/" + tail[:-4] + "_" + str(begin) + "-" + str(end) + ".pdf"
    with open(newfilename, "wb") as outputStream:
        output.write(outputStream)
    
    return newfilename

# create the root window
root = tk.Tk()
root.title('File Helper')
root.resizable(False, False)
root.geometry('500x250')

def select_files():
    filetypes = (
        ('PDF Files', '*.pdf'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    entry.delete(0, 'end')
    for name in filenames:
        entry.insert('end', name + '|')

def print_filenames():
    fileList = entry.get().split('|')[:-1]
    begin = spMin.get()
    end = spMax.get()

    fileListSplitMerge = []

    if(split.get() == 1):
        for name in fileList:
            fileListSplitMerge.append(split_pdf(name, int(begin), int(end)))
        if(merge.get() == 1):
            merge_pdf(fileListSplitMerge)
    elif(merge.get() == 1):
        merge_pdf(fileList)

        
# open button
open_button = ttk.Button(
    root,
    text='Open Files',
    command=select_files
)

action_button = ttk.Button(
    root,
    text='Split PDFs!',
    command=print_filenames
)

entry = tk.Entry(
    root,
    width=50,
    fg="grey"
)

open_button.grid(row=0,column=0, padx=20, pady=20, sticky='nwse')
entry.grid(row=0,column=1, padx=20, pady=20, sticky='nwse')
action_button.grid(row=5,column=1, padx=20, pady=15, sticky='nwse')
split = tk.IntVar(value=1)
merge = tk.IntVar()

shouldSplit = ttk.Checkbutton(root, text = "Split range:", variable = split)
shouldMerge = ttk.Checkbutton(root, text = "Merge files?", variable = merge)
shouldSplit.grid(row=1,column=0, padx=20, pady=10, sticky='w')
shouldMerge.grid(row=2,column=0, padx=20, pady=10, sticky='w')

spFrame = ttk.Frame(root)
spFrame.grid(row=1, column=1, sticky="nsew")

spMin = ttk.Spinbox(spFrame, from_= 1, to = 9999, width=10)
spMax = ttk.Spinbox(spFrame, from_= 1, to = 9999, width=10)
label = ttk.Label(spFrame, text="to")
spMin.pack(padx=0, pady=2, anchor="center")
label.pack(padx=0, pady=2, anchor="center")
spMax.pack(padx=0, pady=2, anchor="center")

root.mainloop()