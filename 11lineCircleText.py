import cv2
import numpy as np

resim1=np.zeros((300,300,3),dtype="uint8")
kamera=cv2.VideoCapture(0)
ret,resim2=kamera.read()
cv2.imshow("Resim 1" ,resim1)
cv2.imshow("Resim 2",resim2)

#CİZGİ OLUSTURMA 
cv2.line(resim1,(150,150),(250,250),(60,90,120),3)
#        kaynak,baslangic,  bitis  ,  b  g  r  ,kalınlık
cv2.line(resim2,(400,250),(200,400),(56,65,45),7)
cv2.imshow("Cizgili Resim 1" ,resim1)
cv2.imshow("Cizgili Resim 2",resim2)

#CEMBER OLUSTURMA
cv2.circle(resim2,  (75,75)  ,  50,(150,200,250),4)
#          kaynak, merkez krd,  r,  b    g  r  ,kalınlık
cv2.imshow("Daireli Resim 2",resim2)

#TEXT OLUSTURMA(metin kutusu)
cv2.putText(resim2,"Reshide" ,(100,350),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,       1        ,(255,150,30),    2)
#           kaynak,  metin  ,baslangic , yazi tipi(cv2.FONT_ kullanilir),yazi buyuklugu , yazi rengi ,harf kalinligi                    
cv2.imshow("Yazili Resim 2",resim2)

#DİKDORTGEN OLUSTURMA --rectangle
cv2.rectangle(resim2 , (400,200),(500,100),(150,80,70),3)
cv2.imshow("Dikdortgenli Resim 2",resim2)

#while dongusu icinde yazarak videoya eklems oluruz
cv2.waitKey(0)
cv2.destroyAllWindows()