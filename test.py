from urllib import response
from matplotlib.style import available
from rbd import RBD
import tkinter
from PIL import Image, ImageTk
from tkinter import DISABLED, END, LEFT, Toplevel, font
from tkinter import messagebox

class Interface():

    def __init__(self, master=None):
        self.master = tkinter.Frame(master)
        self.frame_add_alternative = None
        self.archs = []

        self.title = tkinter.Label(self.master, text="Calculadora RBD")
        self.title['font'] = ('Calibri', '14', 'bold')
        self.title.grid(row=1, column=0)

        # Define main images
        global img_add
        img_add = Image.open("images/square-plus.png")
        img_add = img_add.resize((30,30), Image.ANTIALIAS)
        img_add = ImageTk.PhotoImage(img_add)

        global img_quit
        img_quit = Image.open("images/logout.png")
        img_quit = img_quit.resize((30,30), Image.ANTIALIAS)
        img_quit = ImageTk.PhotoImage(img_quit)

        global img_back
        img_back = Image.open("images/arrow-back.png")
        img_back = img_back.resize((30,30), Image.ANTIALIAS)
        img_back = ImageTk.PhotoImage(img_back)

        global img_check
        img_check = Image.open("images/check.png")
        img_check = img_check.resize((30,30), Image.ANTIALIAS)
        img_check = ImageTk.PhotoImage(img_check)

        self.button_add = tkinter.Button(self.master, image=img_add, compound=LEFT,
                                        text="Adicionar alternativa", command=self.add)
        self.button_add['font'] = ('Calibri', '12', 'bold')
        self.button_add.grid(row=2, column=0)

        self.button_quit = tkinter.Button(self.master, image=img_quit, compound=LEFT,
                                        text="Sair", command=self.quit_ask)
        self.button_quit['font'] = ('Calibri', '12', 'bold')
        self.button_quit.grid(row=3, column=0)

        self.master.pack()

    def quit_ask(self):
        response = messagebox.askyesno(
            "Sair",
            "Poxa, já vai me abandonar? Tem certeza que quer ir embora?"
        )

        if response:
            self.master.quit()

    def add(self):
        # If this frame is not None, it means the user has already made an inserction.
        # To avoid interface mismatches, this frame must be deleted.
        if self.frame_add_alternative != None:
            self.frame_add_alternative.destroy()

        # Create the Toplevel window frame
        self.frame_add_alternative = Toplevel(self.master)
        # Setup window frame configs
        self.frame_add_alternative.title("Adicionar alternativa")
        self.frame_add_alternative.wm_transient(self.master)
        self.frame_add_alternative.iconbitmap("images/calculator.ico")

        # Create Label Frame to contain the widgets
        self.add_label_frame = tkinter.LabelFrame(self.frame_add_alternative, text="Me passe os dados")
        self.add_label_frame.pack()

        # Label and Entry - Name
        self.add_label_name = tkinter.Label(self.add_label_frame, text="Alternativa: ")
        self.add_label_name.grid(row=0, column=0)

        self.add_entry_name = tkinter.Entry(self.add_label_frame, borderwidth=5)
        self.add_entry_name.grid(row=0, column=1)

        # Label and Entry - Availibility
        self.add_label_availibility = tkinter.Label(self.add_label_frame, text="Disponibilidade: ")
        self.add_label_availibility.grid(row=1, column=0)

        self.add_entry_availibility = tkinter.Entry(self.add_label_frame, borderwidth=5)
        self.add_entry_availibility.grid(row=1, column=1)

        # Label and Entry - Cost
        self.add_label_cost = tkinter.Label(self.add_label_frame, text="Custo: ")
        self.add_label_cost.grid(row=2, column=0)

        self.add_entry_cost = tkinter.Entry(self.add_label_frame, borderwidth=5)
        self.add_entry_cost.grid(row=2, column=1)

        # Label and Entry - Unavailibility
        self.add_label_availibility = tkinter.Label(self.add_label_frame, text="Indisponibilidade: ")
        self.add_label_availibility.grid(row=3, column=0)

        self.add_entry_unavailibility = tkinter.Entry(self.add_label_frame, borderwidth=5, state=DISABLED)
        self.add_entry_unavailibility.grid(row=3, column=1)

        # Buttons
        self.add_button_calculate = tkinter.Button(self.frame_add_alternative, image=img_check,
                                                    text="Adicionar", compound=LEFT, 
                                                    command=self.add_alternative)
        self.add_button_calculate.pack()

        self.add_button_quit = tkinter.Button(self.frame_add_alternative, image=img_back,
                                                    text="Voltar", compound=LEFT, 
                                                    command=lambda: self.frame_add_alternative.destroy())
        self.add_button_quit.pack()

    def add_alternative(self):
        # Get values from user entries
        name = self.add_entry_name.get
        availibility = float(self.add_entry_availibility.get)
        cost = float(self.add_entry_cost.get)

        # Create a new RBD object
        rbd = RBD(
            alternative=name,
            availability=availibility,
            cost=cost
        )
        self.archs.append(rbd)

        response = messagebox.askyesnocancel(
            "Sucesso!",
            "Desejas adicionar mais alternativas?"
        )
        if response:
            self.add_entry_name.delete(0, END)
            self.add_entry_availibility.delete(0, END)
            self.add_entry_cost.delete(0, END)
            self.add_entry_unavailibility.delete(0, END)

            self.add_alternative()


root = tkinter.Tk()
root.title("Calculadora - RBD")
root.iconbitmap("images/calculator.ico")
_font = font.nametofont("TkDefaultFont")
_font.configure(family="Calibri", size=12)
Interface()
root.mainloop()