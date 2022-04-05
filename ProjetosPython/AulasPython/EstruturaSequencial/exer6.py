# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import numpy as pg

raio = float(input("Informe o raio do círculo: "))
area = pg.pi * raio**2

print("A área do círculo é: {:.2f}".format(area))
