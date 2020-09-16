#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from termcolor import *
from random import *

banner = """                             000      00
                           0000000   0000
              0      00  00000000000000000
            0000 0  000000000000000000000000       0
         000000000000000000000000000000000000000 000
        0000000000000000000000000000000000000000000000
    000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000
              / / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
            / / / / / / / / / / / / / / /
          / / / / / / / / / / / / / /
          / / / / / / / / / / / / /
        / / / / / / / / / / / /
        / / / / / / / / / /

         ...........CC RAIN OwO!."""

def main():
    global gmm
    global gyy
    global gcvv
    global gcc
    print(colored(banner, "blue"))
    print("\nEjemplo de BIN: 53659563362XXXXX")
    bin = input(colored("Ingresa BIN: ", "yellow"))
    print("\nEjemplo de Mes: 05 o da ENTER para numero Random")
    mm = input(colored("Ingresa mes: ", "yellow"))
    print("\nEjemplo de Año: 2020 o da ENTER para numero Random")
    yy = input(colored("Ingresa año: ", "yellow"))
    print("\nEjemplo de CVV: 152 o da ENTER para numero Random")
    cvv = input(colored("Ingresa CVV: ", "yellow"))
    print("\nEjemplo de nombre: rojas.txt")
    archivo = input(colored("Ingresa el nombre del archivo para las CCs: ", "yellow"))
    print("\nEjemplo de cantidad: 50")
    cantidad = int(input(colored("Ingresa la cantidad de CCs: ", "yellow")))
    print(colored("\nGenerando ....\n", "magenta"))
    for n in range(cantidad):
        gcc = ""
        for l in bin:
            l = l.replace("X", str(randint(0,9)))
            gcc = gcc + l
        if mm == "":
            gmm = str(choice(["01","02","03","04","05","06","07","08","09","10","11","12"]))
        else:
            gmm = str(mm)
        if yy == "":
            gyy = str(choice(["2020","2021","2022","2023","2024","2025","2026"]))
        else:
            gyy = str(yy)
        if cvv == "":
            gcvv = str(randint(100,999))
        else:
            gcvv = str(cvv)
        datos = "{}|{}|{}|{}".format(gcc, gmm, gyy, gcvv)
        print(colored(datos, "green"))
        with open(archivo, "a") as f:
            f.write(datos+"\n")
    print("\n")
if __name__ == '__main__':
    main()
