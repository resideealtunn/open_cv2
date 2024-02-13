import cv2
import numpy as np

resim=cv2.imread("nataliePortman.png")
cv2.imshow("Orijinal Resim" , resim)

griResim=cv2.cvtColor(resim , cv2.COLOR_BGR2GRAY)       #cvt=convert:donusturmek
cv2.imshow("Gri Resim", griResim)

yukseklik,genislik,kanalsayisi = resim.shape                #shape : form
yukseklik, genislik=griResim.shape

print(yukseklik,genislik,kanalsayisi)
print(yukseklik,genislik)                                   #grilesen resimde kanal sayısı alabilecegi minimum deger olan 1'i alır ve yazılmaz.

#2. yol -- eger direkt gri resim üzerinden islem yapılacaksa 
# resim= cv2.imread("nataliePortman.png" ,0) diye 2. parametre olarak 0 eklenirse de resim gri olur



cv2.waitKey(0)
cv2.destroyAllWindows()