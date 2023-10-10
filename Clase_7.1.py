
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
###### Resumen: Area de placa binarizada.      ###
##################################################


# In[4]:


from cv2 import *                               # Se importan todas las funciones de la libreria de Opencv
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(14,10))                 # Se utiliza para poner de un tamaño apreciable el plot

a=imread('placa_bin.bmp',0)                     # Se lee la placa con funcion de libreria cv2 binarizada(clase 6)

imshow('Placa binarizada',a)                    # Se muestra placa binarizada usando funcion de libreria cv2
waitKey(0)                                      # Se espera hasta que se oprima una tecla
destroyAllWindows()                             # Se cierran todas las ventanas creadas

ret, labels=connectedComponents(a)              # Funcion de cv2 utilizada para etiquetar las figuras de la imagen
                                                # hace las veces de bwlabel en matlab
for i in range(1,ret):                          # Ciclo para recorrer la imagen 
    c=a*0                                       # Se crea una matriz en cero con las dimensiones de la imagen original
    ind=np.where(labels==i)                     # Se recorren las etiquetas de los objetos en la imagen
    c[ind]=1                                    # A cada pixel se les lleva el valor de 1
    suma=sum(c)                                 # Se suman los pixeles de todas las figuras 
    total=sum(suma)                             # Se suman esos valores de los pixeles para hallar areas de objetos
    imshow('Buscando placa',c*255)              # Se muestra como el cilo recorre la imagen buscando la placa
    waitKey(100)                                # Se esperan 100ms y es como si se oprimiera la tecla automaticamente
    if total > 2500:                            # Aproximar area de la placa en pixeles usando libreria IV usada en clase 1
        suma1=suma                              # Se lleva el lugar y el area de la placa a dos vbles nuevas
        area=total
destroyAllWindows()                             # Se destruyen las ventanas abiertas

plt.plot(suma1)                                 # Se grafica el lugar donde se encuentra la placa
plt.title('Luegar donde se encuentra la placa',fontsize=24) # Se le da un nombre al plot 
plt.grid(True)                                  # Se agrega una cuadricula a la grafica anterior
plt.show()                                      # Permite mostrar grafica en el notebook

print('El area de la placa es: ',area,'pixeles') # Se imprime el area correspondiente a la placa en pixeles

