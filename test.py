from rbd import RBD
import tkinter
from PIL import Image, ImageTk
from tkinter import DISABLED, END, LEFT, Toplevel, font
from tkinter import messagebox

class Interface():

    def __init__(self, master=None):
        self.master = tkinter.Frame(master)
        self.frame_add_alternative = None
        self.frame_show_result = None
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
                                        text="Adicionar alternativa", command=self.add)
        self.button_add['font'] = ('Calibri', '12', 'bold')
        self.button_add.grid(row=2, column=0)

        self.button_calculate = tkinter.Button(self.master, image=img_calculate, compound=LEFT,
                                        text="Calcular", command=self.calculate)
        self.button_calculate['font'] = ('Calibri', '12', 'bold')
        self.button_calculate.grid(row=3, column=0)

        self.button_quit = tkinter.Button(self.master, image=img_quit, compound=LEFT,
                                        text="Sair", command=self.quit_ask)
        self.button_quit['font'] = ('Calibri', '12', 'bold')
        self.button_quit.grid(row=4, column=0)

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
        self.add_button_add = tkinter.Button(self.frame_add_alternative, image=img_check,
                                                    text="Checar", compound=LEFT, 
                                                    command=self.add_check)
        self.add_button_add.pack()

        self.add_button_quit = tkinter.Button(self.frame_add_alternative, image=img_back,
                                                    text="Voltar", compound=LEFT, 
                                                    command=lambda: self.frame_add_alternative.destroy())
        self.add_button_quit.pack()

    def add_check(self):
        # Get values from user entries
        name = self.add_entry_name.get()
        availibility = self.add_entry_availibility.get()
        cost = self.add_entry_cost.get()

        availibility = float(availibility)
        cost = float(cost)
    
        # Create a new RBD object
        self.rbd = RBD(
            alternative=name,
            availability=availibility,
            cost=cost
        )

        self.add_entry_unavailibility.configure(state="normal")
        self.add_entry_unavailibility.insert(0, str(self.rbd.unavailability))
        self.add_entry_unavailibility.configure(state=DISABLED)

        self.add_button_add.configure(text="Adicionar", command=self.add_alternative, bg="#D3D3D3")

    def add_alternative(self):
        self.archs.append(self.rbd)

        response = messagebox.askyesnocancel(
            "Sucesso!",
            "Desejas adicionar mais alternativas?"
        )
        if response:
            self.add_entry_name.delete(0, END)
            self.add_entry_availibility.delete(0, END)
            self.add_entry_cost.delete(0, END)
            self.add_entry_unavailibility.configure(state="normal")
            self.add_entry_unavailibility.delete(0, END)
            self.add_entry_unavailibility.configure(state=DISABLED)

            self.add()
        else:
            self.frame_add_alternative.destroy()

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
            # Get costs and unavailabilities values
            costs = []
            unavs = []
            for arch in self.archs:
                costs.append(arch.cost)
                unavs.append(arch.unavailability)
            # Get max values for each one
            max_cost = max(costs)
            max_unav = max(unavs)

            # Calculate values
            for arch in self.archs:
                arch.norm_cost = (arch.cost/max_cost)
                arch.norm_unav = (arch.unavailability/max_unav)
                arch.distance = pow((arch.cost ** 2) + (arch.unavailability ** 2), 1/2)
            
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

        for arch in self.archs:
            self.show_button_arch = tkinter.Button(self.frame_show_result, text=arch.alternative,
                                                    command=lambda:self.display_value(arch),
                                                    width=20)
            self.show_button_arch.pack()

    def display_value(self, arch: RBD):
        # Create the Toplevel window frame
        self.frame_display = Toplevel(self.frame_show_result)
        # Setup window frame configs
        self.frame_display.title("Mostrar resultados")
        self.frame_display.wm_transient(self.frame_show_result)
        self.frame_display.iconbitmap("images/calculator.ico")
        
        # Display results with widgets
        # Display alternative name
        self.display_label_name_title = tkinter.Label(self.frame_display, text="Alternativa: ")
        self.display_label_name_title.grid(row=0, column=0)
        self.display_label_name = tkinter.Label(self.frame_display, text=arch.alternative)
        self.display_label_name.grid(row=0, column=1)

        # Display availability
        self.display_label_avai_title = tkinter.Label(self.frame_display, text="Disponibilidade: ")
        self.display_label_avai_title.grid(row=1, column=0)
        avai = float("{:.2f}".format(arch.alternative))
        self.display_label_avai = tkinter.Label(self.frame_display, text=avai)
        self.display_label_avai.grid(row=1, column=1)

        # Display cost
        self.display_label_cost_title = tkinter.Label(self.frame_display, text="Custo: ")
        self.display_label_cost_title.grid(row=2, column=0)
        cost = float("{:.2f}".format(arch.cost))
        self.display_label_cost = tkinter.Label(self.frame_display, text=cost)
        self.display_label_cost.grid(row=2, column=1)

        # Display unavailability
        self.display_label_unav = tkinter.Label(self.frame_display, text=arch.unavailability).pack()
        self.display_label_dist = tkinter.Label(self.frame_display, text=arch.distance).pack() 
        self.display_label_unav_month = tkinter.Label(self.frame_display, text=arch.unav_month).pack()  
        self.display_label_unav_year = tkinter.Label(self.frame_display, text=arch.unav_year).pack()
                


root = tkinter.Tk()
root.title("Calculadora - RBD")
root.iconbitmap("images/calculator.ico")
_font = font.nametofont("TkDefaultFont")
_font.configure(family="Calibri", size=12)
Interface()
root.mainloop()