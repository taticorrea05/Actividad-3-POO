
import math
import tkinter as tk
from tkinter import ttk, messagebox


class Notas:
    def __init__(self, lista_notas):
        self.lista_notas = lista_notas

    def calcular_promedio(self):
        suma = sum(self.lista_notas)
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = 0

        for nota in self.lista_notas:
            suma += (nota - promedio) ** 2

        return math.sqrt(suma / len(self.lista_notas))

    def calcular_mayor(self):
        return max(self.lista_notas)

    def calcular_menor(self):
        return min(self.lista_notas)


class VentanaPrincipal:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ejercicio 8.2 - Notas")
        self.raiz.geometry("360x430")
        self.raiz.resizable(False, False)

        self.campos = []
        self.resultados = {}

        self.inicio()

    def inicio(self):
        panel = ttk.Frame(self.raiz, padding=20)
        panel.pack(fill="both", expand=True)

        titulo = ttk.Label(
            panel,
            text="Cálculo de notas",
            font=("Arial", 16, "bold")
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        for i in range(5):
            etiqueta = ttk.Label(
                panel,
                text=f"Nota {i + 1}:"
            )
            etiqueta.grid(
                row=i + 1,
                column=0,
                padx=10,
                pady=5,
                sticky="w"
            )

            campo = ttk.Entry(panel, width=20)
            campo.grid(
                row=i + 1,
                column=1,
                padx=10,
                pady=5
            )

            self.campos.append(campo)

        boton_calcular = ttk.Button(
            panel,
            text="Calcular",
            command=self.calcular
        )
        boton_calcular.grid(
            row=6,
            column=0,
            pady=15
        )

        boton_limpiar = ttk.Button(
            panel,
            text="Limpiar",
            command=self.limpiar
        )
        boton_limpiar.grid(
            row=6,
            column=1,
            pady=15
        )

        nombres = [
            ("promedio", "Promedio"),
            ("desviacion", "Desviación estándar"),
            ("mayor", "Nota mayor"),
            ("menor", "Nota menor")
        ]

        for i, (clave, nombre) in enumerate(nombres):
            etiqueta = ttk.Label(panel, text=nombre + ":")
            etiqueta.grid(
                row=i + 7,
                column=0,
                padx=10,
                pady=7,
                sticky="w"
            )

            resultado = tk.StringVar(value="")

            etiqueta_resultado = ttk.Label(
                panel,
                textvariable=resultado
            )
            etiqueta_resultado.grid(
                row=i + 7,
                column=1,
                padx=10,
                pady=7,
                sticky="w"
            )

            self.resultados[clave] = resultado

    def calcular(self):
        valores = []

        for campo in self.campos:
            texto = campo.get().strip()

            if texto == "":
                messagebox.showwarning(
                    "Campos vacíos",
                    "Debe ingresar las cinco notas."
                )
                return

            try:
                nota = float(texto.replace(",", "."))

                if not math.isfinite(nota):
                    raise ValueError

                valores.append(nota)

            except ValueError:
                messagebox.showerror(
                    "Error de entrada",
                    "Todas las notas deben ser valores numéricos válidos."
                )
                return

        notas = Notas(valores)

        promedio = notas.calcular_promedio()
        desviacion = notas.calcular_desviacion()
        mayor = notas.calcular_mayor()
        menor = notas.calcular_menor()

        self.resultados["promedio"].set(f"{promedio:.2f}")
        self.resultados["desviacion"].set(f"{desviacion:.2f}")
        self.resultados["mayor"].set(f"{mayor:g}")
        self.resultados["menor"].set(f"{menor:g}")

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)

        for resultado in self.resultados.values():
            resultado.set("")


def main():
    raiz = tk.Tk()
    VentanaPrincipal(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()
