import cv2
import numpy as np

image=cv2.imread("reshide.png")
cv2.imshow("Orijinal",image)
image2=cv2.imread("reshide2.png")
cv2.imshow("reshide 2",image2)

kernel=np.ones((5,5),np.uint8)      #matris dondurur
#Yapılandırma Elemanı olusturduk. oncekilerde kullandıgımız zeros fonksiyonu da bir yapılandırma elemanıydı(kerneldı)

genisleyen=cv2.dilate(image,kernel,iterations=1)        #beyaz yerleri genişletir. genişleyen:dilation
cv2.imshow("Genisleyen",genisleyen)

daralan=cv2.erode(image,kernel,iterations=1)            #beyaz yerleri daraltır. daralan:erosion
cv2.imshow("Daralan",daralan)

#iterations degeri artırılırsa yapılan işlem daha güçlü sonuçlar oluşturur
#işlemin anlamlı olması için önce beyaz yerlerin daraltılıp -pürüzlerin giderilip- sonra pürüzsüz resmin genişletilmesi gerekir;

daralan2=cv2.erode(image,kernel,iterations=1)
genisleyen2=cv2.dilate(daralan2,kernel,iterations=1)
cv2.imshow("Sahane",genisleyen2) 

#erosion + dilation yapan komut-> opening; (GÜRÜLTÜLÜ RESİMLERDE)
opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)       #erosion ve dilation operatorleri disindakiler morphologyEx fonksiyonu ile çağırılır
cv2.imshow("Opening",opening)

#dilation + erosion yapan komut -> closing; (birleştirmeli kopuk kesikli görsellerde tamamlamak istiyorsak)
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow("closing",closing)

#dilation - erosion yapan -> gradian;
gradian=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("Gradian",gradian)

#orijinal-opening yapan -> tophat;
tophat=cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)
cv2.imshow("Tophat",tophat)

#orijinal - closing yapan ->blackhat;
blackhat=cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)
cv2.imshow("Blackhat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()