from tkinter.ttk import Treeview
from rbd import RBD
from equipment import Equipment
from ttkwidgets import CheckboxTreeview
import tkinter
from PIL import Image, ImageTk
from tkinter import CENTER, DISABLED, END, LEFT, NO, RIGHT, W, Y, IntVar, Scrollbar, Toplevel, font
from tkinter import messagebox
import numpy

class Interface():

    def __init__(self, master=None):
        self.master = tkinter.Frame(master)
        self.frame_add_alternative = None
        self.frame_show_result = None
        self.rbd = RBD()
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

        global img_calculate
        img_calculate = Image.open("images/calculator.png")
        img_calculate = img_calculate.resize((30,30), Image.ANTIALIAS)
        img_calculate = ImageTk.PhotoImage(img_calculate)

        self.button_add = tkinter.Button(self.master, image=img_add, compound=LEFT,
                                        text="Adicionar", command=self.add, width=100)
        self.button_add.grid(row=2, column=0)

        self.button_calculate = tkinter.Button(self.master, image=img_calculate, compound=LEFT,
                                        text="Calcular", command=self.calculate, width=100)
        self.button_calculate.grid(row=3, column=0)

        self.button_quit = tkinter.Button(self.master, image=img_quit, compound=LEFT,
                                        text="Sair", command=self.quit_ask, width=100)
        self.button_quit.grid(row=4, column=0)

        self.master.pack()

    def quit_ask(self):
        response = messagebox.askyesno(
            "Sair",
            "Poxa, já vai me abandonar? Tem certeza que quer ir embora?"
        )

        if response:
            self.master.quit()

    def add(self, alternative=None):
        # If this frame is not None, it means the user has already made an inserction.
        # To avoid interface mismatches, this frame must be deleted.
        if self.frame_add_alternative != None:
            self.frame_add_alternative.destroy()

        # Create the Toplevel window frame
        self.frame_add_alternative = Toplevel(self.master)
        # Setup window frame configs
        self.frame_add_alternative.title("Adicionar")
        self.frame_add_alternative.wm_transient(self.master)
        self.frame_add_alternative.iconbitmap("images/calculator.ico")
        self.frame_add_alternative.geometry("300x300")

        # Create Label Frame to contain the widgets
        self.add_label_frame = tkinter.LabelFrame(self.frame_add_alternative, text="Me passe os dados")
        self.add_label_frame.pack()

        # Label and Entry - Name
        self.add_label_name = tkinter.Label(self.add_label_frame, text="Alternativa: ")
        self.add_label_name.grid(row=0, column=0)

        if alternative == None:
            self.add_entry_name = tkinter.Entry(self.add_label_frame, borderwidth=5)
            self.add_entry_name.grid(row=0, column=1)
        else:
            self.add_entry_name = tkinter.Entry(self.add_label_frame, borderwidth=5)
            self.add_entry_name.insert(0, alternative)
            self.add_entry_name.configure(state=DISABLED)
            self.add_entry_name.grid(row=0, column=1)

        # Label and Entry - Equipment
        self.add_label_equip = tkinter.Label(self.add_label_frame, text="Equipamento: ")
        self.add_label_equip.grid(row=1, column=0)

        self.add_entry_equip = tkinter.Entry(self.add_label_frame, borderwidth=5)
        self.add_entry_equip.grid(row=1, column=1)

        # Radio Button - Parallel or Series
        self.var = IntVar()
        self.add_button_serie = tkinter.Radiobutton(self.add_label_frame, text="Serie",
                                                        variable=self.var, value=1)
        self.add_button_serie.grid(row=2, column=0)

        self.add_button_parallel = tkinter.Radiobutton(self.add_label_frame, text="Paralelo",
                                                        variable=self.var, value=2)
        self.add_button_parallel.grid(row=2, column=1)

        # Label and Entry - Availibility
        self.add_label_availibility = tkinter.Label(self.add_label_frame, text="Disponibilidade: ")
        self.add_label_availibility.grid(row=3, column=0)

        self.add_entry_availibility = tkinter.Entry(self.add_label_frame, borderwidth=5)
        self.add_entry_availibility.grid(row=3, column=1)

        # Label and Entry - Cost
        self.add_label_cost = tkinter.Label(self.add_label_frame, text="Custo: ")
        self.add_label_cost.grid(row=4, column=0)

        self.add_entry_cost = tkinter.Entry(self.add_label_frame, borderwidth=5)
        self.add_entry_cost.grid(row=4, column=1)

        # Label and Entry - Unavailibility
        self.add_label_availibility = tkinter.Label(self.add_label_frame, text="Indisponibilidade: ")
        self.add_label_availibility.grid(row=5, column=0)

        self.add_entry_unavailibility = tkinter.Entry(self.add_label_frame, borderwidth=5, state=DISABLED)
        self.add_entry_unavailibility.grid(row=5, column=1)

        # Buttons
        self.add_button_add = tkinter.Button(self.frame_add_alternative, image=img_check,
                                                    text="Checar", compound=LEFT, 
                                                    command=self.add_check)
        self.add_button_add.pack()

        self.add_button_quit = tkinter.Button(self.frame_add_alternative, image=img_back,
                                                    text="Voltar", compound=LEFT, 
                                                    command=lambda: self.frame_add_alternative.destroy())
        self.add_button_quit.pack()

    def add_equip_parallel(self, value):
        qtd = int(value)
        self.equip.qtd_parallel = qtd
        self.popup.destroy()

    def add_check(self):
        # Get values from user entries
        name = self.add_entry_name.get()
        availibility = self.add_entry_availibility.get()
        cost = self.add_entry_cost.get()
        equipment = self.add_entry_equip.get()
        is_parallel = self.var.get()

        availibility = float(availibility)
        cost = float(cost)

        if is_parallel == 1:
            is_parallel = False
            self.equip = Equipment(
                availability=availibility,
                cost=cost,
                equipment=equipment,
                is_parallel=is_parallel
            )
        else:
            is_parallel = True
            # Create a new Equipment object
            self.equip = Equipment(
                availability=availibility,
                cost=cost,
                equipment=equipment,
                is_parallel=is_parallel
            )
            self.popup = Toplevel(self.frame_add_alternative)
            labelqtd = tkinter.LabelFrame(self.popup, text="Qual a quantidade em paralelo?")
            labelqtd.pack()
            entryqtd = tkinter.Entry(labelqtd)
            entryqtd.pack()
            buttonqtd = tkinter.Button(labelqtd, text="Ok", 
                                        command=lambda: self.add_equip_parallel(entryqtd.get()))
            buttonqtd.pack()

        # Create a new RBD object
        self.rbd.alternative = name        

        self.rbd.equipments.append(self.equip)

        self.add_entry_unavailibility.configure(state="normal")
        self.add_entry_unavailibility.insert(0, str(self.equip.unavailability))
        self.add_entry_unavailibility.configure(state=DISABLED)

        self.add_button_add.configure(text="Adicionar", command=self.add_alternative, bg="#D3D3D3")

    def add_alternative(self):

        response = messagebox.askyesnocancel(
            "Sucesso!",
            "Desejas adicionar mais equipamentos a essa arquitetura?"
        )
        if response:
            self.add_entry_name.configure(state=DISABLED)
            self.add_entry_availibility.delete(0, END)
            self.add_entry_cost.delete(0, END)
            self.add_entry_unavailibility.configure(state="normal")
            self.add_entry_unavailibility.delete(0, END)
            self.add_entry_unavailibility.configure(state=DISABLED)
            self.add(self.rbd.alternative)
        else:
            print(f"adding {self.rbd.alternative} it has {len(self.rbd.equipments)} equipments")
            self.archs.append(self.rbd)
            self.rbd = RBD()

            self.add_entry_name.configure(state="normal")
            self.add_entry_name.delete(0, END)
            self.add_entry_availibility.delete(0, END)
            self.add_entry_cost.delete(0, END)
            self.add_entry_unavailibility.configure(state="normal")
            self.add_entry_unavailibility.delete(0, END)
            self.add_entry_unavailibility.configure(state=DISABLED)

            self.add()

    def show_inserts(self):
        if len(self.archs) > 0:
            for arch in self.archs:
                for equip in arch.equipments:
                    print(arch.alternative)
                    print(equip.equipment)

    def calculate(self):
        if len(self.archs) == 0:
            response = messagebox.askyesno(
            "Aviso",
            """Poxa, parece que você não adicionou nenhuma arquitetura. Não tenho como calcular :(
            \nFaz assim, adiciona as alternativas e volta aqui de novo, OK?"""
            )

            if response:
                self.add()
        else:
            for rbd in self.archs:
                costs = []
                unavs = []
                equip_series = []
                dparallel = 0
                for equip in rbd.equipments:

                    if equip.is_parallel:
                        dparallel = 1 - (1 - equip.availability) ** equip.qtd_parallel
                        equip_series.append(dparallel)
                    else:
                        equip_series.append(equip.availability)
                    costs.append(equip.cost)
                    unavs.append(equip.unavailability)

                # Get max values for each one
                max_cost = max(costs)
                max_unav = max(unavs)

                rbd.cost = sum(costs)
                rbd.availability = numpy.prod(equip_series)
                print(rbd.availability)
                rbd.unavailability = (1 - rbd.availability)

                # Calculate values
                rbd.norm_cost = (rbd.cost/max_cost)
                rbd.norm_unav = (rbd.unavailability/max_unav)
                rbd.distance = pow((rbd.norm_cost ** 2) + (rbd.norm_unav ** 2), 1/2)

                rbd.unav_month = (rbd.unavailability * (30*24))
                rbd.unav_year = rbd.unav_month * 12   
            
            messagebox.showinfo(
            "Sucesso!",
            """Prontinho, os valores foram calculados com sucesso. Clique para ver o resultado."""
            )
            self.show_result()
        
    def show_result(self):
        # If this frame is not None, it means the user has already made an inserction.
        # To avoid interface mismatches, this frame must be deleted.
        if self.frame_show_result != None:
            self.frame_show_result.destroy()

        # Create the Toplevel window frame
        self.frame_show_result = Toplevel(self.master)
        # Setup window frame configs
        self.frame_show_result.title("Mostrar resultados")
        self.frame_show_result.wm_transient(self.master)
        self.frame_show_result.iconbitmap("images/calculator.ico")
        
        self.frame_scroll = Scrollbar(self.frame_show_result, orient="vertical")
        self.frame_scroll.pack(side=RIGHT, fill=Y)

        self.view = Treeview(self.frame_show_result, yscrollcommand=self.frame_scroll.set)
        self.view.pack()

        self.frame_scroll.config(command=self.view.yview)

        columns = ["Arquitetura", "Disponibilidade", "Custo", "Indisp.", "Distância", "Indisp. Mês", "Indisp. Ano"]

        # define column
        self.view["columns"] = columns

        # format column and headings
        i = 0
        for column in columns:
            if i == 0:
                self.view.column("#0", anchor=W, stretch=NO, width=70)
            
            self.view.column(column, anchor=CENTER, stretch=NO, width=70)
            self.view.heading(column, text=column, anchor=CENTER)
            i+=1

        list = []
        data = []
        dist = []
        for rbd in self.archs:
            list = (
                rbd.alternative, 
                rbd.availability,
                rbd.cost,
                rbd.unavailability,
                rbd.distance,
                rbd.unav_month,
                rbd.unav_year
                )
            dist.append(rbd.distance)
            data.append(list)
        # add data
        i = 0
        for rbd in data:
            self.view.insert(parent="", index="end", iid=i, text="", values=rbd)
            i += 1

        self.view.pack(pady=10, padx=20)

        best = "Arq"
        for rbd in self.archs:
            if min(dist) == rbd.distance:
                best = rbd.alternative

        label_best_alt = tkinter.Label(self.frame_show_result, 
                                            text="Melhor alternativa: "+best,
                                            font=('Calibri', '12', 'bold')).pack()

        button_back = tkinter.Button(self.frame_show_result, text="Voltar", image=img_back,
                                    compound=LEFT, command=self.frame_show_result.destroy).pack()

root = tkinter.Tk()
root.title("Calculadora - RBD")
root.iconbitmap("images/calculator.ico")
root.geometry("300x200")
_font = font.nametofont("TkDefaultFont")
_font.configure(family="Calibri", size=12)
Interface()
root.mainloop()