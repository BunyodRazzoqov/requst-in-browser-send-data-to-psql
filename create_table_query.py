import psycopg2
import threading

my_conn = psycopg2.connect(database='n48', user='postgres', password='1234', host='localhost', port=5432)
cur = my_conn.cursor()


def create_users():
    create_table_query = '''
        create table users(
        id serial primary key,
        firstname varchar(100),
        lastname varchar(100),
        maidenName varchar(100),
        age int,
        gender varchar(100),
        email varchar(100),
        phone varchar(100),
        username varchar(100),
        password varchar(100),
        birthDate varchar(100),
        image varchar(100));
    '''
    cur.execute(create_table_query)
    my_conn.commit()
    print('Table successfully created!!!')


def create_products():
    create_table_products_query = '''
        create table products(
        id serial primary key,
        title varchar(100),
        description varchar(500),
        category varchar(100),
        price float,
        rating float,
        stock float,
        brand varchar(100),
        tags varchar(100));
    '''
    cur.execute(create_table_products_query)
    my_conn.commit()
    print('Table successfully created!!!')


thread1 = threading.Thread(target=create_users())
thread2 = threading.Thread(target=create_products())

thread1.start()
thread2.start()

thread1.join()
thread2.join()
