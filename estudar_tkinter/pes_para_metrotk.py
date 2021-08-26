import tkinter
from tkinter import ttk


class PesParaMetro:

    def __init__(self, root1):

        root1.title("Pés para metros")

        mainframe = ttk.Frame(root1, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        root1.columnconfigure(0, weight=1)
        root1.rowconfigure(0, weight=1)

        self.pes = tkinter.StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.pes)
        feet_entry.grid(column=2, row=1, sticky=(tkinter.W, tkinter.E))
        self.metros = tkinter.StringVar()

        ttk.Label(mainframe, textvariable=self.metros).grid(column=2, row=2, sticky=(tkinter.W, tkinter.E))
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=3, row=3, sticky=tkinter.W)

        ttk.Label(mainframe, text="Pés").grid(column=3, row=1, sticky=tkinter.W)
        ttk.Label(mainframe, text="Inserir o valor: ").grid(column=1, row=1, sticky=tkinter.W)
        ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=tkinter.E)
        ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=tkinter.W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root1.bind("<Return>", self.calcular)

    def calcular(self):
        try:
            value = float(self.pes.get())
            self.metros.set(int(0.3048 * value * 10000.0 + 0.5) / 10000.0)
        except ValueError:
            pass


root = tkinter.Tk()
PesParaMetro(root)
root.mainloop()
