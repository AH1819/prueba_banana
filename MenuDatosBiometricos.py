from tkinter import *


class MenuDB:
    def __init__(self, view):
        self.root = view
        self.root = view
        self.root.title("Menu de opciones")

        self.root.geometry("648x361")
        self.root.iconbitmap("icono.ico")
        self.root.resizable(False, False)
        self.fondo = PhotoImage(file="Recursos/fondoRegistro.png")
        self.background = Label(self.root, image=self.fondo, text="Inicio")
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.Info = Label(self.root, text="Opciones", font=("Helvetica", 30))
        self.Info.pack(padx=10, pady=20)

        self.imageRegistrar = PhotoImage(file="Recursos/face.png")
        self.BtnRegistro = Button(
            self.root,
            text="Registrar Datos Biometricos",
            image=self.imageRegistrar,
            compound="left",
            bg="#72DE0D",
            font=("Helvetica", 18)
        )
        self.BtnRegistro.pack(padx=10, pady=20)
        self.imageEntrenar = PhotoImage(file="Recursos/training.png")
        self.BtnEntrenamiento = Button(
            self.root,
            text="Entrenar modelo",
            image=self.imageEntrenar,
            compound="left",
            bg="#DE430D",
            font=("Helvetica", 18)
        )
        self.BtnEntrenamiento.pack(padx=10, pady=20)


if __name__ == "__main__":
    panel = Tk()
    app = MenuDB(panel)
    panel.mainloop()
