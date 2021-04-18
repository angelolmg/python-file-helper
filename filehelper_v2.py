import tkinter as tk
from tkinter import ttk
from split_merge_funcs import *
from table_extract_funcs import *

title = 'File Helper'
wsize = '500x250'

class FileHelper(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title(title)
        self.resizable(False, False)
        self.geometry(wsize)

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="File Helper", font=(None, 20)).pack(side="top", fill="both", pady=30)

        tk.Button(self, text="Open split and merge",
                  command=lambda: master.switch_frame(SplitAndMerge)).pack(side="top", fill="both", pady=10)

        tk.Button(self, text="Open table extractor",
                command=lambda: master.switch_frame(TableExtractor)).pack(side="top", fill="both", pady=10)

        tk.Label(self, text="by Angelo L. (2021)", font=(None, 8), fg='gray').pack(side="bottom", fill="x", pady=10)

class SplitAndMerge(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        entry = tk.Entry(self, width=50, fg="grey")

        split = tk.IntVar(value=1)
        merge = tk.IntVar(value=0)
        shouldSplit = tk.Checkbutton(self, text = "Split range:", variable = split)
        shouldMerge = tk.Checkbutton(self, text = "Merge files?", variable = merge)

        spFrame = ttk.Frame(self)

        spMin = ttk.Spinbox(spFrame, from_= 1, to = 9999, width=10)
        spMax = ttk.Spinbox(spFrame, from_= 1, to = 9999, width=10)
        label = ttk.Label(spFrame, text="to")

        open_button = ttk.Button(self, text='Open Files', 
                                command=lambda: select_files(entry))
        action_button = ttk.Button(self,text='Split PDFs!', 
                                command=lambda: print_filenames(entry, spMin, spMax, split, merge))

        open_button.grid(row=0,column=0, padx=20, pady=20, sticky='nwse')
        action_button.grid(row=3,column=1, padx=20, pady=15, sticky='nwse')
        entry.grid(row=0,column=1, padx=20, pady=20, sticky='nwse')

        shouldSplit.grid(row=1,column=0, padx=20, pady=10, sticky='w')
        shouldMerge.grid(row=2,column=0, padx=20, pady=10, sticky='w')

        spFrame.grid(row=1, column=1, sticky="nsew")
        spMin.pack(padx=0, pady=2, anchor="center")
        label.pack(padx=0, pady=2, anchor="center")
        spMax.pack(padx=0, pady=2, anchor="center")

        backBtn = ttk.Button(self, text="Back", 
                            command=lambda: master.switch_frame(StartPage))
        backBtn.grid(row=3,column=0, padx=20, pady=10, sticky='w')

class TableExtractor(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        fileEntry = tk.Entry(self, width=50, fg="grey")
        pageEntry = tk.Entry(self, width=50)
        formatEntry = tk.Entry(self, width=50)

        shouldFormat = tk.IntVar(value=0)

        open_button = ttk.Button(self, text='Open Files', 
                                command=lambda: select_file(fileEntry))
        action_button = ttk.Button(self,text='Extract table!', 
                                command=lambda: extract_tables(fileEntry, pageEntry, shouldFormat,formatEntry))

        pageEntryLabel = tk.Label(self, text="Page range: \n(ex.: 1-2, 11-16)")

        formatEntryBox = tk.Checkbutton(self, text="Format collums? \n(ex.: 5, 8, 11)", 
                                        variable = shouldFormat, 
                                        command = lambda:toggleEntry(formatEntry))
        formatEntry.config(state='disabled')
        
        open_button.grid(row=0, column=0, padx=20, pady=20, sticky='nwse')
        action_button.grid(row=3, column=1, padx=20, pady=15, sticky='nwse')
        fileEntry.grid(row=0, column=1, padx=20, pady=20, sticky='nwse')
        pageEntry.grid(row=1, column=1, padx=20, pady=20, sticky='w')
        pageEntryLabel.grid(row=1, column=0, padx=20, pady=5, sticky='nwse')
        formatEntry.grid(row=2, column=1, padx=20, pady=20, sticky='w')
        formatEntryBox.grid(row=2, column=0, padx=20, pady=5, sticky='w')


        backBtn = ttk.Button(self, text="Back", 
                            command=lambda: master.switch_frame(StartPage))
        backBtn.grid(row=3,column=0, padx=20, pady=10, sticky='w')

if __name__ == "__main__":
    app = FileHelper()
    app.mainloop()