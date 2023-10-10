
# coding: utf-8

# In[ ]:


##################################################
###### Creado por: Esteban Restrepo Sierra     ###
###### Estudiante                              ###
###### Ingenieria de Telecomunicaciones        ###
##################################################
###### Docente: David Fernandez Mc Cann        ###
###### Procesamiento Digital de Imagenes       ###
######             2018-1                      ###
###### Resumen: Erosion y dilatacion.          ###
##################################################


# In[37]:


from cv2 import *                              # Se importan todas las funciones de la libreria de Opencv

a=imread('figuras3.bmp',0)                     # Se lee placa directamente en escala de grises usando funcion de cv2 
a1=a

ee=getStructuringElement(MORPH_RECT,(5,5))     # Se crea elemento estructurante rectangular de 5x5

for i in range(1,10):                          
    a=erode(a,ee)                              # Se aplica erosion a la imagen original con el elemento estructurante creado
    imshow('Erosion',a)                        # Se muestra la imagen aplicando proceso de erosion
    waitKey(700)                               # Se esperan 700 ms entre los cambios en la imagen erosionada
destroyAllWindows()                            # Se destruyen todas las ventanas abiertas

for i in range(1,10):
    a1=dilate(a1,ee)                           # Se aplica dilatacion a la imagen original con el elemento estructurante creado
    imshow('Dilatacion',a1)                    # Se muestra la imagen aplicando proceso de dilatacion
    waitKey(700)                               # Se esperan 700 ms entre los cambios en la imagen dilatada
destroyAllWindows()                            # Se destruyen todas las ventanas abiertas

