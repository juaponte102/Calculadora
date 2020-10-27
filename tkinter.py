# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:09:01 2020

@author: jdapo
"""

import tkinter as tk
from tkinter import ttk
def init_window():
    window = tk.Tk() #crea la pantalla
    window.title("Calculadora   ")#Título de la pantalla
    window.geometry('400x250')#Dimensiones de la pantalla
    #Texto principal o título, con sus posibles configuraciones, fuente y tamaño 
    label = tk.Label(window, text = "CALCULADORA", font = ("Arial bold", 15))
    label.grid(column = 0, row = 0) #Define el lugar donde estará la etiqueta
    #Seleccione los campos de texto
    label_entrada1 = tk.Label(window,text = "Ingrese el primer número", font = ("Arial bold", 10))
    label_entrada1.grid(column = 0, row = 1)
    
    label_entrada2 = tk.Label(window,text = "Ingrese el segundo número", font = ("Arial bold", 10))
    label_entrada2.grid(column = 0, row = 2)
    
    entrada1 = tk.Entry(window, width = 10)
    entrada2 = tk.Entry(window, width = 10)
    
    entrada1.focus()
    entrada2.focus()
    
    entrada1.grid(column = 1, row = 1)
    entrada2.grid(column = 1, row = 2)
    #Agrege las etiquetas para que el usuario sepa los datos que debemos ingresar
    #Crear una etiqueta para el seleccionador(combox)
    label_operador = tk.Label(window , text = "Escoja un operador" , font = ("Arial bold", 10))
    label_operador.grid(column = 0, row = 3)
    #Crear un seleccionador (combobox):
    combo_operadores = ttk.Combobox(window)
    #Asignar los valores del seleccionador a traves de su atributo values:
    combo_operadores["values"] = ["+", "-", "*","/","pow"]
    #Asignar por defecto una opcion seleccionada: 0 es el índice de los valores:
    combo_operadores.current(0) # selecciona el item
    #Ubicar el seleccionador:
    combo_operadores.grid(column  =1, row = 3)
    #Agregar etiqueta para mostrar el resultado de la operacion en pantalla:
    label_resultado = tk.Label(window, text = "Resultado: ", font = ("Arial bold" , 15))
    label_resultado.grid(column = 0, row = 5)
    boton = tk.Button(window,
                    command = lambda: click_calcular(
                            label_resultado,entrada1.get(),
                            entrada2.get(),
                            combo_operadores.get()),
                    text = "calcular",
                    bg = "purple",
                    fg = "green")
    boton.grid(column = 1, row =  4)      
    window.mainloop()
def calculadora(num1, num2, operador):
    if operador == "+":
        resultado = num1 + num2      
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2
    else:
        resultado = num1 ** num2
    
    return resultado
def click_calcular (label, num1,num2,operador):
    #Conversion de valores:
    valor1 = float(num1)
    valor2 = float(num2)
    #Calculo dados los valores y el operador:
    res = calculadora(valor1, valor2, operador)
    #Actualización de texto en la etiqueta:
    label.configure(text = "Resultado: " + str(int(res)))
          
                          
def main():
    init_window()  

main()