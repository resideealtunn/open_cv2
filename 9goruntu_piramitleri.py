import cv2
import numpy as np

resim=cv2.imread("theo_james.png")
cv2.imshow("Orijinal" ,resim)
#resmin hem yuksekligini hem genisligini 2 katına cikarma
ikiKat=cv2.pyrUp(resim)
cv2.imshow("Iki Kat Buyuk" , ikiKat)

#resmin hem yuksekligini hem genisligini yariya indirme
yariya = cv2.pyrDown(resim)
cv2.imshow("Iki Kat Kucuk" ,yariya)

print("Orijinal Boyutlar           :" , resim.shape)
print("Iki Kat Buyutulmus Boyutlar :" ,ikiKat.shape)
print("Iki Kat Kucultulmus Boyutlar:", yariya.shape)

#resim olusturma
goruntu= np.zeros((300,300,3),dtype="uint8")   #zeros matrisin tum elemanlarını sıfır yapar. olusturulacak resmin shape ve data tipini pm alır 
print(goruntu)                                  #zeros fonksiyonu arkaplanda liste olusturur ekrana matris basar

cv2.waitKey(0)
cv2.destroyAllWindows()