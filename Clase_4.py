
# coding: utf-8

# In[1]:


##################################################
###### Creado por: Esteban Restrepo Sierra     ###
###### Estudiante                              ###
###### Ingenieria de Telecomunicaciones        ###
##################################################
###### Docente: David Fernandez Mc Cann        ###
###### Procesamiento Digital de Imagenes       ###
######             2018-1                      ###
###### Resumen: Histograma de una imagen y     ###
###### binarizacion.                           ###
##################################################

import matplotlib.pyplot as plt                  
import numpy as np
from cv2 import *                                 # Se importan todas las funciones de la libreria de Opencv

batman=imread('batman.jpg',0)                     # Se lee directamente imagen en escala de grises sin tener que convertirla luego

imshow('Gray',batman)                             # Se muestra imagen en escala de grises usando comando de cv2
waitKey(0)                                        # Se espera que se oprima una tecla
destroyAllWindows()                               # Se cierran todas las ventanas

histo=calcHist([batman], [0], None, [256], [0,256]) # Se calcula el histograma para la imagen anterior

plt.plot(histo)                                     # Se grafica el histograma utilizando libreria matplotlib.pyplot
plt.xlabel("Intensidad",fontsize=18)                # Etiqueta para eje x de la grafica
plt.ylabel("Frecuencia",fontsize=18)                # Etiqueta para eje y de la grafica
plt.title("Histograma escala de grises",fontsize=24)# Titulo para el histograma (fontsize permite escoger tamaño de letra)
plt.grid(True)                                      # Se agrega una cuadricula a la grafica 
plt.show()                                          # Comando que se utiliza para mostrar en notebook


# In[2]:


batmanred=imread('batman.jpg')                         # Se lee imagen utilizando funcion de cv2
batmanred[:,:,0]=0                                     # Eliminamos el color verde de la imagen
batmanred[:,:,1]=0                                     # Eliminamos el color azul de la imagen

imshow('Batmanred',batmanred)                          # Se muestra imagen solo con componente roja usando comando de cv2
waitKey(0)                                             # Se espera que se oprima una tecla
destroyAllWindows()                                    # Se cierran todas las ventanas

histor=calcHist([batmanred], [0], None, [256], [0,256]) # Se calcula el histograma para la imagen anterior

plt.plot(histor)                                    # Se grafica el histograma utilizando libreria matplotlib.pyplot
plt.xlabel("Intensidad",fontsize=18)                # Etiqueta para eje x de la grafica
plt.ylabel("Frecuencia",fontsize=18)                # Etiqueta para eje y de la grafica
plt.title("Histograma Rojo",fontsize=24)            # Titulo para el histograma (fontsize permite escoger tamaño de letra)
plt.grid(True)                                      # Se agrega una cuadricula a la grafica 
plt.show()                                          # Comando que se utiliza para mostrar en notebook


# In[3]:


batmanblue=imread('batman.jpg')                           # Se lee imagen utilizando funcion de cv2
batmanblue[:,:,1]=0                                       # Eliminamos el color rojo de la imagen
batmanblue[:,:,2]=0                                       # Eliminamos el color verde de la imagen

imshow('Batmanblue',batmanblue)                           # Se muestra imagen solo con componente azul usando comando de cv2
waitKey(0)                                                # Se espera que se oprima una tecla
destroyAllWindows()                                       # Se cierran todas las ventanas

histob=calcHist([batmanblue], [0], None, [256], [0,256])   # Se calcula el histograma para la imagen anterior

plt.plot(histob)                                    # Se grafica el histograma utilizando libreria matplotlib.pyplot
plt.xlabel("Intensidad",fontsize=18)                # Etiqueta para eje x de la grafica
plt.ylabel("Frecuencia",fontsize=18)                # Etiqueta para eje y de la grafica
plt.title("Histograma Azul",fontsize=24)            # Titulo para el histograma (fontsize permite escoger tamaño de letra)
plt.grid(True)                                      # Se agrega una cuadricula a la grafica 
plt.show()                                          # Comando que se utiliza para mostrar en notebook


# In[4]:


batmangreen=imread('batman.jpg')                               # Se lee imagen utilizando funcion de cv2
batmangreen[:,:,0]=0                                      # Eliminamos el color rojo de la imagen
batmangreen[:,:,2]=0                                      # Eliminamos el color azul de la imagen

imshow('Batmangreen',batmangreen)                         # Se muestra imagen solo con componente verde usando comando de cv2
waitKey(0)                                                # Se espera que se oprima una tecla
destroyAllWindows()                                       # Se cierran todas las ventanas

histog=calcHist([batmangreen], [0], None, [256], [0,256])  # Se calcula el histograma para la imagen anterior

plt.plot(histog)                                    # Se grafica el histograma utilizando libreria matplotlib.pyplot
plt.xlabel("Intensidad",fontsize=18)                # Etiqueta para eje x de la grafica
plt.ylabel("Frecuencia",fontsize=18)                # Etiqueta para eje y de la grafica
plt.title("Histograma Verde",fontsize=24)           # Titulo para el histograma (fontsize permite escoger tamaño de letra)
plt.grid(True)                                      # Se agrega una cuadricula a la grafica 
plt.show()                                          # Comando que se utiliza para mostrar en notebook



# In[5]:


batman=imread('batman.jpg',0)                # Se lee directamente imagen en escala de grises sin tener que convertirla luego

umbr = 80                                    # Se define un umbral                             
umbr1 = np.where(batman>umbr)                # Se usa funcion Where de libreria numpy para discriminar los pixeles con intensidad
                                             # mayor que la del umbral
umbr2 = np.where(batman <= umbr)             # Se usa funcion Where de libreria numpy para discriminar los pixeles con intensidad
                                             # menor o igual que la del umbral

batman[umbr1] = 0                            # Los pixeles que cumplan la primera condicion se llevan a negro
batman[umbr2] = 255                          # Los pixeles que cumplan la segunda condicion se llevan a blanco

imshow('Binarizada',batman)                  # Se muestra imagen binarizada utilizando funcion de libreria cv2
waitKey(0)                                   # Se espera que se oprima una tecla
destroyAllWindows()                          # Se cierran todas las ventanas

