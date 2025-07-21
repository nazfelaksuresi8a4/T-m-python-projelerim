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
not: yapay zeka hocasının bana 8. sınıfta 1. dönemde verdiği proje güzel şekilde tamamladım ve kabul etti 🫡🫡
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
not: yapay zeka hocasının bana 8. sınıfta 2. dönemde verdiği proje kabul etti🫡🫡
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
---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
5- UMBRELLA(Siber güvenlik port tarama aracım)

bu araç ağ programlama mantıkları ile programlanan bir siber güvenlik aracı pyqt5 arayüzlü olmasına rağmen tasarımı kırmızı-siyah olacak şekilde tasarlandı kötü yanı ise bu default 

bu projedeki özellikler:

port tarama

açık kapalı port tespiti 

tüm portları destekleyen yapı 

gelişmiş loglama sistemi 

1-detaylı ip-mapper konsolu

2-detaylı port-mapper konsolu 
---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
ayrıca bu progam çift thread çekirdeğine sahip 1- gui 2-logic(yani teknik işlemler)

1- seçenekte cmd den destek alarak cmd de bulunan ip ile alakalı bir çok tarama işlemini gerçekleştriebiliyor 

2- seçenekte ise 1. seçeneğin aynısı olacak şekilde sadece ip yerine port ile alakalı olanları gerçekleştirebiliyor 

bu iki seçenekte çalışır dumudadır ve bir çok tarama türüne ev sahipliği yapar 
---------------------------------------------------------------------------------------------------------------------------------

***son olarak nmap'in bir çok tarama türünü destekler***

bunlar sırası ile 


***TCP Syn (half open) Scan.
  FIN (stealth) Scan.
  Xmas Scan.
  Ping Scan.
  UDP Scan.
  IP Protocol Scan.****


bu şekildedir 

daha bir çok özelliğe ev sahipliği yapar
---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
6-Sayısal loto projesi 
---------------------------------------------------------------------------------------------------------------------------------
bu proje önceden belirlenen bir veri setinde "uzunluk fark etmeksizin" 

her işlemi yapabilen bir projedir 

bu projede sadece cli desteği vardır ancak bu proje teknik açıdan çok güçlü 

---------------------------------------------------------------------------------------------------------------------------------
teknik-özellikleri 
---------------------------------------------------------------------------------------------------------------------------------

*cross-platform*

*yüksek düzey hata koruması//HATA YAKALAMA*

---------------------------------------------------------------------------------------------------------------------------------
Program içi özellikleri
---------------------------------------------------------------------------------------------------------------------------------

1-Bütün çekiliş listesi(ARŞİV)
2-En çok çıkan sayılar        
3-Tahmin al
4-Tek-çift oranı
5-Tek-çift dağılımı
6-Asal sayılar çok çıkanlar   
---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
özellik açıklamaları
---------------------------------------------------------------------------------------------------------------------------------
1- bütün çekiliş  lsitesini sıralayan seçeneketir

2- istediğiniz yıla göre veya hepsini olacak şekide en çok çıkan sayıları size veren seçenektir

3-Tahmin almak için kullanılan seçenektir sayı tahmininde orta düzeydedir

4-istediğiniz yıla-veya tüm yıllara göre tek çift oranını hesaplayıp size veren seçenektir

5-istediğiniz yıla-veya tüm yıllara göre tek çift dağılımını hesaplayıp size veren seçenektir

6-istediğiniz yıla-veya tüm yıllara göre Asal sayılardan en çok çıkanları size veren seçenektir
---------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------------------
Ekstra özellikler
---------------------------------------------------------------------------------------------------------------------------------

*veri filtreleme algoritmaları mevcut*

*veri temizleme algoritmaları mevcut*

*bazı sıralama algoritmaları çıktı alırken kullanıldı*

--------------------------------------------------------------------------------------------------------------------------------

##evet aslında daha bir çok projem var ama aralarından seçerek bunları yazdım##

---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------
