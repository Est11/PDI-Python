
# coding: utf-8

# In[12]:


from cv2 import *     
import numpy as np

a=imread('1_filtro_suavizador.bmp',0)

mascara=np.array([[1,2,1],[2,4,2],[1,2,1]])/16

x,y=a.shape

b=np.zeros((x,y))

c=a

z=[]

for i in range(20):
 
    for col in range(2,y-1):
       
        for fil in range(2,x-1):
            
            z=a[range(fil-2,fil+1),range(col-2,col+1)]
            
            R=np.float64(z)*mascara          
            R=np.sum(R)
        
            b[fil][col]=R
            
            

a=np.uint8(b)

imshow('Imagen original',c)
waitKey()

imshow('Imagen suavizada',np.uint8(b))
waitKey()


destroyAllWindows()


            
        



