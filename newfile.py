import tkinter as tk
from tkinter import ttk
import math

class Window(tk.Tk):
    def __init__(self):
        super(Window, self).__init__()
        
        self.title("Menghitung KPL")
        self.minsize(480, 320)
        #self.iconphoto(False, tk.PhotoImage(file=))
        self.text_entry()
    
    def hasil(self):
        
        kpl_sebelumnya = float(self.kpl_sebelumnya_entry.get())
        jarak_sebelumnya = float(self.jarak_sebelumnya_entry.get())
        kpl_sekarang = float(self.kpl_sekarang_entry.get())
        jarak_sekarang = float(self.jarak_sekarang_entry.get())
        
        hasil_sebelumnya = jarak_sebelumnya / kpl_sebelumnya
        hasil_sekarang = jarak_sekarang / kpl_sekarang
       
        liter = hasil_sebelumnya - hasil_sekarang
        if liter<0 :
            liter = liter * -1
        
        jarak_terakhir = jarak_sekarang - jarak_sebelumnya
        if jarak_terakhir<0 :
            jarak_terakhir = jarak_terakhir * -1

        kpl_terakhir = jarak_terakhir / liter
        
        self.kpl_terakhir_label.configure(text="{:.2f}".format(kpl_terakhir))
        
    def text_entry(self):
        kpl_sebelumnya_label = ttk.Label(self, text="Kpl Sebelumnya:")
        kpl_sebelumnya_label.grid(column=0, row=0, padx=5, pady=5)
    
        kpl_sekarang_label = ttk.Label(self, text="Kpl Sekarang:")
        kpl_sekarang_label.grid(column=0, row=1, padx=5, pady=5)
        
        jarak_sebelumnya_label = ttk.Label(self, text="Jarak Sebelumnya:")
        jarak_sebelumnya_label.grid(column=2, row=0, padx=5, pady=5)
        
        jarak_sekarang_label = ttk.Label(self, text="Jarak Sekarang:")
        jarak_sekarang_label.grid(column=2, row=1, padx=5, pady=5)

        self.kpl_sebelumnya_entry = ttk.Entry(self)
        self.kpl_sebelumnya_entry.grid(column=1, row=0, padx=7, pady=7)
        
        self.kpl_sekarang_entry = ttk.Entry(self)
        self.kpl_sekarang_entry.grid(column=1, row=1, padx=7, pady=7)
        
        self.jarak_sebelumnya_entry = ttk.Entry(self)
        self.jarak_sebelumnya_entry.grid(column=3, row=0, padx=7, pady=7)
        
        self.jarak_sekarang_entry = ttk.Entry(self)
        self.jarak_sekarang_entry.grid(column=3, row=1, padx=7, pady=7)
        
        hitung_button = ttk.Button(self, text="Hitung KPL", command=self.hasil)
        hitung_button.grid(column=1, row=3, padx=7, pady=7, columnspan=2, sticky=tk.EW)
        
        kpl_terakhir_label = ttk.Label(self, text="Kpl Terakhir:")
        kpl_terakhir_label.grid(column=2, row=4, padx=7, pady=7, sticky=tk.W)
        
        self.kpl_terakhir_label = ttk.Label(self, text="")
        self.kpl_terakhir_label.grid(column=3, row=4, padx=7, pady=7)
        

window = Window()
window.mainloop()