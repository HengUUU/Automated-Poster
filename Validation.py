import os
import tkinter as tk
from tkinter import filedialog

class FileSelector:
    def __init__(self, root):
        self.root = root
        self.text_box = tk.Text(root, width=100, height=30)
        self.text_box.pack(padx=10, pady=10)

        self.select_button = tk.Button(root, text="Select CSV Files", command=self.select_csv_files)
        self.select_button.pack(padx=100, pady=100)

    def select_csv_files(self):
        file_paths = filedialog.askopenfilenames(
            title="Select CSV Files",
            initialdir=os.path.expanduser("~/Desktop"),
            filetypes=[
                ("All files", "*.*"),
                ("CSV files", "*.csv"),
                ("Excel files", "*.xlsx")
            ]
        )

        self.text_box.delete(1.0, tk.END)  # clear previous text

        if not file_paths:
            self.text_box.insert(tk.END, "No files selected.\n")
            return

        self.text_box.insert(tk.END, "Selected files:\n")
        for path in file_paths:
            self.text_box.insert(tk.END, path + "\n")
