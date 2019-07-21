import numpy as np
import cv2
import pyautogui
import mss






with mss.mss() as sct:
    monitor = {"top": 40, "left": 0, "width": 800, "height": 640}


trexKoordinat=()  #Trexin koordinatlarını tutmak için bir tuple
Trex=cv2.imread("Trex.png",0)# Trexi tanımak için Trexin fotoğrafını okuyorum(gri ton halde okuma işlemi)
wTrex,hTrex=Trex.shape  # Okuduğum fotoğrafın boyutları

kernel=np.ones((30,30),np.float)*(-1) # filtrelme yapmak için oluşturulan bir değer

while True:
    Ekran=np.array(sct.grab(monitor)) #ekranı okuyoruz
    Ekran_gri=cv2.cvtColor(Ekran,cv2.COLOR_BGR2GRAY)#okuduğumuz ekran görüntüsünü gri tona çeviriyoruz
    resTrex=cv2.matchTemplate(Ekran_gri,Trex,cv2.TM_CCOEFF_NORMED)#gri tona çevirdiğimiz ekranda Trexi arıyoruz

    loc = np.where(resTrex>0.7)#bulduğumuz değerleri karşılaştırıyoruz tutarlılık oranı 0.7 den büyük olan kısımları ayırıyoruz

    for i in zip (*loc[::-1]):#

        trexKoordinat=(i[0],i[1])# bu döngüde ise ayırdığımız kısımları bir tuple ye atıyoruz bu 2 değer bizim x ve y eksenlerindeki koordinatlarımız oluyor

    if len(trexKoordinat)>0:# eğer tupe boş değilse yani trex tanıma işlemi yapılmışsa

        print("Trex Koordinatları alındı {}".format(trexKoordinat))# trexin koordinatlarını ekrana yazdır
        break# ve trex tanıma işlemini bitirmek için döngüyü kır

pt1=trexKoordinat[1]# ağaçların çıktığı bölgeyi ayırmak için bazı koordinatları alıyoruz
pt2=trexKoordinat[1]+75# ağaçlar sadece trex in düzleminde çıktığından Trexin düzlemini alıyoruz

pt3=trexKoordinat[0]
pt4=trexKoordinat[0]+400



veri=()
while True:


    Ekran=np.array(sct.grab(monitor))#Tekrar ekran görüntüsünü alıyoruz


    Ekran_gri=cv2.cvtColor(Ekran,cv2.COLOR_BGR2GRAY)#Ekran görüntüsünü gri tona çeviriyoruz
    Agac_Ekran = Ekran[pt1:pt2, pt3:pt4]#ağaçların ve Trexin bulunduğu bölgenin ekran görüntüsünü alıyoruz
    Agac_Ekran_Gri=cv2.cvtColor(Agac_Ekran,cv2.COLOR_BGR2GRAY)#Ağaçların ve Trexin bulunduğu bölgeyi gri tona çeviriyoruz
    minn,Ekran_filtre=cv2.threshold(Agac_Ekran_Gri,100,255,cv2.THRESH_BINARY)#filtreleme işlemi yapıyoruz

    erosion=cv2.erode(Ekran_filtre,kernel,iterations=1)#Filtrelediğimz bölgedeki siyahların belirginliğini artırıyoruz
    cv2.imshow("Erosion",erosion)#bölgeyi gösteriyoruz



    cv2.circle(Agac_Ekran,(155,23),4,(0,255,0),3)#referans noktası
    #cv2.imshow("Agac_Ekran",Agac_Ekran)#trex ve ağaçların bulunduğu bölgeyi yalın halde gösteriyoruz
    cv2.circle(Ekran_filtre,(155,23),4,(0,255,0),3)#referans noktası







    if erosion[23,155]==0:# eğer (23,140) pixelleri siyahsa yani herhangi bir ağaç veya başka birşey varsa

        pyautogui.press("space")# space tuşuna bas


    if cv2.waitKey(25) & 0xFF ==ord("q"):#Eğer ekranda q tuşuna basılmış ise tüm ekranları kapat ve döngüden çık yani programı sonlandır
        cv2.destroyAllWindows()
        break
    cv2.rectangle(Ekran,trexKoordinat,(trexKoordinat[0]+hTrex,trexKoordinat[1]+wTrex),(0,0,0),3)#Trexi kare içine alıyoruz
    cv2.imshow("Ekran_Filtre",Ekran_filtre)
    #cv2.imshow("Ekran",Ekran)#Trexin işaretlenmiş ve Referans noktamızın işaretlenmiş görüntüsü









