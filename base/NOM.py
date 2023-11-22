from faker import Faker
import random
import json

fake = Faker()
categories = ['C', 'B', 'A', 'S']
users_list = []

for _ in range(100):
    first_name = fake.first_name()
    last_name = fake.last_name()
    username = first_name.lower() + str(random.randint(100, 999))
    password = fake.password()
    category = random.choice(categories)

    user_data = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'password': password,
        'category': category
    }

    users_list.append(user_data)

# Écriture des données dans un fichier texte (.txt)
with open('users.txt', 'w') as txt_file:
    for user in users_list:
        txt_file.write(f"Username: {user['username']}, First Name: {user['first_name']}, Last Name: {user['last_name']}, "
                       f"Password: {user['password']}, Category: {user['category']}\n")

# Écriture des données dans un fichier JSON (.json)
with open('users.json', 'w') as json_file:
    json.dump(users_list, json_file, indent=4)
