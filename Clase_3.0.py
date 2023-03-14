
# coding: utf-8

# In[9]:


##################################################
###### Creado por: Esteban Restrepo Sierra     ###
###### Estudiante                              ###
###### Ingenieria de Telecomunicaciones        ###
##################################################
###### Docente: David Fernandez Mc Cann        ###
###### Procesamiento Digital de Imagenes       ###
######             2018-1                      ###
###### Resumen: Transformaciones con imagenes. ###
##################################################

from skimage import color
import matplotlib.pyplot as plt
import numpy as np
from cv2 import *                      # Se importan todas las funciones de la libreria de Opencv

img = imread('paisaje.jpg')            # Se lee imagen
imshow("imagen",img)                   # Se muestra imagen utilizando funcion de cv2
waitKey(0)                             # Se espera que se oprima una tecla
destroyAllWindows()                    # Se cierran todas las ventanas


# In[3]:


imggray=color.rgb2gray(img)            # Utilizando libreria color se transforma imagen a escala de grises
imshow('grises',imggray)               # Se muestra imagen utilizando funcion de cv2
waitKey(0)                             # Se espera que se oprima una tecla
destroyAllWindows()                    # Se cierran todas las ventanas


# In[7]:


imgneg=255-imggray                     # Se invierten valores de los pixeles de la imagen para obtenerla en negativo
plt.imshow(imgneg, cmap=plt.cm.gray)   # Se muestra la imagen utilizando libreria matplotlib.pyplot
plt.show()                             # Comando que se utiliza para mostrar en notebook


# In[18]:


imgnegt=np.fliplr(imgneg)              # Se rota la imagen en negativo con la funcion fliplr de la libreria numpy
plt.imshow(imgnegt, cmap=plt.cm.gray)  # Se muestra la imagen utilizando libreria matplotlib.pyplot
plt.show()                             # Comando que se utiliza para mostrar en notebook


# In[8]:


imgtcolor=np.fliplr(img)               # Se rota la imagen original con la funcion fliplr de la libreria numpy
imshow('flip_orig',imgtcolor)          # Se muestra imagen utilizando funcion de cv2
waitKey(0)                             # Se espera que se oprima una tecla
destroyAllWindows()                    # Se cierran todas las ventanas

