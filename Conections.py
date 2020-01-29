import socket
import psycopg2


def database_connection():
    host = read_config("database host")
    user = read_config("database username")
    password = read_config("database password")
    dbname = read_config("database dbname")

    connection = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)

    print("Database connected")
    return connection

def create_socket():
    try:
        ip = read_config("server ip")
        port = int(read_config("server port"))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((ip, port))
        sock.listen(100)
    except Exception:
       print("Неудалось создать сокет")

    print("Socket created")
    return sock

def read_config(word):
    with open("Config\Server configs.txt", 'r', encoding='utf-8') as configs:
        for line in configs:
            if word in line:
                info = line.split('=')[1].replace(' ', '')
                info = info.replace('\n', '')
                return info
        print("Необнаружено {} в Server configs.txt".format(word))