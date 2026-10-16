import tkinter as tk
import math


class Calculadora():
    def __init__(self, root):

        
        self.entry = tk.Entry(root, width=36, borderwidth=3,
                              font=("Arial", 18), justify="left")
        self.entry.config(state='readonly')
        self.entry.grid(row=0, column=0, columnspan=4,
                        sticky="w", padx=5, pady=5)

        self.boton_borrar = tk.Button(
            root, text="⌫", width=5, height=1,
            font=("Arial", 13),
            command=lambda: self.borrar_caracter()
        )
        self.boton_borrar.grid(row=0, column=4, padx=3, pady=5)

        
        self.boton_7 = tk.Button(root, text="7", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(7))
        self.boton_7.grid(row=1, column=0)

        self.boton_8 = tk.Button(root, text="8", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(8))
        self.boton_8.grid(row=1, column=1)

        self.boton_9 = tk.Button(root, text="9", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(9))
        self.boton_9.grid(row=1, column=2)

        self.boton_suma = tk.Button(root, text="+", width=10, height=2,
                                    font=("Arial", 12),
                                    command=lambda: self.click("+"))
        self.boton_suma.grid(row=2, column=3)



        self.boton_dms = tk.Button(root, text="DMS", width=10, height=2,
                                   font=("Arial", 12),
                                   command=lambda: self.grados_minutos_segundos())
        self.boton_dms.grid(row=1, column=4)

        self.boton_clear = tk.Button(root, text="C", width=10, height=2,
                                     font=("Arial", 12),
                                     command=lambda: self.clear())
        self.boton_clear.grid(row=1, column=3)
        

        
        self.boton_4 = tk.Button(root, text="4", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(4))
        self.boton_4.grid(row=2, column=0)

        self.boton_5 = tk.Button(root, text="5", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(5))
        self.boton_5.grid(row=2, column=1)

        self.boton_6 = tk.Button(root, text="6", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(6))
        self.boton_6.grid(row=2, column=2)

        self.boton_resta = tk.Button(root, text="-", width=10, height=2,
                                     font=("Arial", 12),
                                     command=lambda: self.click("-"))
        self.boton_resta.grid(row=2, column=4)

        # Tercera fila
        self.boton_1 = tk.Button(root, text="1", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(1))
        self.boton_1.grid(row=3, column=0)

        self.boton_2 = tk.Button(root, text="2", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(2))
        self.boton_2.grid(row=3, column=1)

        self.boton_3 = tk.Button(root, text="3", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(3))
        self.boton_3.grid(row=3, column=2)

        self.boton_multiplicacion = tk.Button(
            root, text="*", width=10, height=2, font=("Arial", 12),
            command=lambda: self.click("*"))
        self.boton_multiplicacion.grid(row=3, column=3)

        self.boton_vacio = tk.Label(root, text="", width=10)
        self.boton_vacio.grid(row=3, column=4)

        
        self.boton_0 = tk.Button(root, text="0", width=10, height=2,
                                 font=("Arial", 12),
                                 command=lambda: self.click(0))
        self.boton_0.grid(row=4, column=1)

        self.boton_coma = tk.Button(root, text=",", width=10, height=2,
                                    font=("Arial", 12),
                                    command=lambda: self.click("."))
        self.boton_coma.grid(row=4, column=0)

        self.boton_igual = tk.Button(root, text="=", width=10, height=2,
                                     font=("Arial", 12),
                                     command=lambda: self.igual())
        self.boton_igual.grid(row=4, column=2)

        self.boton_division = tk.Button(root, text="/", width=10, height=2,
                                        font=("Arial", 12),
                                        command=lambda: self.click("/"))
        self.boton_division.grid(row=3, column=4)
        
        self.boton_parentesis1 = tk.Button(
            root, text="(", width=10, height=2, font=("Arial", 12),
            command=lambda: self.click("("))
        self.boton_parentesis1.grid(row=4, column=3)

        self.boton_parentesis2 = tk.Button(
            root, text=")", width=10, height=2, font=("Arial", 12),
            command=lambda: self.click(")"))
        self.boton_parentesis2.grid(row=4, column=4)        
        
    def click(self, num):
        self.entry.config(state='normal')
        temporal = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, temporal + str(num))
        self.entry.config(state='readonly')

    def clear(self):
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.config(state='readonly')
    
    def igual(self):
        expresion = self.entry.get()
        expresion = expresion.replace("^", "**")

        if expresion != "":
            resultado = eval(expresion)
            self.mostrar_resultado(resultado)
    
    def borrar_caracter(self):
        self.entry.config(state='normal')
        temporal = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, temporal[:-1])
        self.entry.config(state='readonly')

    def mostrar_resultado(self, resultado):
        if isinstance(resultado, (int, float)):
            if isinstance(resultado, float):
                if resultado.is_integer():
                    resultado = int(resultado)
                else:
                    resultado = round(resultado, 10)

        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(resultado))
        self.entry.config(state='readonly')


class CalculadoraCientifica(Calculadora):
    def __init__(self, root):
        super().__init__(root)

        
        self.boton_coseno = tk.Button(
            root, text="cos", width=10, height=2, font=("Arial", 12),
            command=lambda: self.coseno())
        self.boton_coseno.grid(row=6, column=0)

        self.boton_seno = tk.Button(
            root, text="sin", width=10, height=2, font=("Arial", 12),
            command=lambda: self.seno())
        self.boton_seno.grid(row=6, column=1)

        self.boton_tangente = tk.Button(
            root, text="tan", width=10, height=2, font=("Arial", 12),
            command=lambda: self.tan())
        self.boton_tangente.grid(row=6, column=2)

        self.boton_raiz = tk.Button(
            root, text="√", width=10, height=2, font=("Arial", 12),
            command=lambda: self.sqr_root())
        self.boton_raiz.grid(row=6, column=3)

        self.boton_raiz_cubica = tk.Button(
            root, text="∛", width=10, height=2, font=("Arial", 12),
            command=lambda: self.cube_root())
        self.boton_raiz_cubica.grid(row=6, column=4)

        
        self.boton_potencia = tk.Button(
            root, text="x²", width=10, height=2, font=("Arial", 12),
            command=lambda: self.power())
        self.boton_potencia.grid(row=7, column=0)

        self.boton_cubo = tk.Button(
            root, text="x³", width=10, height=2, font=("Arial", 12),
            command=lambda: self.cube())
        self.boton_cubo.grid(row=7, column=1)

        self.boton_potencia_y = tk.Button(
            root, text="xʸ", width=10, height=2, font=("Arial", 12),
            command=lambda: self.click("^"))
        self.boton_potencia_y.grid(row=7, column=2)

        self.boton_factorial = tk.Button(
            root, text="n!", width=10, height=2, font=("Arial", 12),
            command=lambda: self.factorial())
        self.boton_factorial.grid(row=7, column=3)

        self.boton_pi = tk.Button(
            root, text="π", width=10, height=2, font=("Arial", 12),
            command=lambda: self.click(math.pi))
        self.boton_pi.grid(row=7, column=4)

    def coseno(self):
        numero = float(self.entry.get().replace(",", "."))
        resultado = math.cos(math.radians(numero))
        self.mostrar_resultado(resultado)

    def seno(self):
        numero = float(self.entry.get().replace(",", "."))
        resultado = math.sin(math.radians(numero))
        self.mostrar_resultado(resultado)

    def tan(self):
        numero = float(self.entry.get().replace(",", "."))
        resultado = math.tan(math.radians(numero))
        self.mostrar_resultado(resultado)

    def sqr_root(self):
        numero = float(self.entry.get().replace(",", "."))
        resultado = math.sqrt(numero)
        self.mostrar_resultado(resultado)

    def cube_root(self):
        numero = float(self.entry.get().replace(",", "."))
        resultado = numero ** (1 / 3)
        self.mostrar_resultado(resultado)

    def power(self):
        numero = float(self.entry.get().replace(",", "."))
        resultado = math.pow(numero, 2)
        self.mostrar_resultado(resultado)

    def cube(self):
        numero = float(self.entry.get().replace(",", "."))
        resultado = math.pow(numero, 3)
        self.mostrar_resultado(resultado)

    def factorial(self):
        numero = int(self.entry.get())
        resultado = math.factorial(numero)
        self.mostrar_resultado(resultado)

    def grados_minutos_segundos(self):
        numero = self.entry.get()

       
        if "°" in numero:
            numero = numero.replace("°", " ")
            numero = numero.replace("'", " ")
            numero = numero.replace('"', " ")
            partes = numero.split()

            grados = float(partes[0])
            minutos = float(partes[1]) if len(partes) > 1 else 0
            segundos = float(partes[2]) if len(partes) > 2 else 0

            if grados < 0:
                resultado = grados - minutos / 60 - segundos / 3600
            else:
                resultado = grados + minutos / 60 + segundos / 3600

            self.mostrar_resultado(resultado)

        else:
            numero = float(numero.replace(",", "."))

            grados = int(numero)
            minutos_decimal = abs(numero - grados) * 60
            minutos = int(minutos_decimal)
            segundos = (minutos_decimal - minutos) * 60

            resultado = (
                str(grados) + "° " +
                str(minutos) + "' " +
                str(round(segundos, 2)) + '"'
            )

            self.mostrar_resultado(resultado)


root = tk.Tk()
root.title("Calculadora Cientifica")
root.geometry("570x430")
root.resizable(False, False)

appCalculadora = CalculadoraCientifica(root)

root.mainloop()
