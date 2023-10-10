
# coding: utf-8



##################################################
###### Creado por: Esteban Restrepo Sierra     ###
###### Estudiante                              ###
###### Ingenieria de Telecomunicaciones        ###
##################################################
###### Docente: David Fernandez Mc Cann        ###
###### Procesamiento Digital de Imagenes       ###
######             2018-1                      ###
###### Resumen: Filtros en la imagen.          ###
##################################################



from cv2 import *     
import funciones2 as fun2
import numpy as np
from skimage.viewer import ImageViewer as IV
import scipy.misc as sc


a=imread('001.jpg')
a=sc.imresize(a,0.5)
imshow('Imagen original',a)
waitKey()
destroyAllWindows()



a1,a2,a3=fun2.filtros(a)

at=np.hstack((a1,a2,a3))

imshow('Diferentes filtros',at)
waitKey()
destroyAllWindows()

