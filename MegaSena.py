#!/usr/bin/env python3
import random
from tkinter import N 


jogos = int(input("Numero jogos: "))
numero_jogado = input("Numero jogado: ")
## Função de geração de numeros randomicos
def test():
    quadrante = [range(0, 100)]

    random_num1 = random.choice(quadrante[0])
    if random_num1 <= 9:
        random_num1 = "{}{}".format(0,random_num1)

    random_num2 = random.choice(quadrante[0])
    if random_num2 <= 9:
        random_num2 = "{}{}".format(0,random_num2)

    random_num3 = random.choice(quadrante[0])
    if random_num3 <= 9:
        random_num3 = "{}{}".format(0,random_num3)

    random_num4 = random.choice(quadrante[0])
    if random_num4 <= 9:
        random_num4 = "{}{}".format(0,random_num4)

    random_num5 = random.choice(quadrante[0])
    if random_num5 <= 9:
        random_num5 = "{}{}".format(0,random_num5)

    random_num6 = random.choice(quadrante[0])
    if random_num6 <= 9:
        random_num6 = "{}{}".format(0,random_num6)

    print ("|{}|{}|{}|{}|{}|{}|".format(random_num1, random_num2, random_num3, random_num4, random_num5, random_num6))


## Validação

## Laço de repetição
contador = 0
while contador < jogos:
    contador = contador + 1
    test()


