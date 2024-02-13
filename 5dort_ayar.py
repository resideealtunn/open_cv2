import cv2
import numpy as np

resim=cv2.imread("adileNasit.png")
cv2.imshow("Adile Nasit", resim)

#AYNALAMA 
aynalananresim = cv2.copyMakeBorder(resim ,75 ,75, 125 ,125 , cv2.BORDER_REFLECT) #reflect:yansıtmak , border:sınır #(resim , alt,ürt ,sağ,sol ,islem)
cv2.imshow("Aynalanan Resim" , aynalananresim)

#UZATMA
uzatilanresim= cv2.copyMakeBorder(resim , 120,120,120,120, cv2.BORDER_REPLICATE)  #replicate:tekrarlamak
cv2.imshow("Uzatilan Resim", uzatilanresim)

#TEKRARLAMA
tekrarlananresim = cv2.copyMakeBorder(resim , 300,300,300,300,cv2.BORDER_WRAP)  #wrap:paketlemek
cv2.imshow("Tekrarlanan Resim" , tekrarlananresim)

#ÇERÇEVE EKLEME
cercevelenenresim = cv2.copyMakeBorder(resim,25,25,25,25, cv2.BORDER_CONSTANT , value=(75,150,255)) #valur vermezsek default siyah gelir
cv2.imshow("Cercevelenen Resim", cercevelenenresim)

cv2.waitKey(0)
cv2.destroyAllWindows()
                 