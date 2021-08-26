import tkinter
from tkinter import ttk


class PrecoPorLitro:

    def __init__(self, root2):

        root2.title("Preço por litro")
        mainframe = ttk.Frame(root2, padding="3 3 12 12")

        mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        root2.columnconfigure(0, weight=1)
        root2.rowconfigure(0, weight=1)

        self.ml = tkinter.StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.ml)
        feet_entry.grid(column=2, row=1, sticky=(tkinter.W, tkinter.E))
        self.valor_litro = tkinter.StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.valor_litro)
        feet_entry.grid(column=2, row=2, sticky=(tkinter.W, tkinter.E))
        self.valor_por_litro = tkinter.StringVar()

        ttk.Label(mainframe, textvariable=self.valor_por_litro).grid(column=2, row=3, sticky=(tkinter.W, tkinter.E))
        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=3, row=2, sticky=tkinter.W)

        ttk.Label(mainframe, text="ml").grid(column=3, row=1, sticky=tkinter.W)
        ttk.Label(mainframe, text="Digite os ml: ").grid(column=1, row=1, sticky=tkinter.W)
        ttk.Label(mainframe, text="Digite o valor em R$ ").grid(column=1, row=2, sticky=tkinter.W)
        ttk.Label(mainframe, text="Preço por litro igual à R$").grid(column=1, row=3, sticky=tkinter.W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root2.bind("<Return>", self.calcular)

    def calcular(self):
        try:
            valor_ml = int(self.ml.get())
            preco = float(self.valor_litro.get())
            self.valor_por_litro.set(float(round(((preco * 1000) / valor_ml), 2)))
        except ValueError:
            pass


root = tkinter.Tk()
PrecoPorLitro(root)
root.mainloop()
