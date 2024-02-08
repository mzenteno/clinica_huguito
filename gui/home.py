import tkinter as tk
from tkinter import ttk
from tkinter import Button, Menu, Toplevel
from gui.pacientes import create_content

master = tk.Tk()
class Home:    
    
    def __init__(self):        
        master.title('CLINCIA HUGUITO')
        master.minsize(1024, 800) 
        master.attributes('-zoomed', True)
        
        #Configurar menú
        menubar = Menu(master)
        master.config(menu=menubar)
                
        archivoMenu = Menu(menubar, tearoff=0)
        atencionMenu = Menu(menubar, tearoff=0)
        reportesMenu = Menu(menubar, tearoff=0)
        
        archivoMenu.add_command(label="Pacientes", command=self.create_window)
        archivoMenu.add_separator()
        archivoMenu.add_command(label="Seguros", command=self.create_window)
        
        atencionMenu.add_command(label="Historias clínicas", command=self.donothing)
        atencionMenu.add_separator()
        atencionMenu.add_command(label="Consultas", command=self.donothing)
        atencionMenu.add_command(label="Re-consultas", command=self.donothing)
        
        reportesMenu.add_command(label="Consultas", command=self.donothing)
        reportesMenu.add_command(label="Re-consultas", command=self.donothing)
        
        menubar.add_cascade(label='Archivo', menu=archivoMenu)
        menubar.add_cascade(label='Atención', menu=atencionMenu)
        menubar.add_cascade(label='Reportes', menu=reportesMenu)
        
        # Creamos un Tab control
        tab_control = ttk.Notebook(master)
        tab_control.pack(expand=1, fill='both')
        # Creamos un Tab y le agregamos un botón que abre una nueva ventana
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Tab 1')
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Tab 2')
              
        # Llamamos a la función create_content del archivo externo para agregar el contenido a tab1
        create_content(tab1)
        
        master.mainloop()
        
        
    def donothing(root):
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()
               
    def create_window():
        window = Toplevel(master)
        window.title("Ventana Secundaria")
        window.geometry("300x200")

        label = tk.Label(window, text="Esta es una ventana secundaria")
        label.pack(padx=10, pady=10)

        master.windows.append(window)