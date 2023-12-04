from tkinter import *


class Principal:
    def __init__(self, view):
        self.root = view
        self.root.title("Menu principal")

        self.root.geometry("800x433")
        self.root.iconbitmap("icono.ico")
        self.root.resizable(False, False)
        self.fondo = PhotoImage(file="Recursos/fondo.png")
        self.background = Label(self.root, image=self.fondo, text="Inicio")
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.Info = Label(self.root, text="Control de Asistencia", font=("Helvetica", 30))
        self.Info.pack(side=TOP, pady=50)

        button_frame = Frame(self.root)
        button_frame.pack(side=TOP)

        self.BtnEntrada = Button(button_frame, text="Registro de Entradas", bg="#72DE0D", font=("Helvetica", 18))
        self.BtnEntrada.pack(side=LEFT, padx=10, pady=10)

        self.BtnSalida = Button(button_frame, text="Registro de Salidas", bg="#DE430D", font=("Helvetica", 18))
        self.BtnSalida.pack(side=LEFT, padx=10, pady=10)

        self.BtnRegistro = Button(self.root, text="Datos Biométricos", bg="#DEC80D", font=("Helvetica", 18))
        self.BtnRegistro.pack(side=TOP, pady=10)


if __name__ == "__main__":
    panel = Tk()
    app = Principal(panel)
    panel.mainloop()
