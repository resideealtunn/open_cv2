import cv2
import numpy as np

resim=cv2.imread("23_nisan.jpg")

kesit = resim[550:700,80:200]           #buyuk resimden bir kesit kırptık

cv2.imshow("Buyuk Resim",resim)
cv2.imshow("Kesit",kesit)

resim[0:150 , 0:120] = kesit            #kesilen resmin asıl resim üzerinde yapistirilacagi yeri atadık. kucuk resmin boyutlarına uyumsuz boyut girersen hata
cv2.imshow("Yapistir",resim)

#resmin belli bolgesine efekt uygulamak 
resim[120:200 , 200:300] = (100,200,150)    #(blue , green ,red) ile direkt atama yaptık 
cv2.imshow("belli bolge boya" , resim)
cv2.waitKey(0)
cv2.destroyAllWindows()