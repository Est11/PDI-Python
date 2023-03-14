
# coding: utf-8

# In[2]:


##################################################
###### Creado por: Esteban Restrepo Sierra     ###
###### Estudiante                              ###
###### Ingenieria de Telecomunicaciones        ###
##################################################
###### Docente: David Fernandez Mc Cann        ###
###### Procesamiento Digital de Imagenes       ###
######             2018-1                      ###
###### Resumen: Identificacion palabras en un  ###
###### texto.                                  ###
##################################################

from skimage import color
from scipy import ndimage
import matplotlib.pyplot as plt                  
import numpy as np
from cv2 import *                                 # Se importan todas las funciones de la libreria de Opencv

fig=plt.figure(figsize=(12,6))                    # Lo que se grafique quede mas grande en el notebook

texto=imread('texto.png',0)                       # Se lee directamente imagen en escala de grises sin tener que convertirla luego
textorot = ndimage.rotate(texto, -90)             # Se rota imagen 270º o -90ª

imshow('Texto',texto)                             # Se muestra imagen usando comando de cv2
waitKey(0)                                        # Se espera que se oprima una tecla
destroyAllWindows()                               # Se cierran todas las ventanas

imshow('Texto rotado',textorot)                   # Se muestra imagen usando comando de cv2
waitKey(0)                                        # Se espera que se oprima una tecla
destroyAllWindows()                               # Se cierran todas las ventanas

suma=sum(textorot)                                # Suma las intensidades del texto

plt.plot(suma)                                    # Se grafica suma de intensidades en el texto
plt.title('Suma de intensidades en el texto',fontsize=24)# Titulo para la suma de intensidades (fontsize permite escoger tamaño de letra)
plt.xlabel('Letras',fontsize=18)                  # Etiqueta para eje x de la grafica
plt.ylabel('Intensidad',fontsize=18)              # Etiqueta para eje y de la grafica
plt.grid(True)                                    # Se agrega una cuadricula a la grafica 
plt.show()                                        # Comando que se utiliza para mostrar en notebook


# In[5]:


texto=imread('texto.png')                               # Se lee imagen usando comando de cv2
textr=texto[0:23,20:60,:]                               # Se recorta un palabra del texto

textrg=color.rgb2gray(textr)                            # Se convierte imagen a escala de grises con funcion de libreria color

imshow('Texto recortado',textr)                         # Se muestra palabra recortada del texto
waitKey(0)                                              # Se espera que se oprima una tecla
destroyAllWindows()                                     # Se cierran todas las ventanas


# In[6]:


suma1=sum(textrg)                                       # Se suman las intensidades de la palabra recortada

plt.plot(suma1)                                         # Se grafica suma de intensidades de la palabra
plt.title('Suma de intensidades palabra',fontsize=25)   # Titulo para la suma de las intensidades de la palabra
plt.xlabel('Letras',fontsize=18)                        # Etiqueta para eje x de la grafica
plt.ylabel('Intensidades',fontsize=18)                  # Etiqueta para eje y de la grafica
plt.grid(True)                                          # Se agrega una cuadricula a la grafica 
plt.show()                                              # Comando que se utiliza para mostrar en notebook


# In[7]:


#de 12 a 18 la i
letra=textr[:,3:12,:]                                  # Se recorta una letra de la palabra anterior

imshow('Letra',letra)                                  # Se muestra letra recortada de la palabra
waitKey(0)                                             # Se espera que se oprima una tecla
destroyAllWindows()                                    # Se cierran todas las ventanas

