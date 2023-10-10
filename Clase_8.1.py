
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
###### Resumen: Obtener placa con erosion      ###
###### y dilatacion.                           ###
##################################################


# In[11]:


from cv2 import *                              # Se importan todas las funciones de la libreria de Opencv
import numpy as np
from skimage import morphology
from skimage.segmentation import clear_border

a=imread('placa_bin.bmp')                      # Se leen placa binarizada e imagen original con funcion de cv2
b=imread('carro1.bmp')

fil,col,cap= b.shape                           # Se sacan dimensiones de la imagen original
c=np.reshape(a,(fil,col,cap))                  # Se crea nuevo arreglo con dimensiones de las imagenes

b1=b
a1=a

b1[c==0]=0                                     # Se lleva a blanco en el auxiliar de la imagen original todo lo que sea blanco
                                               # en la binarizada
imshow('Carro solo con area de interes',b1)    # se muestra imagen original con mascara de imagen binarizada
waitKey()                                      # Se espera hasta que se oprima una tecla
destroyAllWindows()                            # Se destruyen todas las ventanas abiertas

ee=getStructuringElement(MORPH_RECT,(5,7))     # Se crea elemento estructurante rectangular de 5x7

kernel = np.ones((5,7),np.uint8)               # Parametro de morphologyEx para eliminar ruido exterior a la placa

im_clear=morphologyEx(a1,MORPH_OPEN,kernel)    # Funcion que elimina ruido exterior de la placa de libreria skimage

imshow('Imagen limpia',im_clear)               # Se muestra con menos ruido en el fondo
waitKey()                                      # Se espera hasta que se oprima una tecla
destroyAllWindows()                            # Se destruyen todas las ventanas abiertas

for i in range(1,6):
    im_clear=dilate(im_clear,ee)               # Se aplica dilatacion a la imagen limpia con el elemento estructurante creado
    imshow('Dilatacion',im_clear)              # Se muestra la imagen aplicando proceso de dilatacion
    waitKey(700)                               # Se esperan 700 ms entre los cambios en la imagen dilatada
destroyAllWindows()                            # Se destruyen todas las ventanas abiertas

for i in range(1,8):                          
    im_clear=erode(im_clear,ee)                # Se aplica erosion a la imagen limpia con el elemento estructurante creado
    imshow('Erosion',im_clear)                 # Se muestra la imagen aplicando proceso de erosion
    waitKey(700)                               # Se esperan 700 ms entre los cambios en la imagen erosionada
destroyAllWindows()                            # Se destruyen todas las ventanas abiertas

c1=np.reshape(im_clear,(fil,col,cap))          # Se crea matriz auxiliar con dimensiones de imagen luego de procesado anterior

b2=b
b2[c1==0]=0                                    # Se utiliza matriz auxiliar para llevar a cero todos los valores correspondientes
                                               # de la imagen original
    
imshow('Placa extraida',b2)                    # Se muestra placa luego de aplicar el proceso, aun tiene un poco de basura exterior
waitKey()                                      # Se espera hasta que se oprima una tecla
destroyAllWindows()                            # Se destruyen todas las ventanas abiertas

