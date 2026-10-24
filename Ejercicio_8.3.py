
import math
import tkinter as tk
from tkinter import ttk, messagebox


# Clase padre
class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

    def calcular_volumen(self):
        raise NotImplementedError

    def calcular_superficie(self):
        raise NotImplementedError


# Clase Cilindro
class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return math.pi * self.radio ** 2 * self.altura

    def calcular_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)


# Clase Esfera
class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return (4 / 3) * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio ** 2


# Clase Piramide de base cuadrada
class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return self.base ** 2 * self.altura / 3

    def calcular_superficie(self):
        return self.base ** 2 + 2 * self.base * self.apotema


# Clase Cubo
class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return self.lado ** 3

    def calcular_superficie(self):
        return 6 * self.lado ** 2


# Clase Prisma rectangular
class Prisma(FiguraGeometrica):
    def __init__(self, largo, ancho, altura):
        super().__init__()
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
        self.volumen = self.calcular_volumen()
        self.superficie = self.calcular_superficie()

    def calcular_volumen(self):
        return self.largo * self.ancho * self.altura

    def calcular_superficie(self):
        return 2 * (
            self.largo * self.ancho
            + self.largo * self.altura
            + self.ancho * self.altura
        )


# Ventana para ingresar las dimensiones de una figura
class VentanaFigura:
    DATOS = {
        "Cilindro": (["Radio", "Altura"], Cilindro),
        "Esfera": (["Radio"], Esfera),
        "Pirámide": (["Base", "Altura", "Apotema"], Piramide),
        "Cubo": (["Lado"], Cubo),
        "Prisma": (["Largo", "Ancho", "Altura"], Prisma)
    }

    def __init__(self, principal, nombre):
        self.nombre = nombre
        self.campos = {}

        self.ventana = tk.Toplevel(principal)
        self.ventana.title(nombre)
        self.ventana.resizable(False, False)

        self.volumen_texto = tk.StringVar(value="—")
        self.superficie_texto = tk.StringVar(value="—")

        self.inicio()

    def inicio(self):
        panel = ttk.Frame(self.ventana, padding=18)
        panel.pack()

        ttk.Label(
            panel,
            text=self.nombre,
            font=("Arial", 15, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        nombres, _ = self.DATOS[self.nombre]

        for fila, nombre_campo in enumerate(nombres, 1):
            ttk.Label(
                panel,
                text=f"{nombre_campo} (cm):"
            ).grid(row=fila, column=0, sticky="w", pady=4)

            entrada = ttk.Entry(panel, width=18)
            entrada.grid(
                row=fila, column=1, padx=(10, 0), pady=4
            )
            self.campos[nombre_campo] = entrada

        fila_boton = len(nombres) + 1

        ttk.Button(
            panel,
            text="Calcular",
            command=self.calcular
        ).grid(row=fila_boton, column=0, pady=10, sticky="ew")

        ttk.Button(
            panel,
            text="Limpiar",
            command=self.limpiar
        ).grid(
            row=fila_boton,
            column=1,
            padx=(10, 0),
            pady=10,
            sticky="ew"
        )

        ttk.Label(
            panel, text="Volumen (cm³):"
        ).grid(row=fila_boton + 1, column=0, sticky="w")

        ttk.Label(
            panel, textvariable=self.volumen_texto
        ).grid(row=fila_boton + 1, column=1, sticky="w")

        ttk.Label(
            panel, text="Superficie (cm²):"
        ).grid(
            row=fila_boton + 2,
            column=0,
            sticky="w",
            pady=5
        )

        ttk.Label(
            panel, textvariable=self.superficie_texto
        ).grid(row=fila_boton + 2, column=1, sticky="w")

        self.dibujo = tk.Canvas(
            panel,
            width=240,
            height=160,
            bg="white",
            highlightthickness=1
        )
        self.dibujo.grid(
            row=fila_boton + 3,
            column=0,
            columnspan=2,
            pady=(12, 0)
        )

        self.dibujar_figura()

    def dibujar_figura(self):
        c = self.dibujo
        color = "#cce5fa"
        linea = "#235789"

        if self.nombre == "Esfera":
            c.create_oval(
                70, 20, 170, 120,
                fill=color, outline=linea, width=2
            )
            c.create_arc(
                70, 49, 170, 91,
                start=0, extent=180, style="arc",
                outline=linea, dash=(4, 3)
            )
            c.create_arc(
                70, 49, 170, 91,
                start=180, extent=180,
                style="arc", outline=linea
            )

        elif self.nombre == "Cilindro":
            c.create_rectangle(
                75, 45, 165, 120,
                fill=color, outline=""
            )
            c.create_line(
                75, 40, 75, 120, fill=linea, width=2
            )
            c.create_line(
                165, 40, 165, 120, fill=linea, width=2
            )
            c.create_oval(
                75, 20, 165, 60,
                fill=color, outline=linea, width=2
            )
            c.create_arc(
                75, 100, 165, 140,
                start=180, extent=180,
                style="arc", outline=linea, width=2
            )
            c.create_arc(
                75, 100, 165, 140,
                start=0, extent=180,
                style="arc", outline=linea, dash=(4, 3)
            )

        elif self.nombre == "Pirámide":
            c.create_polygon(
                120, 20, 50, 115, 170, 115,
                fill=color, outline=linea, width=2
            )
            c.create_line(
                120, 20, 200, 90, fill=linea, width=2
            )
            c.create_line(
                200, 90, 170, 115, fill=linea, width=2
            )
            c.create_line(
                50, 115, 200, 90,
                fill=linea, dash=(4, 3)
            )

        else:
            # Dibujo del cubo o prisma rectangular
            if self.nombre == "Cubo":
                x, y, w, h, dx, dy = 70, 57, 75, 75, 35, -25
            else:
                x, y, w, h, dx, dy = 45, 65, 110, 62, 42, -26

            c.create_polygon(
                x, y,
                x + dx, y + dy,
                x + w + dx, y + dy,
                x + w, y,
                fill="#e4f2fc", outline=linea, width=2
            )
            c.create_polygon(
                x + w, y,
                x + w + dx, y + dy,
                x + w + dx, y + h + dy,
                x + w, y + h,
                fill="#9cc9e9", outline=linea, width=2
            )
            c.create_rectangle(
                x, y, x + w, y + h,
                fill=color, outline=linea, width=2
            )

    def calcular(self):
        nombres, clase_figura = self.DATOS[self.nombre]
        valores = []

        for nombre_campo in nombres:
            texto = self.campos[nombre_campo].get().strip()

            if not texto:
                messagebox.showwarning(
                    "Campo vacío",
                    f"Ingrese {nombre_campo.lower()}.",
                    parent=self.ventana
                )
                return

            try:
                numero = float(texto.replace(",", "."))
            except ValueError:
                messagebox.showerror(
                    "Dato incorrecto",
                    f"{nombre_campo} debe ser numérico.",
                    parent=self.ventana
                )
                return

            if not math.isfinite(numero) or numero <= 0:
                messagebox.showerror(
                    "Dato incorrecto",
                    f"{nombre_campo} debe ser positivo y finito.",
                    parent=self.ventana
                )
                return

            valores.append(numero)

        try:
            figura = clase_figura(*valores)
            volumen = figura.volumen
            superficie = figura.superficie

            if not math.isfinite(volumen) or not math.isfinite(superficie):
                raise ValueError(
                    "Las dimensiones producen resultados demasiado grandes."
                )

        except (ValueError, OverflowError) as error:
            messagebox.showerror(
                "Dimensiones inválidas",
                str(error),
                parent=self.ventana
            )
            return

        self.volumen_texto.set(f"{volumen:.2f}")
        self.superficie_texto.set(f"{superficie:.2f}")

    def limpiar(self):
        for entrada in self.campos.values():
            entrada.delete(0, tk.END)

        self.volumen_texto.set("—")
        self.superficie_texto.set("—")


# Ventana principal
class VentanaPrincipal:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Ejercicio 8.3 - Figuras geométricas")
        self.raiz.resizable(False, False)

        panel = ttk.Frame(raiz, padding=22)
        panel.pack()

        ttk.Label(
            panel,
            text="Figuras geométricas",
            font=("Arial", 16, "bold")
        ).pack(pady=(0, 12))

        ttk.Label(
            panel,
            text="Seleccione una figura para calcular volumen y superficie"
        ).pack(pady=(0, 10))

        for nombre in VentanaFigura.DATOS:
            ttk.Button(
                panel,
                text=nombre,
                width=24,
                command=lambda n=nombre: self.abrir_figura(n)
            ).pack(pady=4)

    def abrir_figura(self, nombre):
        VentanaFigura(self.raiz, nombre)


def main():
    raiz = tk.Tk()
    VentanaPrincipal(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()
