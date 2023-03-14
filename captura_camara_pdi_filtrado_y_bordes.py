
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
###### Resumen: Captura de imagen por medio    ###
###### de la camara del pc o camara usb se     ###
###### aplica filtro gaussiano y filtro cany   ###
###### para ver bordes en la imagen.           ###
##################################################

from cv2 import *                       # Se importan todas las funciones de la libreria de Opencv

namedWindow("webcam")                   # Se crea una nueva ventana donde se mostrara el contenido de la imagen
vc = VideoCapture(0)                    # Se guarda en una variable lo que se capture por la camara 0 (la del pc) si es una
                                        # camara usb seria la 1 y asi sucesivamente.         
    
while True:
    next, frame = vc.read()             # Constantemente se lee el estado de la variable y actualiza
    gray = cvtColor(frame, COLOR_BGR2GRAY)  #Se convierte la imagen capturada a escala de grises
    gauss = GaussianBlur(gray, (7,7), 1.5, 1.5)  # Se aplica filtro gaussiano
    can = Canny(gauss, 0, 30, 3)   #Se aplica filtro canny que permite ver bordes de la imagen
    imshow("webcam", can)          # Se muestra la imagen capturada por la camara luego de aplicado el proceso anterior
    if waitKey(10)==27:            # Se espera que se oprima una tecla 10ms y si se compara si esta coincide con la tecla ESC
        break                      # Se rompe el ciclo infinito
destroyAllWindows()                # Se destruyen todas las ventanas creadas

