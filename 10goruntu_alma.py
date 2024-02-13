import cv2
import numpy as np

kamera=cv2.VideoCapture(0)        #capture:almak
#                                videocapture(0) fonksiyonunun pmsi->  0:bilgisayarın kamerası
#                                                                     1:usb kamerası
#                                                                     2:adresi verilen yada aynı dosyada bulunan bir videodan goruntu alır
while True:
    ret,goruntu = kamera.read() #ret:kameranın dogru calisip calismadiginı kontrol eder
    cv2.imshow("reshide",goruntu)
    if cv2.waitKey(30) & 0xFF==ord('q'): #30 milisaniyede bir tekrar goruntu al ve q'ya basılmadıgı surece don. ms degeri kuculurse akıcılık artar
        break
kamera.release()        #release:serbest bırak , read tutuyordu release serbest bırakır
cv2.destroyAllWindows()


#videodan goruntu alma
"""
video_path = 'tom_and_jerry.mp4'
cap=cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Video bulunamadi..")
    exit()

#donguye alırsan video elde edersin
while True:
    ret,frame = cap.read()    #frame görüntü tutar. ret boolean'dir. framede görüntü varsa 1 yoksa 0 doner
    cv2.imshow("Kamera", frame)
    if cv2.waitKey(10) & 0xFF== ord('q') :     #waitkey pmsi milisaniyedir
        break
camera.release()    #serbest bıraktık
cv2.destroyAllWindows()
"""