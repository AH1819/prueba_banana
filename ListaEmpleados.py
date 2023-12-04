from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Style


class EmpleadosView:
    def __init__(self, view):
        self.root = view
        self.root.state('zoomed')
        self.root.title("Lista de Empleados")
        self.root.iconbitmap("icono.ico")
        self.root.resizable(False, False)

        self.Info = Label(self.root, text="Selecciona un empleado", font=("Helvetica", 15))
        self.Info.pack(padx=10, pady=10)

        self.id_seleccionado = Label(self.root, text="N°: ")
        self.id_seleccionado.place(x=0, y=0)

        self.entry_nombre = Entry(self.root, font=("Arial", 10))
        self.entry_nombre.pack(padx=10, pady=10)

        self.tree = Treeview(self.root, columns=("N°", "Nombre", "Area", "Status"), show="headings")
        Style().configure("Treeview.Heading", font=("Arial", 10))
        Style().configure("Treeview", font=("Arial", 10))
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(expand=True, fill=BOTH)

        self.btn_registrar_face = Button(self.root, text="Siguiente", bg="lightblue", state="disabled",
                                         font=("Helvetica", 10))
        self.btn_registrar_face.pack(padx=10, pady=10)

    def set_tree_data(self, data):
        self.tree.delete(*self.tree.get_children())
        if data:
            for row in data:
                self.tree.insert("", "end", values=row)
        else:
            self.entry_nombre.config(state="disabled")
            messagebox.showwarning(message="No se encontraron datos", title="Consulta")


if __name__ == "__main__":
    panel = Tk()
    app = EmpleadosView(panel)
    panel.mainloop()
