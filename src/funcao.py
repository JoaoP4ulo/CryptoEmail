import string
import numpy as np
import random





alfabeto = ['',' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'à', 'â', 'ã', 'é', 'è', 'ê', 'í', 'ï', 'ó', 'ô', 'õ', 'ö', 'ú', 'ç', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Á', 'À', 'Â', 'Ã', 'É', 'È', 'Ê', 'Í', 'Ï', 'Ó', 'Ô', 'Õ', 'Ö', 'Ú', 'Ç', '!', '"', '#', '$', '%', '&', "'", '(', ')', 
'*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

num_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 
113, 114, 115]


def letra_em_numero(string):

    lista_string = list(string)

    for i in range(len(alfabeto)):
        for x in range(len(lista_string)):
            if lista_string[x] == alfabeto[i]:
                lista_string[x] = num_lista[i]

    return lista_string


def transformar_matriz(lista_string):
    matriz_int=[]
    matriz_ext=[]
    
    tam_frase = len(lista_string)

    while tam_frase%4 != 0:
        lista_string.append(0)
        tam_frase = len(lista_string)
    num_matriz=tam_frase//2

    splited = [lista_string[i::num_matriz] for i in range(num_matriz)]
    while len(splited) != 0:
        matriz_int,splited=matriz_formar(splited)
        matriz_ext.append(matriz_int)
    

    return matriz_ext

def matriz_formar(matriz):
    matriz_int=[]
    
    for i in range(2):
        matriz_int.append(matriz[i])
    
    if len(matriz) != 0:    
        del matriz[:2]

    return matriz_int,matriz



def codifiar(A,B):
    result=[[0,0],[0,0]]
    for i in range(len(A)): 
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                result[i][j] += round((A[i][k]) * (B[k][j])) 

    return result

def formar_frase(matriz):
    lista = []
    lista_frase = []

    for x in range(len(matriz)):
        for y in range(2):
    
            aux = matriz[x][y]
            lista.append(aux)

    for i in range(2):
        for j in range(len(lista)):
            lista_frase.append(lista[j][i])

    return lista_frase

def numero_em_letra(lista):

    for i in range(len(alfabeto)):
        for x in range(len(lista)):
            if lista[x] == num_lista[i]:
                lista[x] = alfabeto[i]

    return lista

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for x in range(2):
            print(f"{matriz[i][x]}")
        print("\n")

def criar_chave():
    chave=[]
    linha=[]

    for i in range(2):
        for k in range(2):
            numero_aleatorio = random.randint(-1000, 1000)
            linha.append(numero_aleatorio)
        chave.append(linha)
        linha=[]
        
    return str(chave)
