# Programa que simula el funcionamiento de la maquina de galton el cual se realizo para 3000 canicas y 12 niveles
# pero se pueden ajustar estas dos variables para cambiar el numero de niveles y la cantidad de canicas y 
# el código se reajustara automáticamente

import random
import matplotlib.pyplot as plt

canicas = 3000 #numero de canicas
niveles = 12 #cantidad de niveles a utilizar
histograma = [0] * (niveles * 2) #lista que almacenara el histograma

def llenar_histograma_galton(niveles, histograma, canicas):
    """_summary_
    Args:
        niveles (int): niveles de que desean simularse
        histograma (list): lista que almacenara el resultado
        canicas (int): cantidad de canicas que se usaran en el sumulado
    Returns:
        lis: retorna una lista con el resultado optenido
    """
    pos = None
    for i in range(canicas):
        pos = niveles - 1
        for j in range(niveles):
            result = random.randint(0,1)
            if j == 0 and result == 0:
                pos = 11        
            elif result == 0:
                pos -= 1
            else:
                pos += 1
        histograma[pos] += 1
    return histograma

def imprimir_grafica(histograma):
    """_summary_
    Args:
        histograma (list): lista que contiene los resultados que se imprimiran en el diagrama
    """
    distribucion = list(range(1,len(histograma) + 1))  
    plt.figure(figsize=(9, 6))
    plt.bar(distribucion, histograma)
    plt.xticks(range(len(histograma)), distribucion)
    plt.xlabel("Distribución de Canicas")
    plt.ylabel("Cantidad de Canicas")
    plt.title("Simulación de la Máquina de Galton") 
    plt.show()

imprimir_grafica(llenar_histograma_galton(niveles, histograma, canicas))
