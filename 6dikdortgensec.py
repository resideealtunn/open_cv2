import cv2
import numpy as np

resim= cv2.imread("hababam.png")

cv2.rectangle(resim      ,    (280,250)         ,     (370,130)   , [255,0,0]         , 7)
#           kaynak resim , sol alt koordinatlar ,  sag ust koord. , cerceve rengi     , cerceve kalınlık
#                                 (x,y)         ,        (x.y)     ,[blue,green,red]  , 1-10 arası degerler                   
cv2.imshow("Hababam" ,resim)

cv2.waitKey(0)
cv2.destroyAllWindows()