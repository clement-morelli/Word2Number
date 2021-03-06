from flask import Flask
import psycopg2
import datetime
import pytz

def get_db_connection():
    HOST = "postgres"
    USER = "clement"
    PASSWORD = "12345"
    DATABASE = "call_db"
    PORT = "5432"
    # Connect to an existing database
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
    return conn

def add_call_to_db(request,result):
    time=datetime.datetime.now()
    timezone = pytz.timezone("Europe/Paris")
    time = timezone.localize(time)
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO Word2Number2 (time, request, result)'
                'VALUES (%s, %s, %s)',
                (time, request, result))
    conn.commit()
    cur.close()
    conn.close()
    return 0

conn = get_db_connection()
cur = conn.cursor()
sql = '''CREATE TABLE IF NOT EXISTS Word2Number2(
    time timestamp NOT NULL,
    request TEXT NOT NULL,
    result TEXT NOT NULL
    ); '''
cur.execute(sql)
conn.commit()
cur.close()
conn.close()


api = Flask(__name__)

@api.route('/ready')
def ready():
    add_call_to_db("status","ok")
    return {"status": "ok"}


@api.route('/<word>')
def Word2Number(word):
    value =''
    word = word.lower()
    word = word.replace(" ", "")
    for caractere in word:
        if caractere.isdigit() == True :
            value=value + caractere
        elif caractere.isalpha() == True :
            value=value + str(ord(caractere) - 96)
        else : 
            print("On skip")
    add_call_to_db(word,value)
    return {"result": value}