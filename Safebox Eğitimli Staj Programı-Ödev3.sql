
/* Fİlmlerin süre uzunluklarının ortalama değeri alınıp, 5 birim uzaklığındaki filmleri getir.*/

SELECT * FROM film
WHERE ABS(length - (SELECT AVG(length) FROM film)) <= 5;

/* 
Rabbit virus (Fork Bomb) nedir?

Fork Bomb, bir bilgisayar sisteminin kaynaklarını aşırı kullanarak kendini tekrar tekrar çoğaltan ve çalıştıran 
bir zararlı yazılım veya komut serisidir. Bu tür bir saldırı, bir sistemin hızla çalışmaz hale gelmesine ve hatta 
çökmesine neden olabilir.

Fork Bomb, adını "fork" sistem çağrısından almıştır. Fork sistemi çağrısı, mevcut bir işlemi kopyalar ve iki 
ayrı işlemi çalıştırır. Fork Bomb, bu işlemi tekrar tekrar çağırarak sürekli yeni işlemler oluşturur. Her bir yeni 
işlem, daha fazla işlem yaratır ve bu şekilde işlem sayısı hızla artar. Bu işlem zinciri, sistem kaynaklarının 
tükenmesine ve sistemin yanıt vermez hale gelmesine yol açar.

Fork Bomb, genellikle bilgisayar sistemlerine zarar vermek veya hizmet dışı bırakmak amacıyla kötü niyetli kişiler 
veya bilgisayar korsanları tarafından kullanılır. Bu tür saldırılara karşı korunmak için güvenlik önlemleri, güncel 
yazılım ve güvenlik yamalarının kullanılması, güvenilir antivirüs yazılımının yüklenmesi ve bilinmeyen kaynaklardan 
yazılım indirme ve yürütme gibi güvenlik bilincine sahip olmak önemlidir.
*/
