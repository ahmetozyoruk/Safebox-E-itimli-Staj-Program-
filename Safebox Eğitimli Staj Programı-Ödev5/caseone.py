import pymongo
import random

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create the "flaskmongodb" database
db = client["flaskmongodb"]

# Create the "users" collection
users_collection = db["users"]

# Turkish names
turkish_names = [
    "Ahmet", "Mehmet", "Mustafa", "Ali", "Ayşe", "Fatma", "Emine", "Hatice", "Zeynep", "Ömer",
    "Hüseyin", "Hasan", "Ebru", "Selin", "Gülay", "Burak", "İsmail", "Aylin", "Cem", "Ceren",
    "Erdem", "Gamze", "Gül", "Kadir", "Kemal", "Nur", "Pınar", "Serdar", "Şevval", "Uğur"
]

# Turkish job titles
turkish_jobs = [
    "Mühendis", "Doktor", "Avukat", "Öğretmen", "Eczacı", "Hemşire", "Polis", "Mimar", "Diş Hekimi",
    "Oyuncu", "Yazar", "Sanatçı", "Satış Temsilcisi", "Bilgisayar Programcısı", "Grafiker", "Kasiyer",
    "Şef", "Garson", "Tercüman", "Hizmetli"
]

# Generate and insert 50 random data entries with Turkish names and job titles
for _ in range(50):
    name = random.choice(turkish_names)
    age = random.randint(0, 50)
    job = random.choice(turkish_jobs)
    description = 1

    # Create the data entry
    user_data = {
        "Name": name,
        "Age": age,
        "Job": job,
        "Description": description
    }

    # Insert the data entry into the "users" collection
    users_collection.insert_one(user_data)

