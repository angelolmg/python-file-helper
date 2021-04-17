import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import ntpath

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

    #print("Num. de páginas: " + str(inputpdf.numPages))

    if(begin < 1 or end > inputpdf.numPages or begin > end):
        mb.showwarning(title="Page index error", message="Inconsistent page index numbers.\nCheck and try again.")
        #print("Deu ruim com o numero de páginas!")
        return

    output = PdfFileWriter()
    for i in range(begin-1, end):
        output.addPage(inputpdf.getPage(i))

    head, tail = path_leaf(file)
    newfilename = head + "/" + tail[:-4] + "_" + str(begin) + "-" + str(end) + ".pdf"
    with open(newfilename, "wb") as outputStream:
        output.write(outputStream)
    
    return newfilename

def select_files(entry):
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

def print_filenames(entry, spMin, spMax, split, merge):
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

