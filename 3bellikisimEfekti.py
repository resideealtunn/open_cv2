import cv2
import numpy as np

resim=cv2.imread("kemal_sunal.webp")
cv2.imshow("Kemal Sunal",resim)
resim2=cv2.imread("kemal_sunal.webp")
resim3=cv2.imread("kemal_sunal.webp")
#resmin tekli renk efektini degistirme 
resim[:,:,0]=255        #0:blue , 1:green , 2:red degeridir
cv2.imshow("Tekli degistirme blue", resim)
# resim[:,:,1]=255        #0:blue , 1:green , 2:red degeridir
# cv2.imshow("Tekli degistirme green", resim)
# resim[:,:,2]=255        #0:blue , 1:green , 2:red degeridir
# cv2.imshow("Tekli degistirme red", resim)

#birden fazla ayar icin komutlar alt alta yazılır
resim2[:,:,0]=50
resim2[:,:,1]=100
cv2.imshow("Coklu efekt",resim2)

#belli kısmına efekt ekleme
resim3[160:220, 400:590 , 0]=255        # ilk parametre y eksenidir , 2. parametre x eksenidir , 3. parametre bgrdir , atama bgr degerine yapılır
resim3[160:220, 400:590 , 1]=150
cv2.imshow("Belli bolge",resim3)

cv2.waitKey(0)
cv2.destroyAllWindows()