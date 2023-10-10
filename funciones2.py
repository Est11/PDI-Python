# coding: utf-8

import funciones1 as fun1
import numpy as np
import scipy.signal as sc
from cv2 import *

def filtro_clave(a):
    aa,aa_b,aa_g,aa_r=fun1.chori(a)
    a1_fil=sc.medfilt2d(aa_b,21)
    a2_fil=sc.medfilt2d(aa_g,21)
    a3_fil=sc.medfilt2d(aa_r,21)
    acolor_fil=waffer(a1_fil,a2_fil,a3_fil)
    return acolor_fil


def waffer(x,y,z):
    at=np.dstack([x,y,z])                        
    return at


def filtros(a):
    a1=filtro_clave(a)
    aa2,aa_b2,aa_g2,aa_r2=fun1.chori(a)
    a2_fil_b=GaussianBlur(aa_b2,(21,21),0)
    a2_fil_g=GaussianBlur(aa_g2,(21,21),0)
    a2_fil_r=GaussianBlur(aa_r2,(21,21),0)
    a2=waffer(a2_fil_b,a2_fil_g,a2_fil_r)
    aa3,aa_b3,aa_g3,aa_r3=fun1.chori(a)
    a3_fil_b=blur(aa_b3,(21,21))
    a3_fil_g=blur(aa_g3,(21,21))
    a3_fil_r=blur(aa_r3,(21,21))
    a3=waffer(a3_fil_b,a3_fil_g,a3_fil_r)
    return a1,a2,a3
    
    

