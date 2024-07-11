import requests
import psycopg2
import threading

my_conn = psycopg2.connect(database='n48', user='postgres', password='1234', host='localhost', port=5432)
cur = my_conn.cursor()

user_url = requests.get('https://dummyjson.com/users')
product_url = requests.get('https://dummyjson.com/products')

users_list = user_url.json()['users']
products_list = product_url.json()['products']

insert_users_query = '''
    insert into users (firstname,lastname,maidenName,age,gender,email,phone,username,password,birthDate,image)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
'''

insert_products_query = '''
    insert into products (title,description,category,price,rating,stock,brand,tags)
    values (%s,%s,%s,%s,%s,%s,%s,%s);
'''


def products_insert():
    for i in range(0, 5):
        cur.execute(insert_products_query,
                    (products_list[i]['title'], products_list[i]['description'], products_list[i]['category'],
                     products_list[i]['price'], products_list[i]['rating'],
                     products_list[i]['stock'], products_list[i]['brand'], products_list[i]['tags']))
        my_conn.commit()
    print('insert products success!')


def users_insert():
    for i in range(0, 5):
        cur.execute(insert_users_query, (
            users_list[i]['firstName'], users_list[i]['lastName'], users_list[i]['maidenName'], users_list[i]['age'],
            users_list[i]['gender'], users_list[i]['email'],
            users_list[i]['phone'],
            users_list[i]['username'], users_list[i]['password'], users_list[i]['birthDate'],
            users_list[i]['image']))
        my_conn.commit()
    print('insert users success!')


thread1 = threading.Thread(target=products_insert)
thread2 = threading.Thread(target=users_insert)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
