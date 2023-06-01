# Safebox Cyber Security Data Science Eğitimi - Ödev 4

## İçerikler

 * [Soru_1](#Soru_1)
 * [Örnekler](#Örnekler)
 * [Soru_2](#Soru_2)

## Soru_1
## Stored Procedure ve Trigger  neden kullanılır?  olumlu ve olumsuz etkileri nelerdir? 

Stored Prosedürler ve Triggers, veritabanı yönetim sistemlerinde kullanılan önemli bileşenlerdir. Bunlar birçok fayda sağlar, ancak bazı dezavantajları da vardır. Stored prosedürler ve Triggersin kullanımının pozitif ve negatif etkilerini inceleyelim:

Stored Prosedürler:
Pozitif Etkiler:
1. Modülerlik ve Yeniden Kullanılabilirlik: Stored prosedürler, bir dizi SQL ifadesini tek bir birime kapsüle etmenize olanak sağlar ve bu birim farklı uygulama parçalarında yeniden kullanılabilir. Bu modülerliği teşvik eder, kod tekrarını azaltır ve bakımı geliştirir.
2. İyileştirilmiş Performans: Stored prosedürlerdeki SQL ifadelerinin önceden derlenmesi, rastgele sorgulara kıyasla daha verimli bir şekilde çalışmasını sağlar. Özellikle karmaşık sorgular için daha hızlı veri alımı ve işleme sağlayabilir.
3. Geliştirilmiş Güvenlik: Stored prosedürler, kullanıcılara doğrudan tablo erişimini kısıtlayarak güvenlik önlemlerinin uygulanmasına yardımcı olabilir. Bu, veri manipülasyonu üzerinde ince ayrıntılı kontrol sağlar ve yetkisiz erişimi önler.
4. Azaltılmış Ağ Trafiği: Stored prosedürler veritabanı sunucusunda çalıştırıldığından, yalnızca prosedür çağrısının ağ üzerinden iletilmesi gerekir, birden çok SQL ifadesinin gönderilmesi gerekmez. Bu, ağ trafiğini ve gecikmeyi azaltır.

Negatif Etkiler:
1. Öğrenme Süreci: Stored prosedürlerin geliştirilmesi ve sürdürülmesi, genellikle veritabanı yönetim sisteminin ve kullanılan programlama dilinin özel bilgisini gerektirir. Bu, Stored prosedür geliştirme konusunda deneyimi olmayan geliştiriciler için öğrenme sürecini artırabilir.
2. Hata Ayıklama ve Test Etme: Stored prosedürlerin hata ayıklanması ve test edilmesi, bağımsız SQL sorgularını hata ayıklamaktan daha karmaşık olabilir. Prosedürlerin doğruluğunu sağlamak için uygun test yöntemleri ve araçları gereklidir.
3. Tedarikçi Bağımlılığı: Stored prosedürler genellikle belirli bir veritabanının yordamsal dilinde (örneğin, Oracle için PL/SQL veya SQL Server için T-SQL) yazılır. Farklı bir veritabanı sistemine geçmeye karar verirseniz, Stored prosedürleri yeni sistem diline yeniden yazmanız gerekebilir ve bu da tedarikçi bağımlılığına yol açar.

Triggers:
Pozitif Etkiler:
1. Veri Bütünlüğü ve Tutarlılığı: Triggers, belirli olaylar gerçekleştiğinde (örneğin, kayıt ekleme, güncelleme veya silme) otomatik olarak işlemler yaparak iş kurallarını uygulamanıza ve veri bütünlüğünü sağlamanıza olanak tanır. Veri doğrulamasını gerçekleştirebilir, kısıtlamaları uygulayabilir ve referans bütünlüğünü koruyabilir, böylece veritabanı içinde veri tutarlılığı sağlanır.
2. Denetim Kaydı Tutma: Triggers, veritabanında yapılan değişiklikleri kaydetmek için kullanılabilir ve denetim kayıtlarının oluşturulmasını sağlar. Bu, uyumluluk amaçları, kullanıcı etkinliğini takip etme ve sorunları araştırma açısından değerli olabilir.
3. Basitleştirilmiş Uygulama Mantığı: Bazı iş mantığını Triggerse taşıyarak, veritabanına veri doğrulama ve manipülasyon gibi görevleri yükleyerek uygulama kodunu basitleştirebilirsiniz. Bu, kod okunabilirliğini ve sürdürülebilirliği artırabilir.

Negatif Etkiler:
1. Gizli Mantık: Triggers, belirli olaylar gerçekleştiğinde otomatik olarak çalışır, bu da sistemin tam akışını takip etmeyi ve anlamayı zorlaştırabilir. Eğer Triggers iyi belgelenmemiş veya yönetilmemişse, gizli mantık oluşabilir ve sistem bakımını zorlaştırabilir.
2. Performans Etkisi: Kötü tasarlanmış veya verimsiz Triggers, veritabanı performansını etkileyebilir. Triggers, veritabanı işleminin bir parçası olarak çalıştırılır ve veri manipülasyon işlemlerine ek yük ekler. Genel sistem performansı üzerindeki etkileri en aza indirmek için Triggersi optimize etmek önemlidir.
3. Test Etme ve Hata Ayıklama: Triggersin otomatik doğası nedeniyle, hata ayıklama ve test etme süreçleri karmaşık olabilir. Triggersin beklenmedik yan etkilere veya sonsuz döngülere neden olmaması için özel bir dikkat gereklidir.

Özetlemek gerekirse, Stored prosedürler ve Triggers modülerlik, yeniden kullanılabilirlik, performans iyileştirmesi, geliştirilmiş güvenlik ve veri bütünlüğü gibi faydalar sağlar. Ancak, öğrenme süreci, hata ayıklama, test etme ve potansiyel performans etkisi gibi zorluklarla karşılaşabilirsiniz. Stored prosedürler ve Triggersi uygulamanızın gereksinimleri bağlamında dikkatlice değerlendirmek ve beraberinde gelen takasları göz önünde bulundurmak önemlidir.


---------------------

## Örnekler

```
CREATE TRIGGER EnforceAgeRestriction BEFORE INSERT ON customers
FOR EACH ROW
BEGIN
    IF NEW.age < 18 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'You must be 18 years or older.';
    END IF;
END;

```

```
DELIMITER //

CREATE PROCEDURE GetCustomerDetails(IN customerId INT)
BEGIN
    SELECT * FROM customers WHERE id = customerId;
END //

DELIMITER ;

```

---------------------

## Soru_2
## Python ile veri tabanı bağlantısı yapıldıktan sonra stored procedure yada trigger kullanıldığı durumda python içerisinde bunu nasıl çağırabiliriz/nasıl bir mantık kurulabilir?

Python ile veritabanı bağlantısı kurulduktan sonra, bir saklanmış prosedürü veya tetikleyiciyi kullanmak için, seçtiğiniz veritabanı bağlayıcısının veya ORM (Nesne-İlişkisel Eşleme) kütüphanesinin sağladığı uygun yöntemleri kullanabilirsiniz. İşte popüler `mysql-connector-python` kütüphanesi kullanılarak yapılan örnekler:

1. Saklanmış Prosedürü Çağırmak:
```python
import mysql.connector

# Veritabanı bağlantısı kurma
cnx = mysql.connector.connect(user='kullanici_adi', password='parola', host='localhost', database='veritabani')

# Bir imleç nesnesi oluşturma
cursor = cnx.cursor()

# Saklanmış prosedürü çağırma
cursor.callproc('GetCustomerDetails', [1])  # Prosedür adı ve parametreleri (varsa) geçirme

# Sonuç kümesini alın
result = cursor.fetchall()

# Sonucu işleme
for row in result:
    print(row)

# İmleci ve bağlantıyı kapatma
cursor.close()
cnx.close()
```
Bu örnekte, `callproc()` yöntemi kullanılarak `'GetCustomerDetails'` adlı saklanmış prosedür çağrılır ve `1` parametresi geçilir. Sonuç kümesi alınır ve gerektiği gibi işlenir.

2. Tetikleyiciyi Çalıştırma:
```python
import mysql.connector

# Veritabanı bağlantısı kurma
cnx = mysql.connector.connect(user='kullanici_adi', password='parola', host='localhost', database='veritabani')

# Bir imleç nesnesi oluşturma
cursor = cnx.cursor()

# Tanımlanan tetikleyiciyi tetiklemek için bir INSERT ifadesi yürütme
cursor.execute("INSERT INTO orders (product_id, quantity) VALUES (1, 10)")

# Yapılan değişiklikleri veritabanına uygulama
cnx.commit()

# İmleci ve bağlantıyı kapatma
cursor.close()
cnx.close()
```
Bu örnekte, tetikleyici, `orders` tablosuna bir `INSERT` ifadesi gerçekleştirerek dolaylı olarak çalıştırılır. İfade yürütüldüğünde ve değişiklikler uygulandığında, tetikleyici mantığı otomatik olarak tetiklenir.

Not: Yukarıdaki örnekler, `mysql-connector-python` kütüphanesini zaten kurduğunuzu ve MySQL veritabanınıza başarılı bir bağlantı kurduğunuzu varsayar. Bağlantı parametrelerini (`user`, `password`, `host`, `database`) kendi yapılandırmanıza göre ayarlayın.

Bu örnekler, Python kullanarak saklanmış prosedürleri çağırmak ve tetikleyicileri çalıştırmak için `mysql-connector-python` kütüphanesini kullanmanın temel

 yaklaşımını göstermektedir. Özel uygulama, kullandığınız veritabanı bağlayıcısına veya ORM'e bağlı olarak değişebilir.
