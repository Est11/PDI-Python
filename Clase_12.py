
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
import funciones1 as fun1
import funciones2 as fun2
import scipy.misc as sc
import numpy as np
from skimage import color
from skimage.viewer import ImageViewer as IV
from skimage import morphology



a=imread('058.jpg')
a=sc.imresize(a,0.3)

a_fil=fun2.filtro_clave(a)

# imwrite('nombre.extension') comando de opencv para guardar imagenes


c=imread('058_fil.jpg')
c=sc.imresize(c,0.3)

s,y,b,h=fun1.componentes(c)

tot=np.vstack((s,y,b,h))

imshow('Componentes en diferentes espacios',tot)
waitKey()
destroyAllWindows()



d=imread('st.jpg',0)

e=imread('yt.jpg',0)

f=imread('bt.jpg')

g=imread('ht.jpg')

ret,thresh1=threshold(d,151,255,THRESH_BINARY)
ret,thresh2=threshold(e,80,255,THRESH_BINARY)
ret,thresh3=threshold(f,199,255,THRESH_BINARY)
ret,thresh4=threshold(g,224,255,THRESH_BINARY)

total=np.hstack((thresh1,thresh2))
total1=np.hstack((thresh3,thresh4))


total1[:,:,0]=0
total1[:,:,1]=0

total1_gray=color.rgb2gray(total1)

                                                                               
umbr1 = np.where(total1_gray <= 0)                
                                             
umbr2 = np.where(total1_gray > 0)            

total1_gray[umbr1] = 0                            
total1_gray[umbr2] = 255   


final=np.vstack((total,total1_gray))

final=sc.imresize(final,0.8)

imshow('Imagenes binarizadas',final)
waitKey()
destroyAllWindows()


kernel = np.ones((12,15),np.uint8)               

im_clear=morphologyEx(final,MORPH_OPEN,kernel)    

imshow('Imagenes limpias',im_clear)
waitKey()
destroyAllWindows()

