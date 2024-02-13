import cv2
import numpy as np

kurtresmi = cv2.imread("kurt.webp")

print(kurtresmi[(230,80)])      #resmin 230. satır 80. sutunundaki pikselin bgr degerini yazdir demek

resim2=cv2.imread("sherlock.jpg")
cv2.imshow("Sherlock",resim2)
resim3=cv2.imread("sherlock.jpg")

resim2[100,70] = [255,255,255]              #piksele renk atama
cv2.imshow("Sherlock Boyanmis",resim2)

for i in range(25,100):                 #çizgi şeklinde sütun boyama
    resim2[25,i]=[255,255,255]
cv2.imshow("sherlock cizgi boyanmis",resim2)

for i in range(500):            #sutun boyama 
    resim2[i,500]=[255,255,255]
cv2.imshow("sutun boyama", resim2)

for i in range(100):          #kare seklinde atama
    for j in range(100):
        resim2[i,j]=[255,255,255]
cv2.imshow("kare boyama",resim2)

for i in range(20,100):
    for j in range(20,100):
        resim3[i,j]=[255,255,255]
cv2.imshow("kare boyama2",resim3)

cv2.waitKey(0)
cv2.destroyAllWindows