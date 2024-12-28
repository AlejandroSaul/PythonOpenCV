import numpy as np

lista = [1,2,3]
array = np.array(lista)
# array [1 2 3]

array= np.arange(20)
# array [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

array= np.arange(5,20)
#array [ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

array= np.arange(5,20,2)
#array [ 5  7  9 11 13 15 17 19]

matriz = np.zeros(shape=(4,5))
'''
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
'''

aleatorios = np.random.randint(0,10,100)
'''[8 8 2 7 6 1 9 3 9 6 0 7 2 4 6 8 3 9 8 5 8 7 2 1 3 9 7 2 1 2 4 9 2 8 3 9 5
 9 3 1 6 8 0 3 8 5 3 3 2 6 4 7 7 8 1 4 4 9 1 5 5 8 0 6 1 7 9 4 9 7 9 5 4 5
 1 8 2 7 9 6 2 3 2 5 5 6 5 6 4 3 7 0 2 3 0 2 9 2 0 8]'''

posicionmax = aleatorios.argmax()
#Devuelve la primer posicion del maximo numero que encuentre inversa argmin

numeromaximo = aleatorios.max()
#devuelve el numero maximo del arreglo inversa min

aleatorios = aleatorios.reshape(5,20)
#Convierte el arreglo en matriz priero numero de filas luego numero de columnas
'''
[[0 8 5 8 6 6 0 0 4 9]
 [7 9 4 1 2 3 5 5 6 8]
 [5 5 2 3 6 3 9 4 4 2]
 [7 7 2 5 3 7 7 6 0 3]
 [4 8 5 4 2 0 4 7 2 8]
 [6 9 6 2 1 5 8 6 2 1]
 [3 3 5 3 0 6 8 5 1 2]
 [5 6 8 0 8 1 2 7 1 8]
 [7 0 7 7 2 6 2 4 1 0]
 [0 8 2 4 1 6 1 6 5 3]]'''

print(aleatorios)

print (numeromaximo)



