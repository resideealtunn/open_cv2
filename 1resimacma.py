
#ders 1 -- opencv resim acma ve yazdirma
import cv2
import numpy as np      #python'da daha az bellek kaplayan liste yapısı kütüphanesi

resim = cv2.imread("logo.png")      #resmi okuduk  ' ,0  'eklersek resmi RGB'den siyah beyaza cevirir
cv2.imshow("Twitter Logo" , resim)      #resmi gosterdik
cv2.imwrite("yenigriresim.png",resim)   #griye cevirdigimiz resmin bu halini de dosyaya kaydederiz. yeni resim olusturduk

resim2= cv2.imread("kus.webp")
cv2.imshow("kus resmi", resim2)

resim3= cv2.imread("logo.png",0)
cv2.imshow("gri",resim3)

print(resim2)                   #resimler piksellerden olusur, piksellerin rgb degerlerinin matrise yerlesmis halini bastırır
                                #resimlerin matris karsiligini gormus oluruz

print(resim.size)           #resim boyutunu gormek icin
print(resim2.size)          
print(resim3.size)

print(resim.dtype)          #resmin data type'ini gormek icin
print(resim2.dtype)
print(resim3.dtype)

print(resim.shape)          #resmin (genislik, yukseklik, kanal sayisi) degerlerini yazar. bu 3 degerin carpimi size degerini verir
print(resim2.shape)
print(resim3.shape)

cv2.waitKey(0)              #pencere acıldıgında kapanması için bir tuşa basılmasını bekler
cv2.destroyAllWindows()     #çarpıya basıldıgında opencvye bağlı tüm pencereleri kapatır