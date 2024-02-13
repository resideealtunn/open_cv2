import cv2
resim=cv2.imread("noisy2.png")
cv2.imshow("Orijinal",resim)

#mean filtering
meanFilter1=cv2.blur(resim,(3,3))
meanFilter2=cv2.blur(resim,(5,5))
meanFilter3=cv2.blur(resim,(7,7))
meanFilter4=cv2.blur(resim,(9,9))
cv2.imshow("Mean Filter 1",meanFilter1)
cv2.imshow("Mean Filter 2",meanFilter2)
cv2.imshow("Mean Filter 3",meanFilter3)
cv2.imshow("Mean Filter 4",meanFilter4)

#median filtering
medianFilter1=cv2.medianBlur(resim,3)       #3x3 yerine 3 yazmak yeterlidir
medianFilter2=cv2.medianBlur(resim,5)
medianFilter3=cv2.medianBlur(resim,7)
medianFilter4=cv2.medianBlur(resim,9)
cv2.imshow("Median Filter 3x3", medianFilter1)
cv2.imshow("Median Filter 5x5", medianFilter2)
cv2.imshow("Median Filter 7x7", medianFilter3)
cv2.imshow("Median Filter 9x9", medianFilter4)

#gauss filtering
gaussfilter1=cv2.GaussianBlur(resim,(3,3),0)    #,0 gerekli
gaussfilter2=cv2.GaussianBlur(resim,(5,5),0)
gaussfilter3=cv2.GaussianBlur(resim,(7,7),0)
gaussfilter4=cv2.GaussianBlur(resim,(9,9),0)
cv2.imshow("Gauss Filter 3x3",gaussfilter1)
cv2.imshow("Gauss Filter 5x5",gaussfilter2)
cv2.imshow("Gauss Filter 7x7",gaussfilter3)
cv2.imshow("Gauss Filter 9x9",gaussfilter4)

cv2.waitKey(0)
cv2.destroyAllWindows()