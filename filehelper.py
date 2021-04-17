from split_merge_funcs import *

root = tk.Tk()
root.title('File Helper')
root.resizable(False, False)
root.geometry('500x250')

entry = tk.Entry(root, width=50, fg="grey")

split = tk.IntVar(value=1)
merge = tk.IntVar(value=0)
shouldSplit = ttk.Checkbutton(root, text = "Split range:", variable = split)
shouldMerge = ttk.Checkbutton(root, text = "Merge files?", variable = merge)

spFrame = ttk.Frame(root)

spMin = ttk.Spinbox(spFrame, from_= 1, to = 9999, width=10)
spMax = ttk.Spinbox(spFrame, from_= 1, to = 9999, width=10)
label = ttk.Label(spFrame, text="to")

open_button = ttk.Button(root, text='Open Files', command=lambda: select_files(entry))
action_button = ttk.Button(root,text='Split PDFs!', command=lambda: print_filenames(entry, spMin, spMax, split, merge))

open_button.grid(row=0,column=0, padx=20, pady=20, sticky='nwse')
action_button.grid(row=5,column=1, padx=20, pady=15, sticky='nwse')
entry.grid(row=0,column=1, padx=20, pady=20, sticky='nwse')

shouldSplit.grid(row=1,column=0, padx=20, pady=10, sticky='w')
shouldMerge.grid(row=2,column=0, padx=20, pady=10, sticky='w')

spFrame.grid(row=1, column=1, sticky="nsew")
spMin.pack(padx=0, pady=2, anchor="center")
label.pack(padx=0, pady=2, anchor="center")
spMax.pack(padx=0, pady=2, anchor="center")

root.mainloop()