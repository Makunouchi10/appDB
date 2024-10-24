import tkinter as tk
from classgetRecord import EstudianteAPI

class Aplicacion:

    def __init__(self, root):
        self.root = root
        self.root.title("Último Registro Estudiante")
        self.root.geometry("300x200")

        self.api = EstudianteAPI("https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante")

        # Botón para obtener el último registro
        self.boton = tk.Button(root, text="Obtener Último Registro", command=self.mostrar_ultimo_registro)
        self.boton.pack(pady=10)

        # Label para mostrar los resultados
        self.resultado_label = tk.Label(root, text="", justify="left")
        self.resultado_label.pack(pady=10)

    def mostrar_ultimo_registro(self):
        try:
            ultimo_registro = (self.api.obtener_ultimo_registro())
            if ultimo_registro:
                self.mostrar_datos(ultimo_registro)
            else:
                self.resultado_label.config(text="No se encontraron registros.")
        except ValueError as e:
            self.resultado_label.config(text=str(e))

    def mostrar_datos(self, registro):
        texto = (
            f"ID: {registro['id']}\n"
            f"Nombre: {registro['nombre']}\n"
            f"Apellido: {registro['apellido']}\n"
            f"Ciudad: {registro['ciudad']}\n"
            f"Calle: {registro['calle']}"
        )
        self.resultado_label.config(text=texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
