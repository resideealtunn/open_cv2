import cv2
import numpy as np

image1=cv2.imread("image1.png")
image2=cv2.imread("image2.png")
image3=cv2.imread("reshide.jpg",0)
cv2.imshow("Image 1",image1)
cv2.imshow("Image 2",image2)

#bitwise AND        ancak beyaz beyaz ust uste gelirse beyaz olur
b_and= cv2.bitwise_and(image1,image2)
cv2.imshow("Bitwise And",b_and)
#bitwise OR         ancak siyah siyah ust uste gelirse siyah olur
b_or= cv2.bitwise_or(image1,image2)
cv2.imshow("Bitwise Or",b_or)
#bitwise XOR        siyah beyaz ust uste gelirse beyaz olur degilse siyah
b_xor=cv2.bitwise_xor(image1,image2)
cv2.imshow("Bitwise Xor",b_xor)
#bitwise not        siyah yeri beyaz beyaz yeri siyah yapar
b_not=cv2.bitwise_not(image1)       #tek parametre alır!
cv2.imshow("Bitwise Not" ,b_not)

cv2.waitKey(0)
cv2.destroyAllWindows()