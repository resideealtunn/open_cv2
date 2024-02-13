import cv2
import numpy as np

image=cv2.imread("dobby.png")
blur=cv2.GaussianBlur(image,(5,5),0)

canny=cv2.Canny(blur,50,120)    #2. ve 3. parametreler 0'a yaklatıkca kenar algılama hassasiyeti artar
cv2.imshow("canny",canny)

#otomatik sekilde kenar algılamasi icin
def autoCanny(blur , sigma=0.33 ):
    median=np.median(blur)  #piksel yogunluklarının medyanının hesaplanması
    lower=int(max(0,(1.0-sigma)*median))   #alabilecegi minimum degerin aralıgı. (0 ile 1-sigma arası)
    upper=int(min(255,(1.0+sigma)*median))  #alabilecegi maksimum degerin aralıgı
    canny2=cv2.Canny(blur,lower,upper)
    return canny
wide=cv2.Canny(image,10,220)        #wide:genis , aralık genis
tight=cv2.Canny(image,220,240)          #tight:dar , aralık dar
auto=autoCanny(blur)

cv2.imshow("all pictures",np.hstack([ wide ,tight ,auto]))
#np.hstack([]) metoduyla imshow birden çok resmi ayni sekmeye açar

cv2.waitKey(0)
cv2.destroyAllWindows()