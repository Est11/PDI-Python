
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
###### Resumen: Transformacion de color.       ###
##################################################


# In[4]:


from cv2 import *                          # Se importan todas las funciones de la libreria de Opencv
import numpy as np
import scipy.misc as sc
import funciones as fun

a=imread('carro1.png')                     # Se lee la imagen utilizando funcion de libreria cv2

c=sc.imresize(a,0.3)                       # Se redimensiona la imagen al 30% de su tamaño original usando libreria scipy.misc

imshow('carro',a)                          # Se muestra imagen utilizando funcion de libreria cv2
waitKey(0)                                 # Se espera que se oprima una tecla
destroyAllWindows()                        # Se cierran todas las ventanas


# In[5]:


a_rgb,a_hsv,a_cmyk,a_lab,a_lch,k=fun.componentes(c) # Se aplica la funcion componentes que devuelve las componentes de los 
                                                    # espacios de color hsv,cmyk,lab,lch.

imshow('Componentes RGB, HSV , CMYK , LAB y LCH',np.vstack((a_rgb,a_hsv,a_cmyk,a_lab,a_lch))) # Se muestra salida de funcion anterior
waitKey(0)                                          # Se espera a que se oprima una tecla
destroyAllWindows()                                 # Se cierran todas las ventanas abiertas

imshow('Imagen elegida',k)                          # Se muestra imagen seleccionada para realizar el tratamiento ala placa
waitKey(0)                                          # Se espera que se oprima una tecla
destroyAllWindows()                                 # Se cierran todas las ventanas

#kmod=k[75:90,60:95]                                 #PARA RECORTAR SOLO EN LA PLACA DE LA IMAGEN ELEGIDA
#kmod=sc.imresize(kmod,3)
#imshow('Ultima imagen de LAB',kmod)
#waitKey(0)
#destroyAllWindows()

#a_cmyk=sc.imread('carro1.png',mode='CMYK')          #PARA LEER DIRECTAMENTE LA IMAGEN EN EL ESPACIO CMYK
#imshow('iMAGEN CMYK',a_cmyk)
#waitKey(0)
#destroyAllWindows()



# In[6]:


umbr = 167                                  # Se define un umbral                 

umbr1 = np.where(k>umbr)                    # Se usa funcion Where de libreria numpy para discriminar los pixeles con intensidad
                                            # mayor que la del umbral
umbr2 = np.where(k <= umbr)                 # Se usa funcion Where de libreria numpy para discriminar los pixeles con intensidad
                                            # menor o igual que la del umbral
k[umbr1] = 255                              # Los pixeles que cumplan la primera condicion se llevan a negro
k[umbr2] = 0         

imshow('Placa binarizada',k)                # Se muestra placa binarizada utilizando funcion de libreria cv2
waitKey(0)                                  # Se espera que se oprima una tecla
destroyAllWindows()                         # Se cierran todas las ventanas

