
# coding: utf-8

# In[3]:


##################################################
###### Creado por: Esteban Restrepo Sierra     ###
###### Estudiante                              ###
###### Ingenieria de Telecomunicaciones        ###
##################################################
###### Docente: David Fernandez Mc Cann        ###
###### Procesamiento Digital de Imagenes       ###
######             2018-1                      ###
###### Resumen: Fundido de imagenes.           ###
##################################################

from cv2 import *                       # Se importan todas las funciones de la libreria de Opencv
import numpy as np

img = imread('paisaje.jpg')             # Se leen imagenes de un carro y un paisaje utilizando funcion de cv2
img1= imread('carro.jpg')

c=resize(img1,(500, 282))               # Se redimensiona el tamaño del carro al del paisaje con funcion de cv2 para poder operar

imgn=normalize(img.astype('float64'), None, 0.0, 1.0,NORM_MINMAX)   #Se normalizan las imagenes utilizando funcion de cv2
cn=normalize(c.astype('float64'), None, 0.0, 1.0, NORM_MINMAX)

suma=cn/2+imgn/2                        # Se realiza fundido de las imagenes 
imshow('Fundido',suma)                  # Se muestra fundido de las imagenes utilizando funcion de cv2
waitKey(0)                              # Se espera que se oprima una tecla
destroyAllWindows()                     # Se cierra todas las ventanas


# In[4]:


for i in range(30):         # Ciclo para que partiendo del fundido anterior una imagen vaya desapareciendo y la otra apareciendo
    f=suma*i+cn*(i-1)       # Funcion donde partiendo del fundido desaparece el paisaje y queda luego el carro              
    f=normalize(f.astype('float64'),None,0.0,1.0,NORM_MINMAX) # Se normaliza la variable que recibe la operacion
    imshow('Fundido',f)     # Se va mostrando el resultado de esta operacion en los pixeles usando funcion de cv2
    waitKey(100)              # Cada que se oprime una tecla se aplica de nuevo la operacion en los pixeles
destroyAllWindows()         # Cuando el ciclo finaliza se destruyen todas las ventanas

