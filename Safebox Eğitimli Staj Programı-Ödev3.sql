
/* Fİlmlerin süre uzunluklarının ortalama değeri alınıp, 5 birim uzaklığındaki filmleri getir.*/

SELECT * FROM film
WHERE ABS(length - (SELECT AVG(length) FROM film)) <= 5;
