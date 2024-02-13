import cv2
image=cv2.imread("image2.png",0)  #simple'da renkli okey ama adaptive gride çalışıyor
cv2.imshow("Orijinal",image)

#SIMPLE TRESHOLDİNG     threshold:eşik

ret,thresh1=cv2.threshold           (image,                    127,                            255,                         cv2.THRESH_BINARY)      #2 çıktı dondurur
#1.->kullanılan esik 2.->çıktı eşikli görüntü (, bu eşiğin altında kalanlar 0'a yuvarlanır, üstündekiler 255'e yuvarlanır , 
cv2.imshow("Thresh 1",thresh1)
print(ret)
ret,thresh2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh 2",thresh2)
ret,thresh3=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imshow("Thresh 3",thresh3)
ret,thresh4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imshow("Thresh 4",thresh4)
ret,thresh5=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("Thresh 5",thresh5)

#thresh_binary en çok kullanılanıdır
#Simple thresholding'te belirlenen bir eşik degeri tüm resme uygulanır.
#Adaptive thresholding resmin belli bölgesine uygulamak içindir

#ADAPTİVE THRESHOLDİNG                  adaptive:uyarlanabilir
#mean -->ortalamaya gore
a_thresh1=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY ,11,2)   #11,2 ortalama alınacak grup boyutu
cv2.imshow("Mean",a_thresh1)

#guassian -->ağırlıklı ortalamaya göre
a_thresh2=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY ,11,2)
cv2.imshow("Gaussian",a_thresh2)

#OTSU THRESHOLDİNG
ret2,o_tresh1=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#biz araligi veririz, degerlere kendi karar verir
cv2.imshow("Otsu",o_tresh1)



cv2.waitKey(0)
cv2.destroyAllWindows()