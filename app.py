

import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd


selected_files = []


def select_csv_files():
    global selected_files
    file_paths = filedialog.askopenfilenames(
        title="Select CSV Files",
        initialdir=os.path.expanduser("~/Desktop/MOE Intern/Automated poster"),
        filetypes=[("All files","*.*"),
                ("CSV files", "*.csv"),
                ("Excel files", "*.xlsx")]
    )
    # Clear previous text
    text_box.delete(1.0, tk.END)


    if not file_paths:
        text_box.insert(tk.END, "No files selected.\n")
        return
    
    text_box.insert(tk.END, "Selected files:\n")
    selected_files = list(file_paths)
    # for path in file_paths:
    #     text_box.insert(tk.END, path + "\n")
    
    read_files()
    

def read_files():
    text_box.delete(1.0, tk.END)
    data = []
    for path in selected_files:
        ext = os.path.splitext(path)[1].lower()
        try:
            if ext == ".csv":
                df = pd.read_csv(path, encoding='latin1')
            elif ext == ".xlsx":
                df = pd.read_excel(path)
            else:
                print(f"Unsupported file format: {path}")
                continue
            data.append(df)
            print(f"Read file: {path}")
        except Exception as e:
            print(f"Error reading {path}: {e}")
        
    print(data)
    # text_box.insert(tk.END,data)
    
    # text_box.insert(tk.END,data)
        
    


root = tk.Tk()
root.title("Water Quality Validation")

btn = tk.Button(root, text="Select Files", command=select_csv_files)
btn.pack(padx=10, pady=40)


text_box = tk.Text(root, width=100, height=30)
text_box.pack(padx=10, pady=10)


root.mainloop()
