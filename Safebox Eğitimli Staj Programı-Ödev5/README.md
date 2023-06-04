# Safebox Eğitimli Staj Programı-Ödev5


## İçerikler
 * [Setup_MongoDb](#Setup_MongoDb)
 * [Show_Collection](#Show_Collection)
 * [CaseOne_1](#CaseOne_1)
 * [CaseTwo_2](#CaseTwo_2)
 * [CaseThree_3](#CaseThree_3)
 * [Flask_Curl_Examples](#Flask_Curl_Examples)


## Setup_MongoDb

To install MongoDB using Docker and create a Python script to connect to MongoDB, follow the steps below:

1. Install Docker:
   - For Windows or macOS, download and install Docker Desktop from the official Docker website: https://www.docker.com/products/docker-desktop
   - For Linux, follow the instructions provided by Docker for your specific distribution.

2. Pull the MongoDB Docker image:
   Open a terminal or command prompt and run the following command to pull the official MongoDB image from Docker Hub:

   ```
   docker pull mongo
   ```

3. Run MongoDB container:
   Once the image is downloaded, you can create and start a new MongoDB container using the following command:

   ```
   docker run -d -p 27017:27017 --name mongodb mongo
   ```

   This command starts a new container named "mongodb" and maps the MongoDB default port 27017 from the container to the host system.

4. Verify MongoDB container is running:
   Run the following command to check if the container is running:

   ```
   docker ps
   ```

   You should see the MongoDB container in the list of running containers.

5. Install pymongo package:
   Now, let's install the pymongo package, which is a Python driver for MongoDB. Run the following command to install it:

   ```
   pip install pymongo
   pip install flask
   ```

7. Run the Python scripts:
   Save the Python scripts and run it using the following command:

   ```
   python create_database.py
   python caseone.py
   python casethree.py
   python casetwo.py
   ```

   The script should connect to the MongoDB container, insert a document, and print the inserted document ID as well as the queried document(s) to the console.

## Show_Collection

To show the collections within a MongoDB database, you can use the `show collections` command in the MongoDB shell. Here's how you can do it:

1. Make sure your MongoDB container is running.

2. Open a terminal or command prompt.

3. Connect to the MongoDB container using the MongoDB shell by running the following command:

   ```
   docker exec -it mongodb mongosh
   ```

   This command connects you to the MongoDB container and launches the MongoDB shell.

4. Once you are in the MongoDB shell, switch to the desired database using the `use` command. For example, to switch to a database called "mydatabase", run:

   ```
   use flaskmongodb
   ```

   Replace "mydatabase" with the actual name of your database.

5. To list the collections within the selected database, run the following command:

   ```
   show users
   or
   db.users.find()
   ```

   The command will display a list of collections present in the database you selected.

That's it! You should now see the collections within your MongoDB database listed in the MongoDB shell.
   
## CaseOne_1
   
İlk python dosyanız veri tabanınızdaki Users Collection'ına 50 adet random veri eklemek olacak .  User tablosuna Name , Age(0-50) , Job ve Description (1)olacak şekilde  random veriler eklemeniz gerekecek . Description random olmayacak. Description default 1 olacak şekilde eklemeniz gerekli.

![image](https://github.com/ahmetozyoruk/Safebox-E-itimli-Staj-Program-/assets/64263085/bda76dd9-e369-4319-af3f-f781d2a643bf)

## CaseOne_2

İkinci python dosyanız veritabanına belirli sorgular atmak olacak.Sorgular :

- Users collectionında tüm verileri getiren sorgu
- Users collectionında belirlediğiniz isimdeki kişiyi getiren (İsmi Ahmet olanları getir) sorgu
- Users collectionında yaşı 20'den fazla olanları getiren sorgu
- Users collectionında yaşı 25'den fazla olanların description'ı 0 olacak.
- Users collectionında yaşı 45-48 yaş aralığında olan kişileri silen sorgu
 
## CaseOne_3

Üçüncü Python dosyası ise Flask uygulaması yapmanız . 4 adet endpoint hazırlayacaksınız .  Frontend yapmanız gerekmiyor . Yapan olursa süper olur . POSTMAN üzerinden isteklerinizi atabilirsiniz,derste yaptığımız gibi . URL'ler herkeste aynı olmalı .

1.Endpoint -- Users Collectiona kullanıcıları eklemeli  ve başarılı mesajı döndürmeniz gerekmektedir.(POST)  Endpoint Url -- /adduser
2.Endpoint -- Users Collectionında yaşı 25 ' den fazla olanları dönmeli (GET) Endpoint Url -- /25
3.Endpoint -- Users Collectionındaki tüm kullanıcıları dönmeli (GET)  Endpoint Url --  /
4.Endpoint -- Users Collectionındaki verdiğimiz id'ye göre kullanıcıyı silmeli (POST OR DELETE)  Endpoint Url -- /deleteuser

## Flask_Curl_Examples
   
Some examples of using cURL to interact with the Flask application endpoints:

1. Adding a user:
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "age": 30, "job": "Engineer", "description": 1}' http://localhost:5000/adduser
```

2. Retrieving users over 25 years old:
```
curl http://localhost:5000/25
```

3. Retrieving all users:
```
curl http://localhost:5000/
```

4. Deleting a user (replace `USER_ID` with the actual ID of the user to be deleted):
```
curl -X DELETE -H "Content-Type: application/json" -d '{"id": "USER_ID"}' http://localhost:5000/deleteuser
```

Make sure to adjust the hostname (`localhost`) and port (`5000`) in the cURL commands if you are running the Flask application on a different host or port.

These cURL commands demonstrate how to send requests to the respective endpoints using different HTTP methods (`POST`, `GET`, `DELETE`). You can run these commands in your terminal to interact with the Flask application.
