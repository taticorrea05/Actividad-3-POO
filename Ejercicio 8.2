
import math
import tkinter as tk
from tkinter import messagebox, ttk


class Notas:
    def __init__(self, lista_notas):
        if len(lista_notas) != 5:
            raise ValueError("Se requieren exactamente cinco notas.")

        if not all(math.isfinite(nota) for nota in lista_notas):
            raise ValueError("Las notas deben ser números válidos.")

        self.lista_notas = list(lista_notas)

    def calcular_promedio(self):
        return sum(self.lista_notas) / len(self.lista_notas)

    def calcular_desviacion(self):
        promedio = self.calcular_promedio()
        suma = sum((nota - promedio) ** 2 for nota in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_mayor(self):
        return max(self.lista_notas)

    def calcular_menor(self):
        return min(self.lista_notas)


class VentanaPrincipal:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ejercicio 8.2 - Notas")
        self.raiz.resizable(False, False)
        self.campos = []
        self.resultados = {}
        self.inicio()

    def inicio(self):
        panel = ttk.Frame(self.raiz, padding=22)
        panel.grid(row=0, column=0)

        ttk.Label(
            panel,
            text="Cálculo de notas",
            font=("Arial", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=(0, 12))

        for indice in range(5):
            ttk.Label(
                panel, text=f"Nota {indice + 1}:"
            ).grid(row=indice + 1, column=0, sticky="w", pady=4)

            campo = ttk.Entry(panel, width=22)
            campo.grid(row=indice + 1, column=1, pady=4)
            self.campos.append(campo)

        ttk.Button(
            panel, text="Calcular", command=self.calcular
        ).grid(row=6, column=0, padx=4, pady=(14, 12), sticky="ew")

        ttk.Button(
            panel, text="Limpiar", command=self.limpiar
        ).grid(row=6, column=1, padx=4, pady=(14, 12), sticky="ew")

        etiquetas = [
            ("promedio", "Promedio"),
            ("desviacion", "Desviación estándar"),
            ("mayor", "Nota mayor"),
            ("menor", "Nota menor")
        ]

        for fila, (clave, etiqueta) in enumerate(etiquetas, start=7):
            ttk.Label(
                panel, text=f"{etiqueta}:"
            ).grid(row=fila, column=0, sticky="w", pady=3)

            variable = tk.StringVar(value="—")
            ttk.Label(
                panel, textvariable=variable
            ).grid(row=fila, column=1, sticky="w", pady=3)

            self.resultados[clave] = variable

        self.campos[0].focus_set()

    def calcular(self):
        textos = [campo.get().strip() for campo in self.campos]

        if any(not texto for texto in textos):
            messagebox.showwarning(
                "Notas incompletas",
                "Debe ingresar las cinco notas."
            )
            return

        try:
            valores = [
                float(texto.replace(",", ".")) for texto in textos
            ]
            notas = Notas(valores)

        except ValueError:
            messagebox.showerror(
                "Datos incorrectos",
                "Ingrese únicamente valores numéricos válidos."
            )
            return

        self.resultados["promedio"].set(
            f"{notas.calcular_promedio():.2f}"
        )
        self.resultados["desviacion"].set(
            f"{notas.calcular_desviacion():.2f}"
        )
        self.resultados["mayor"].set(
            f"{notas.calcular_mayor():g}"
        )
        self.resultados["menor"].set(
            f"{notas.calcular_menor():g}"
        )

    def limpiar(self):
        for campo in self.campos:
            campo.delete(0, tk.END)

        for variable in self.resultados.values():
            variable.set("—")

        self.campos[0].focus_set()


def main():
    raiz = tk.Tk()
    VentanaPrincipal(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()
