import cv2
camera=cv2.VideoCapture(0)

width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))        #video encoder/decoder edilirken boyut bilgileri gereklidir
height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

#standart ve tanımlılık formatını oluşturmak için ve ses/görüntü vb. dosyaları aktarırken ve alırken encoder ve decoder işlemleri için fourcc kullanılır
fourcc =  cv2.VideoWriter_fourcc(*'MP4V')          #fourcc:four character code
#bir kayıt yapılacak ve fourcc değişkenine atılacak, kayıt formatı mp4 olacak dedik.
writer=cv2.VideoWriter("kayit.mp4" , fourcc         , 20            ,width      ,height) 
#                      video adi   ,encoder formati , kayıt hızı ,genislik   ,yukseklik)



#donguye alırsan video elde edersin
while True:
    ret,frame = camera.read()    #frame görüntü tutar. ret boolean'dir. framede görüntü varsa 1 yoksa 0 doner
    writer.write(frame)          #frameden alınan goruntuler writer içine yazılır
    cv2.imshow("Kamera", frame)
    if cv2.waitKey(25) & 0xFF== ord('q') :     #waitkey pmsi milisaniyedir
        break
#imhow hızıyla kayıt hızı(writer) aynı olmak zorunda değil, bağımsız
camera.release()    #serbest bıraktık
writer.release()    #yazıcıyı da serbest bırakmak gerekir
cv2.destroyAllWindows()



