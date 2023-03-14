
# coding: utf-8

# In[7]:


##################################################
###### Creado por: Esteban Restrepo Sierra     ###
###### Estudiante                              ###
###### Ingenieria de Telecomunicaciones        ###
##################################################
###### Docente: David Fernandez Mc Cann        ###
###### Procesamiento Digital de Imagenes       ###
######             2018-1                      ###
###### Resumen: Lectura y manejo de imagenes.  ###
##################################################

from skimage.viewer import ImageViewer as IV    # Se importa libreria que sirve para ver informacion de los pixeles en una imagen
import matplotlib.pyplot as plt
from cv2 import *                               # Se importan todas las funciones de la libreria de Opencv

img = imread('img.png')                         # Se lee imagen 
ventana=IV(img)                                 # Se crea una variable donde se almacenara el contenido de la imagen 
ventana.show()                                  # Se muestra ventana con la imagen e informacion sobre los pixeles


# In[15]:


r=imread('img.png')
r[:,:,1] = 0                                    # Eliminamos el color verde de la imagen
r[:,:,2] = 0                                    # Eliminamos el color azul de la imagen
rojo=IV(r)                                      # Se crea una variable donde se almacenara la componente roja de la imagen
rojo.show()                                     # Se muestra imagen en su componente roja e informacion sobre los pixeles


# In[9]:


g=imread('img.png')
g[:,:,0] = 0                                    # Eliminamos el color rojo de la imagen
g[:,:,2] = 0                                    # Eliminamos el color azul de la imagen
verde=IV(g)                                     # Se crea una variable donde se almacenara la componente verde de la imagen
verde.show()                                    # Se muestra imagen en su componente verde e informacion sobre los pixeles


# In[10]:


b=imread('img.png')
b[:,:,0] = 0                                    # Eliminamos el color rojo de la imagen
b[:,:,1] = 0                                    # Eliminamos el color verde de la imagen
azul=IV(b)                                      # Se crea una variable donde se almacenara la componente azul de la imagen
azul.show()                                     # Se muestra imagen en su componente azul e informacion sobre los pixeles


# In[14]:


fig=plt.figure(figsize=(10,12))                 # Se define un buen tamaño para la imagen para poder observarla bien
plt.subplot(221)                                # Se crean subplots de las imagenes creadas anteriormente
plt.imshow(r)                                   # Se muestra la imagen utilizando libreria matplotlib.pyplot 

plt.subplot(222)
plt.imshow(g)

plt.subplot(223)
plt.imshow(b)

plt.subplot(224)
plt.imshow(img)

plt.tight_layout()
plt.show()                                      # Comando que sirve para mostrar en notebook


