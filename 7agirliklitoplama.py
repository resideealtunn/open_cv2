import cv2
import numpy as np

resim1=cv2.imread("mujdear.png")
resim2= cv2.imread("tarikakan.png")

cv2.imshow("Mujde Ar", resim1)
cv2.imshow("Tarik Akan",resim2)

#agırlıklı piksel toplama
print(resim1[200,300])
print(resim2[300,400])
print("+______________")
print(resim1[200,300] + resim2[300,400])


#agırlıklı toplama resimleri ust uste ekleme
boyutlu1 = cv2.imread("boyutlanmis1.webp")
boyutlu2= cv2.imread("byt2.jpg")
toplam=cv2.add(boyutlu1,boyutlu2)
cv2.imshow("Ust Uste Eklenmis Resim",toplam)

#agırlıklı toplama resimleri belirginlik oranlarıyla ust uste ekleme
agirliklitoplam = cv2.addWeighted (boyutlu1,       0.7             , boyutlu2,       0.3             ,    0          )
#                                 (1. resim, 1.nin baskınlık oranı , 2.resim , 2.nin baskınlık oranı , sıfır verilir )    
#1. ve 2. resmin baskınlık oranları toplamı 1 olmalıdır. 5 parametre alır                                     
cv2.imshow("Agirlikli Toplama İle" , agirliklitoplam)
cv2.waitKey(0)
cv2.destroyAllWindows()