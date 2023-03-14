
# coding: utf-8

# In[4]:


##################################################
###### Creado por: Esteban Restrepo Sierra     ###
###### Estudiante                              ###
###### Ingenieria de Telecomunicaciones        ###
##################################################
###### Docente: David Fernandez Mc Cann        ###
###### Procesamiento Digital de Imagenes       ###
######             2018-1                      ###
###### Resumen: Ecualizacion de histograma.    ###
##################################################


import matplotlib.pyplot as plt                  
import numpy as np
from cv2 import *                                   # Se importan todas las funciones de la libreria de Opencv

fig=plt.figure(figsize=(10,12))                     # Lo que se grafique quede mas grande en el notebook

a=imread('arroces.png',0)                           # Se lee directamente imagen en escala de grises sin tener que convertirla luego

imshow('Arroces',a)                                 # Se muestra imagen en escala de grises usando comando de cv2
waitKey(0)                                          # Se espera que se oprima una tecla
destroyAllWindows()                                 # Se cierran todas las ventanas

histo=calcHist([a], [0], None, [256], [0,256])      # Se calcula el histograma para la imagen anterior
imgeq=equalizeHist(a)
histoeq=calcHist([imgeq], [0], None, [256], [0,256])# Se calcula el histograma para la imagen anterior

plt.subplot(211)
plt.plot(histo)                                     # Se grafica el histograma utilizando libreria matplotlib.pyplot
plt.xlabel("Intensidad",fontsize=18)                # Etiqueta para eje x de la grafica
plt.ylabel("Frecuencia",fontsize=18)                # Etiqueta para eje y de la grafica
plt.title("Histograma escala de grises",fontsize=24)# Titulo para el histograma (fontsize permite escoger tamaño de letra
plt.grid(True)                                      # Se agrega una cuadricula a la grafica 

plt.subplot(212)
plt.plot(histoeq)                                   # Se grafica el histograma dcualizado utilizando libreria matplotlib.pyplot
plt.xlabel("Intensidad",fontsize=18)                # Etiqueta para eje x de la grafica
plt.ylabel("Frecuencia",fontsize=18)                # Etiqueta para eje y de la grafica
plt.title("Histograma ecualizado escala de grises",fontsize=24)# Titulo para el histograma (fontsize permite escoger tamaño de letra
plt.grid(True)                                      # Se agrega una cuadricula a la grafica 

plt.tight_layout()                                  # Para separar los dos subplots
plt.show()                                          # Comando que se utiliza para mostrar en notebook

imshow('Arroces con histo eq',imgeq)                # Se grafica imagen luego de ecualizar el histograma
waitKey(0)                                          # Se espera que se oprima una tecla
destroyAllWindows()                                 # Se cierran todas las ventanas

