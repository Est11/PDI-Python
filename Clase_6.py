
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
###### Resumen: Cambio de espacio de color     ###
###### y descomposicion en componentes RGB.    ###
##################################################


# In[1]:


from cv2 import *                                  # Se importan todas las funciones de la libreria de Opencv
import numpy as np
import funciones as fun                            # Se importa archivo donde se crearon las funciones 

a=imread('carro1.png')                             # Se lee la imagen utilizando funcion de libreria cv2

imshow('carro',a)                                  # Se muestra imagen utilizando funcion de libreria cv2
waitKey(0)                                         # Se espera que se oprima una tecla
destroyAllWindows()                                # Se cierran todas las ventanas


# In[2]:


a_hsv = cvtColor(a, COLOR_BGR2HSV)                 # Se realiza una transformacion de espacio de RGB a HSV usando funcion de cv2

imshow('Espacio de color HSV',a_hsv)               # Se muestra imagen en espacio HSV
waitKey(0)                                         # Se espera que se oprima una tecla
destroyAllWindows()                                # Se cierran todas las ventanas


# In[3]:


a_rgb=fun.chori(a)                                 # Se aplica funcion chori para descomponer una imagen en RGB.
a_hsv_rgb=fun.chori(a_hsv)                         # Se aplica funcion chori para descomponer en RGB imagen en espacio HSV

imshow('Componentes RGB original y HSV',a_rgb)     # Se muestra imagen RGB en sus componentes
waitKey(0)                                         # Se espera que se oprima una tecla
destroyAllWindows()                                # Se cierran todas las ventanas

imshow('Componentes RGB de HSV',a_hsv_rgb)         # Se muestra imagen HSV en componentes RGB
waitKey(0)                                         # Se espera que se oprima una tecla
destroyAllWindows()                                # Se cierran todas las ventanas


# Para el laboratorio 5 donde  se necesita de un plot saber la posicion del cursor para definir las coordenadas exactas de un punto en particular, se recomienda utilizar la libreria matplotlib.pyplot alias plt para limitar los plots en el eje X y eje Y.
# 
# plt.xlim(inicio,final)
# plt.ylim(inicio,final)
# 
# El comando np.vstack(obj1,obj2,obj2) realiza un apilamiento de una o varias imagenes verticalmente, tienen que coincidir en el numero de columnas las mismas.
# 
# El comando np.hstack(obj1,obj2,obj2) realiza un apilamiento de una o varias imagenes horizontalmente, tienen que coincidir en el numero de filas las mismas.
