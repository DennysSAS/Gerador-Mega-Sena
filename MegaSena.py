import random 

jogos = int(input("Numero de jogos: "))

## Função de geração de numeros randomicos

def gerador():
    quadrante = [[4, 11, 13, 23, 24], [6, 10, 30, 28, 16, 27, 17, 29], [32, 33, 34, 35, 41, 42, 43, 44, 51, 53, 54], [36, 38, 49, 56]]
    random_num1 = random.choice(quadrante[0])
    random_num2 = random.choice(quadrante[1])
    random_num3 = random.choice(quadrante[2])
    random_num4 = random.choice(quadrante[3])
    random_num5 = random.choice(quadrante[2])
    random_num6 = random.choice(quadrante[1])

    n_completo = ("{} {} {} {} {} {}".format(random_num1, random_num2, random_num3, random_num4, random_num5, random_num6))
    print (n_completo)

## Laço de repetição

def exec():
   contador = 0 
   while jogos > contador:
       gerador()
       contador = contador + 1        

exec()