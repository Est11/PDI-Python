
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
###### Resumen: Mapa de bits y areas.          ###
##################################################


# In[2]:


from cv2 import *                                   # Se importan todas las funciones de la libreria de Opencv
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(14,10))                     # Se logra que el plot tenga un tamaño adecuado para su visualizacion

a=imread('figuras2.bmp',0)                          # Se lee imagen utilizando funcion de libreria cv2

imshow('Figuras',a)                                 # Se muestra imagen utilizando funcion de la libreria cv2
waitKey(0)                                          # Se espera hasta que se oprima una tecla
destroyAllWindows()                                 # Se cierran todas las ventanas creadas

ret, labels=connectedComponents(a)                  # Funcion de cv2 utilizada para etiquetar las figuras de la imagen 
                                                    # hace las veces de bwlabel en matlab

plt.imshow(labels,cmap='jet')                       # Se muestra la imagen utilizando las etiquetas anteriores y aplicando
                                                    # colormap a la figura en este caso jet
plt.title('Figuras aplicando colormap',fontsize=24) # Se pone titulo al plot
plt.xticks([0,100,200,300,400])                     # Para escoger los ejes, vacio no aparece ninguna
plt.yticks([])                                      # Para escoger los ejes, vacio no aparece ninguna
plt.show()                                          # Para visualizar el plot en el notebook

print('Numero de objetos es: ',str(ret-1))          # Se imprime el numero de objetos en la imagen se le resta uno porque 
                                                    # al parecer el fondo se esta contando como un objeto


# In[4]:


fig=plt.figure(figsize=(14,10))                     # Se logra que el plot tenga un tamaño adecuado para su visualizacion

for i in range(1,ret-1):                            # Se varia hasta donde va el ciclo para quedarse con una u otra imagen
    c=a*0                                           # Se crean dos matrices nuevas con el tamaño de la imagen original
    d=a*0
    ind=np.where(labels==i)                         # Se reccoren las etiquetas de los objetos 
    c[ind]=255                                      # A los indices de todas las otras figuras se los lleva a blanco
    d[ind]=1                                        # Se llevan estos valores de la figura a 1 para luego sumar Nº de pixeles
    area=sum(d)                                     # El area de la figura esla suma de los indices en 1 anteriores
    
plt.subplot(211)
plt.title('Una sola figura',fontsize=24)            # Se pone un titulo al plot
plt.imshow(c,cmap='winter')                         # Se le aplica a esta imagen otro colormap en este caso winter
plt.xticks([])                                      # Para escoger los ejes, vacio no aparece ninguna
plt.yticks([])                                      # Para escoger los ejes, vacio no aparece ninguna

plt.subplot(212) 
plt.plot(area)                                      # Se grafica el area del objeto deseado
plt.title('Area',fontsize=24)                       # Se pone un titulo para el plot
plt.grid(True)                                      # Se agrega una cuadricula al plot

plt.tight_layout()                                  # Para separar los dos subplots
plt.show()                                          # Se utiliza para mostrar los subplots en el notebook

