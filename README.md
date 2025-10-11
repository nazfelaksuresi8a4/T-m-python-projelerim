##UYARI Buradaki "en güçlü" "en kapsamlı" "ilk" gibi kelimeler sadece kendi içimde yaptıgım karşılaştırmaları yansıtıyor genel bir kavram olarak söylemedim yanlış anlaşılmasın. 


#NOT: Buradaki tüm projeleri solo yani tek başıma geliştirdim

# Bazi python-projelerim
burda bazı python projelerim var

4+ yıldır pythonda kod yazıyorum proje geliştiriyorum

şu zamana kadar çok ciddi olan projelerimin bir kaçı aşağıda yazılı 


---------------------------------------------------------------------------------------------------------------------------------
1- Sanal piyano projesi 
---------------------------------------------------------------------------------------------------------------------------------
bu projede yine pyqt5 + tkinter toolkitleri ile tasarlandı ve pygame winsound alt yapısı mevcut

burda gerçekçi bir piyano görüntüsü var ses ayarlamaları ve daha bir çok şey için ayarlar mevcut 

görünümü kullancıı tarafından özelleştirilebilen ilk projem ancak bunların pek bir önemi yok bu projede ayrıca 

bir özellik mevcut bastığınız notalar bir yere kaydoluyor ve o notaları tekrar çalmak isterseniz ona bakarak tekrar çalabiliyorsunuz 

teknik olarak basit bir piyano ancak orta teferruatlı bir özellik yapısına sahip görüntüsüde aynen bir piyano gibi 


---------------------------------------------------------------------------------------------------------------------------------
2-Makine görü projesi:
---------------------------------------------------------------------------------------------------------------------------------

bu projede 5+ makine görü tekniği ile istediğiniz fotoğrafın işlenmiş halini alabiliyordununz 
programın en bariz özelliklerinden birisi ise 2 tane renderer yani 3 tane fotoğraf göstericisi olması
1. gösterici detaylı ve gui ın içine gömülü bir matplotoib backend'i 2. olan ise matplotlib'in ana renderer canvası yani ana göstericisi
bu göstericide ise 1. de olmayan navigationtoolbar mevcut 3. renderer ise OPENCV'nin kendi resim gösterme yöntemi ile hem gömülü hemde dıştan gösterilebiliyor

bu programda dinamik bir context managerda bulunuyor yani istediğiniz dosyayı program içindeki dosya yöneticisinden açıp seçip direkt olarak işleyebiliyorsunuz

bu programda fotoğraflar işlenirken fotoğrafların özelliklerini ayarlayabiliyorsunuz yani fotoğraf üzerinde oynama yapıp tekniği ona göre uygulayabiliyorsunuz

en önemli olarakta bir loglama sistemi mevcut programda göz ile görülebilen bir yerde olan log ekranına yaptıgınız her işlem kaydediliyor zaman damgası işlem tipi ve daha bir çok işlem verisi 
oraya işleniyor ve bu log ekranını isterseniz gizleyebilirken istrersernizde logları bir dosyaya kaydedebiliyor aktarabiliyorsunuz

ayrıca bu programdaki arayüz pyqt5 ile tasarlandı css kısmı çok yok daha çok teknik bir arayüze sahip 

kapsamlı bir proje bu kadarı ile sınırlı değil 

---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
3- hava durumu analiz programı 
---------------------------------------------------------------------------------------------------------------------------------

bu program şu ana kadar geliştirdiğim en kapsamlı projelereden biriydi burda hem CLİ hem GUİ desteği mevcut olan proje 

bir web sitesinden selenium ile verileri web scrapping yöntemi ile büyük bir tablodan çekiyor ve tamı tamına 1 yıllık verilere erişardımları ile güzel şekilde clean data olarak bize 

çok sıcak - sıcak - ılık - soğuk - çok soğuk - dondurucu soğuk 

sınıflarına olacak şekilde tamı tamına 6 farklı sınıfa ayırıp bize veriyor program biraz hantal asenkorn yapıları tam olarak burada kullanılamadı sonradan düşünülen bir şey oldugu için ve 
zaman baskısı yüzünden biraz hantal oldu bu verileri analiz ediyor ve bize veriyor çıktıları gui kısmıda aslında buna benzer ancak biraz farklı yanları var gui kısmıda aynen bu dediklerimi eksiksiz şekilde 
yapabiliyor ancak gui bunların yanındada bize şu imkanları sunuyor (trimf-trampf) (derece) grafiklerini bize doğru şekilde çiziyor ve yine 4 lü renderer sistemi bulunmakta programın içine gömülü göz ile görülen trimf tramf fonksiyon grafikleri kendi kendine çizilip gösteriliyor 
ancak hava sıcaklıgı gibi dereceler ekstra bire buton ile dışarıdan gösterim ile kullanıcıya sunuluyor ancak bu dediklerim her ikisi içinde geçerli yani her ikiside istr dışarıda ister içeride açılabiliyoır maksat gui çok dolmasın 4 ten 2 ye bölünmüş şekilde grafikler sunuluyor 

grafikten ziyade guida program daha fresh çalışıyorim sağlayabiliyor

bu veri setini bulanık mantık ile arka planda algoritmalar kullanarak sckit-fuzzy yani diğer bir adı ile skfuzyy ile ve bazı numpy y
ve bunların dahasıda var  sadece bunlara kısıtlı değil 

---------------------------------------------------------------------------------------------------------------------------------
 
---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
4- .wav dosyası analiz projesi 
---------------------------------------------------------------------------------------------------------------------------------
bu proje oldukça kapsamlı adındanda belli olacağı üzere bir gui a sahip ayrıca burada modüler bir qss dosyası ile css tanımlandı o yüzden güzel bir arayüz var artık arayüz teknik değil 

programda gerçek zamanlı ses sinyali analizi yapılıyor burada matplotlib ve pyqtgraph ikilisi kullanıldı ancak iki canvasta custom yani hiç biri dışardan gelen bir sığıntı koyiyimda gitsin havası vermiyor 
ilk olarak programda çok yönlü seçenekler var bu seçenekelreedn bazıları ses analizi ile alakalı bazıları ise grafik görünümü ve grafik çizimi ile alakalı ayrıca burada yandan açılır animasyonlu bir menüde var bu emnünün içeriği en sonda açıklanacak 

şimdi ise ilk seçeneğe gelicem 

1- grafik ayarları(GÖRSEL) 
---------------------------------------------------------------------------------------------------------------------------------
dinamik ses seviyesi grafik rengi çizgi kalınlığı grafik monitörüğ arka plan rengi değiştirme grafik gerçek zamanlı çizilirken yaptıgnız ayarlar dinamik olarak değişiyor tabi isteyen başlatmadan önce ayar yapabilir  

2- grafik ayarları (TEKNİK) dediğim gibi iki farklı canvas mevcut 1. pyqtgraph 2. matplotlib pyqtgraph gui içinde bulunurken bu projede matplotlib dockwidget yani kayar widget içinde yine bize içeride veriliyor ancak bunu isteyen dışarıya alabiliyor 
1. seçenek ses ile senkronize çizim burada biraz çağ dışı gibi dursada pygame ve wave ile senkronizasyon yapıldı maksimum 5 saniyeye çıkabilen bir gecikme var bu ihtimal oldukça düşük ve sadece çok kötü sistemlerde bile zar zor gecikme yaşanıyor ilk olarak wave ile ses işleniyor
daha sonra işlenen ses dataları ikincil fonksiyona atanıyor atanırken pygame sesi çalmaya başlıyor ve fonksiyon timer ile çağırılıp ikincil fonksiyon devreye sokuluyor ikincil fonksiyonda FİFO  algoritması mevcut grafikler 10000 noktayı geçince tail yani kuyrukları siliniyor ve tekrar devam ediyor
yani ksama gibi bir durum söz konusu bile değil düzgünce optimize edilmiş bir sistem
---------------------------------------------------------------------------------------------------------------------------------

2- seçenek ise daha çok ses verisini teknik incelemeye almak ve ciddi analizler yapmak için bir seçenek matplotlib dock widget olarka geliyor ve optimizeli ekran sayesinde büyük verilerde bile hafif kasmalar ile grafikte yakınlaştırma uzaklaştırma sağ sol yukarı aşağı inceleme gibi şeyleri yapabiliyorsunuz 
---------------------------------------------------------------------------------------------------------------------------------

2- grafik ayarları(KULLANICI) 
---------------------------------------------------------------------------------------------------------------------------------

bunlar sadece butonlardan ibaret sırası ile 3 tane buton var 1-grafiği sıfırla 2-rastgele grafik 3-monitördeki grafiği kaydet 

bu butonlar her iki canvastada bulunuyor hem gerçek zamanlı olanda hemde teknik analiz için geliştirilen o ikinci kısımdaki canvasta mevcut..


3- ses dosyası bilgileri(TEKNİK)
---------------------------------------------------------------------------------------------------------------------------------

ses dosyası işlendikten sonra yandaki panelde ses dosyasının ses kanalı, sesin süresi hms cinsinden,  sesin bit sayısı, ve sesin kaç hz oldugu bize veriliyor


4-üst panel(KULLANICI)
---------------------------------------------------------------------------------------------------------------------------------

üst panelde mevcut tanımlanan ses dosyası sesi durdur/devam ettir gibi seçenekler mevcut 

5- context manager(KULLANICI-TEKNİK)
---------------------------------------------------------------------------------------------------------------------------------

Burada ses dosyasının seçilmesi için bir context manager var bu manager belirli klasör yoluna gidip klasör içinde gezinmezine o klasör içindeki ses dosyalarını analiz edebilmenize yarıyor o gui içindeki dosya sistemindeki bir ses dosyasına tıkladıgınıza o ses dosyasının yolu alınır ve size onu analiz edebilmenizi sağlar detaylı bir dosya sistemi mevcut 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1- dosya sistemi paneli(KULLANICI-TEKNİK)

dosya sistemi panelinde 3 buton 1 dosyas sistemi ve bir hedef klasör inputu bulunmakta 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. buton - girilen dizini tanımla: inputa girilen dizini dosya sisteminin dizini olarka ayarlar
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. buton - dosya sistemini sıfırla: bu buton adı üstünde dosya sistemindeki tüm ayarları sıfırlar bu dizin ayarda dizin ayarıdır
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3. buton - ses dosyasını işle: bu buton seçtiğiniz ses dosyanı sizin seçtiğiniz seçeneğe göre işler(grafik ve ses verisi olarak size geri döner)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
6- ses slider'ı(KULLANICI-TEKNİK)

bu slider ses ile senkronize şekilde çıkan grafikte arkadaki sesin seviyesini ayarlamak için kullanılır hem analizden işlemeden önce hemde işlem analiz sırasında dinamik olarak ses seviyesi ayarlanabilir
---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
7- Eğlence kısmı 

Bu şu anlık bu projedeki açık ara en gereksiz özellik olmasına rağmen insanları eğlendirmeyi başarıyor

size en son bahsedicem dediğim yan menüde bulunan 5 özellikti

bu özellikler seçildiğinde ses grafiği kısmı meşgul olmadıgı sürece sizi eğlendirmek için analiz grafiği yerine hareketli ve animasyonluı grafikler içeriyor 

bunları sırası ile şöyle 

1-animasyonlu sinüs grafiği 

2- animasyonlu kosinüs grafiği

3- animayonlu gürültü grafiği 

4- animasyonları durudur

olarak 3 e ayrılır 
---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
8-Dosya-Görüntü-Yardınm-Yan menü olarak ayrılan üst menü bar'ı:
.........
.........

.........
.........

##ve son##

ancak bu projeye daha eklencek şeyler var örneğin:

FFT: FAST-FOUİRER-TRANSFORM SWAP'i ----->> analiz kısmında ses grafiği ile fft seçeneği olucak 

hangisi seçilirse program onu yapıcak 

###Muhtemelen siz bunları okurken bunlar eklenmiş olucak##

NOT: (GUNCELLEME)FFT Özelliği programa eklendi hatalar fixlendi
---------------------------------------------------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
**7- Deprem takip sistemi:**
---------------------------------------------------------------------------------------------------------------------------------
Bu proje cok kapsamlı olmasada amacı mantığı ve kullanımı ile kullanıcıları bilgilendirmeyi amaçlayan bir cross-platform programdır..

bu projede ortada bir harita vardır ve bu haritada sağ ve sol panel olacak şekilde Türkiyedeki istediğiniz depremleri sorgulayabiliyorsunuz

sağ panel- Deprem sorgulama kısmı

sol-panel- Son depremleri sorgulama kısmı

ayrıca son depremler listesine her sorguda son depremler aktarılıyor 

son depremler kısmı web kaynaklsrındsn son 100 depremi çekip tüm detaylarını listeye aktarıyor

istersek listeden seçip depremiharitada görselleştirebiliyoruz 

ayrıca programda hem api hemde web kazıma denilen method ile veri çekme özelliği mevcut 

çoklu çekirdek (thread) özelliği ile büyük işlemler aynı andayyapılabiliyor(paralel işlem) h

GÖRSELLEŞTİRME TÜRLERİ:

Marker-Popup

Heatmap


VERİ GÖSTERME TÜRLERİE

SATIR-SÜTUN(Tabler widgeti) 


ve haritada çiz ve sorgula seçenekleri Deprem bölgelerini haritada işaretliyor ayrıca işaretli yerlere popup attığı için Ülke İlçe Büyüklük gibi verilerde orada doğru şekilde gösteriliyor 

proje modüler ve geliştirilmeye açık olduğu için update alıcak o yüzden bu anlattıklarım ile kalmayacak o yüzdende lütfen bunu küçük bir proje olark görmeyin şu andada ilk başta dediğim gibi çok bir şeyi olmasada yakında olacak..
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---------------------------------------------------------------------------------------------------------------------------------
**8- Sistem takip aracı**
---------------------------------------------------------------------------------------------------------------------------------
Bu araç bildiğiniz üzere CLİ(command-line-interface) üzerine kurulu ve sisteminizin/ağınızın kullanım değerlerini size veriyor

iki seçeneği var 

1. Sistem takibi

2. Ağ takibi

bu iki seçenekteki görüntüleme biçimleride aynı 
clide bir grafik sistemi mevcut ve değerlere göre 
hareket ediyor ve yanındada sayılarını veriyor 
yani iyi bir şekilde kullanıcıya değerleri verebiliyor

kullanması ve kontrol etmesi cok basit ve sade
CLİ ve görsel güzelliğe önem verenler için güzel bir araç


-----------------------------------------------------------------------------------------------------------------------------------------

_______________________________________________________________________________________________________________________________________
**9-MRI Analiz Programı**
HMS[19:14:30]
YMD[2025.08.30]

Mrı-BT-CT-PET görüntülerini analiz edebilen yapay zeka destekli bir program 
-------------------------------------------------------------------

#TEMEL ÖZELLİKLER#

1- Kontrastlı bölge gösterme

2- Görüntü İyileştirme

3- Hatları Netleştirme

4- Tümör tespiti

5- Organlardaki hastalıklı dokuları tespit etme

6- .nii.gz .nii dosyalarını işleyebilme 

7- .png  .jpg   .img  dosyalarını işleyebilme

8- Mrı görüntülerini dilim dilim(slice) olarak gösterebilmek(baştan sona sondan başa özelliği ile) 

9- Çoklu mrı gösterimi

10- Farklı tıbbi verileri işleme(CT-BT-MRI-PET) 

11- MRI BT CT yorumlama [Yapay zeka]

12- Farklı görüntü işleme tekniklerini görüntülere uygulayabilme 

#ARAYÜZ FRAMEWORKLERİ#

PyQt5/QtPy -> Ana arayüz

Kivy/Tkİnter -> Ekstra bileşenler için 

#BACKEND MODÜLLERİ#

Numpy -> veri analizi için
Opencv-pyton[cv2] -> Görüntü işleme için
Pandas -> medikal tablolar üzerinde işlem gerçekleştirebilmek için
Skimage -> detaylı medikal görüntü işlemek için
Matplotlib -> Grafik gösterimi / Resim gösterimi -- renderer görevi için
Pyqtgraph -> Gerçek zamanlı grafikler için
Requests -> APİ bağımlılıkları için
Tensorflow -> sinir ağları için
Keras -> Hazır modeller için 


#DETAY#

Bu proje geliştirmeye açık ve modüler şekilde tasarlanacak. Bu yüzdende Güncellemelere açık bir proje olacak.

NOT: !!BU PROJE SOLO OLARAK GELİŞTİRİLMEKTEDİR!!

BİLGİLENDİRME: Proje geliştikçe bu repoya gelişmeler aktarılacaktır 

-TR-TR-



__________________________________________________________________________________________________________________
**Otobüs Takip Sistemi (OTS)**
#web scrapping kaynağı: https://www.eshot.gov.tr/
#opsiyonel(harita apisi): https://www.eshot.gov.tr/
#otobüğs-dıurak api kaynağı: 

#proje amacı: bu proje belirtilen duraktan geçen otobüslerin hangi sıra ile geçtiğini listeyen bir program olacak
__________________________________________________________________________________________________________________

##evet aslında daha bir çok projem var ama aralarından seçerek bunları yazdım##

---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
