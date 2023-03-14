
# coding: utf-8

# In[ ]:


##################################################
###### Creado por: Esteban Restrepo Sierra     ###
###### Estudiante                              ###
###### Ingenieria de Telecomunicaciones        ###
##################################################
###### Docente: David Fernandez Mc Cann        ###
###### Procesamiento Digital de Imagenes       ###
######             2018-1                      ###
###### Resumen: Manipulacion de brillo en      ###
###### imagenes.                               ###
##################################################


# In[1]:


import numpy as np                              
from cv2 import *                               # Se importan todas las funciones de la libreria de Opencv

def brillo(imagen, m, E):                        # Funcion utilizada para manipulacion de brillo en la imagen
    epsilon = np.finfo(np.float).eps             # Se recoge informacion de cada uno de los pixeles de la imagen
    g = 1/(1+(m/(imagen + epsilon))**E)          # Se normaliza la imagen
    return g


# In[2]:


img = imread('paisaje.jpg')                      # Se lee imagen utilizando funcion de cv2

for i in range(1, 21):                           # Ciclo para aumentar brillo a la imagen
    suma = brillo(img, (200 - (i * 10)), 3)      # Se usa funcion brillo para llevar a los pixeles cada vez a 255 (Blanco)
    imshow('Imagen2', suma)                      # Se va mostrando el resultado de aplicar la operacion en los pixeles
    waitKey(0)                                   # Cada que se oprime una tecla se aplica de nuevo la operacion en los pixeles
destroyAllWindows()                              # Cuando el ciclo finaliza se destruyen todas las ventanas

sizeX, sizeY,Nchann = suma.shape                 # Se extraen caracteristicas de la imagen
print ('Las dimensiones de la imagen son', sizeX, 'X',sizeY, 'pixeles') # Se imprimen dimensiones de la imagen
print ('Tipo de dato de la imagen: ', suma.dtype) # Se obtiene es tipo de imagen
print ('Nivel de color mas alto', np.max(suma))   # Se obtiene el pixel con la intensidad mas alta
print ('Nivel de color mas bajo', np.min(suma))   # Se obtiene el pixel con la intensidad mas baja
print ('Nivel de color promedio', np.mean(suma))  # Se obtiene el promedio de todas las intensidades de la imagen
print ('Numero de canales',Nchann)                # Se obtiene el numero de canales de la imagen

  


# In[3]:


img1 = imread('paisaje.jpg')                     # Se lee imagen utilizando funcion de cv2

for i in range(1, 40):                           # Ciclo para disminuir brillo a la imagen
    resta = brillo(img1, (50 + (i * 10)), 3)     # Se usa funcion brillo para llevar a los pixeles cada vez a 0 (negro)
    imshow('Imagen3', resta)                     # Se va mostrando el resultado de aplicar la operacion en los pixeles
    waitKey(0)                                   # Cada que se oprime una tecla se aplica de nuevo la operacion en los pixeles
destroyAllWindows()                              # Cuando el ciclo finaliza se destruyen todas las ventanas

sizeX, sizeY,Nchann = resta.shape
print ('Las dimensiones de la imagen son', sizeX, 'X',sizeY, 'pixeles')
print ('Tipo de dato de la imagen: ', resta.dtype)
print ('Nivel de color mas alto', np.max(resta))
print ('Nivel de color mas bajo', np.min(resta))
print ('Nivel de color promedio', np.mean(resta))
print ('Numero de canales',Nchann)

