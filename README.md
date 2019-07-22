# Bot


BOT

bu bot googlenin Trex oyununu oynuyor. Botu görüntü işleme teknikleri ile yazdım zaten dosyanın içinde her satır için açıklama ekledim umarım anlaşılır olmuştur ben 1250 puana kadar gelebildim çok az algılamama oluyor genelde oyun çok hızlandığı zaman ağaçlara değiyor veya 2 ağaç arası mesafe çok az olursa değme oluyor . Üstten gelen yarasaları zaten hiç görmüyor program alttaki ve ortadan gelenleri görüp zıplayabiliyor.


ÇALIŞMA MANTIĞI


Çalışma mantığına gelince. Önce görüntüyü tanımayla yapmaya çalıştım fakat bazı ağaçların boyutları büyük bazılarınınki diğerlerine göre daha küçük ve işin içinde yarasalarda olduğundan pek ilerleyemedim bazı bilgi eksikliklerinden dolayıda pek ilerleyemedim mesela ağaçların boyutları önemsiz olsaydı yani programa görüntüyü verdiğimde her türden boyutlu ağacı bulsaydı belki görüntüyü tanıma ile de devam edebilirdim bu konuda google'dan biraz araştırma yaptım fakat birşey bulamadım sonra bu fikir geldi aklıma. Çalışma mantığı şu şekilde öncelikle bizim Program Trexi tanıyor ve  koordinatlarını bir yere not ediyor sonra bu not ettiği koordinatlar yardımıyla bir alan oluşturuyor bu alan bizim Treximizin ve ağaçlarımızın bulunduğu bölge. Bölgeyi de oluşturduktan sonra bu bölgeyi  Gri tona  çeviriyor çevirdikten sonra siyah bölgeleri tam siyah beyaz bölgeleri tam beyaz yapıyor. Sonra bu siyah bölgelerin alanını artırıyor yani mesela bizim ağacımız 40 pixel en 40 pixel boya sahipse bu alan 60 pixel e 60 pixel gibi birşey oluyor. Sonra bizim bir referans noktamız var bu noktadaki rengimiz siyah olunca yani bir nesneyle karşılaşınca zıplama işlemi gerçekleştiriyoruz bu böyle devam ediyor 

KARŞILAŞTIĞIM SORUNLAR

Evet gelelim karşılaştığım sorunlara. Öncelikle ilk sorun şu benim belirlediğim referans noktası ile Trexin nesneyi algılama noktası tam olarak uyuşmuyor yani mesela ben Trexden 150 pixel sonrasını referans olarak aldım ama Trex kendisinden 75 pixel sonrasını algılıyor. Gözlemlerime göre bir sıkıntı çıkarmıyor veya çıkarıyor ben fark göremedim ama sonuç olarak benim istediğim şekilde çalışmıyor

İkinci sorun şu

oyun aşırı hızlandığında bazen nesneyi görmeme gibi bir durum olabiliyor fakat ben bunu kendi bilgisayarımdan kaynaklanıyor olabileceğini düşünüyorum bilgisayarım bayağı bir eski ve sistem özelliklerim düşük. Ayrıca bizim ekrandan aldığımız görüntü 20 30 fps arası değişiyor belki bu yüzden de bazen algılamama problemleri ortaya çıkıyor olabilir 


ÇALIŞTIRMAK İÇİN

Çalıştırmak için öncelikle verdiğim oyun sitesine girin sonra oyunu başlatıp başka bir ekrana geçin bu sayede oyun donacaktır. Daha sonra size verdiğim Bot.py dosyasını idle üzerinden açın yani hani kod yazdıktan sonra f5 ile çalıştırıyoruz ya o kısımda açın ve çalıştırın çalıştırdıktan sonra oyun penceresini öne alın zaten program otomatik olarak trexi tanıdıktan sonra çalışacaktır başka birşey yapmanıza gerek yok klavyede bir tuşa basmazsanız o ağaç veya yarasa gördüğünde space tuşuna basacak.Programdan çıkmak için açılan herhangi bir ekranı öne alıp q tuşuna basmanız yeterli olacaktır eğer bu şekilde kapatamazsanız çalıştırkdan sonra ekrana gelen idleyi kapatırsanız yine program sonlanacaktır

not: program Trexi tanıdıktan sonra eğer pencerenin yerini değiştirirseniz çalışmaz.
