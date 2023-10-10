
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
###### Resumen: Extraer placa completamente.   ###
##################################################


# In[6]:


from cv2 import *                              # Se importan todas las funciones de la libreria de Opencv
import numpy as np
import matplotlib.pyplot as plt

a=imread('placa_bin.bmp',0)                    # Se lee la placa binarizada usando funcion de la libreria cv2

imshow('Placa binarizada',a)                   # Se muestra placa binarizada usando funcion de la libreria cv2
waitKey(0)                                     # Se espera a que se oprima una tecla
destroyAllWindows()                            # Se destruyen todas las ventanas abiertas

ret, labels=connectedComponents(a)             # Funcion de cv2 utilizada para etiquetar las figuras de la imagen
                                               # hace las veces de bwlabel en matlab
for i in range(1,ret):                         # Se recorre la imagen 
    c=a*0                                      # Se crea una matriz en ceros con las dimensiones de la imagen
    ind=np.where(labels==i)                    # Se recorren las etiquetas de la imagen 
    c[ind]=1                                   # A cada pixel se les lleva el valor de 1
    suma=sum(c)                                # Se suman los pixeles de todas las figuras 
    total=sum(suma)                            # Se suman esos valores de los pixeles para hallar areas de objetos
    if total > 2500:                           # Aproximar area de la placa en pixeles usando libreria IV usada en clase 1
        area=total                             # Se lleva area de la placa a una vble nueva
        break                                  # Cuando se encuentre la placa se rompe el ciclo
        
c=a*0                                          # Se crea una matriz con las dimensiones de la imagen original
ind1=np.where(labels==area)                    # Se crean unos indices en donde las etiquetas sean igual al area de la placa
c[ind]=255                                     # En la imagen se llevan estos indices a color blanco

imshow('Solo placa',c)                         # Se muestra la imagen solo con la placa usando funcion de libreria cv2
waitKey(0)                                     # Se espera hasta que se oprima una tecla
destroyAllWindows()                            # Se destruyen todas las ventanas creadas

x,y=np.where(c>0)                              # Se extraen las secciones de la placa donde la intensidad sea mayor que cero
                                               # donde este el color blanco
fm=np.min(x)                                   # Se selecciona el valor minimo del vector en el eje x donde haya blanco
cm=np.min(y)                                   # Se selecciona el valor minimo del vector en el eje y donde haya blanco
FM=np.max(x)                                   # Se selecciona el valor maximo del vector en el eje x donde haya blanco
CM=np.max(y)                                   # Se selecciona el valor maximo del vector en el eje y donde haya blanco
    
carro=imread('carro1.png')                     # Se lee imagen original a color del carro(clase 6)

c_placa=carro[fm:FM,cm:CM,:]                   # Con las coordenadas anteriores se extrae seccion de la imagen donde esta
                                               # la placa
imshow('Placa a color',c_placa)                # Se muestra solo la placa de la imagen original
waitKey(0)                                     # Se espera hasta que se oprima una tecla
destroyAllWindows()                            # Se destruyen todas las ventanas abiertas

