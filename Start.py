import socket
import psycopg2
import hashlib


def start():
    connection = database_connection()  # конект к базе данных
    sock = create_socket()  # создание сокета
    cursor = connection.cursor()

    print('Server started')
    menu(sock, connection, cursor)


def menu(sock, connection, cursor):
    sock, addr = sock.accept()
    print("Client connected with address " + addr[0])
    name = auntification_client(sock, connection, cursor)
    sock.send(str("Приветствую " + name + "\n").encode('utf8'))

    sock.send("Выберите действие".encode('utf8'))
    while True:
        result = sock.recv(1024)
        print(result)
        if result == "chat":
            pass
        elif result == "achievement":
            pass
        elif result == "game":
            pass
        elif result == "exit":
            print("Client with address " + addr[0] + "disconnected")


def auntification_client(sock, connection, cursor):

    while True:
        sock.send("Вход или регистрация?".encode('utf8'))
        answer = sock.recv(1024).decode('utf8').upper()
        if answer == "ВХОД":
            print("вход для клиента")
            sock.send("Your login".encode('utf8'))
            login = sock.recv(1024).decode('utf8')
            sock.send("Your password".encode('utf8'))
            key = sock.recv(1024)

            if auntification_login(login, key, sock, cursor):
                name = login
                return name
        elif answer == "РЕГИСТРАЦИЯ":
            print("регистрация для клиента")
            sock.send("Your login".encode('utf8'))
            login = sock.recv(1024).decode('utf8')

            if auntification_create(login, sock, cursor, connection):
                name = login
                return name
        else:
            sock.send("Неверная команда, выберите действие: вход или регистрация?".encode('utf8'))


def auntification_login(login, key, sock, cursor):
    password = hashlib.md5(key)

    cursor.execute("select password from public.arcanoid_game where login='" + login + "'")
    results = cursor.fetchall()


    if (len(results) > 0) and (password.hexdigest() == results[0][0]):
        sock.send("Successful".encode('utf8'))
        return True
    else:
        sock.send("Неверный логин или пароль".encode('utf8'))
        return False


def auntification_create(login, sock, cursor, connection):
    cursor.execute("select password from public.arcanoid_game where login='" + login + "'")
    results = cursor.fetchall()

    if len(results) == 0:
        sock.send("Your password".encode('utf8'))
        password = hashlib.md5(sock.recv(1024)).hexdigest()

        cursor.execute("SELECT COUNT(*) FROM public.arcanoid_game")
        results = cursor.fetchall()
        id = str(results[0][0] + 1)

        cursor.execute("insert into public.arcanoid_game values('" + id + "', '" + login + "', '" + password + "')")
        connection.commit()
        return True

    else:
        sock.send("Такой логин уже существует, придумайте другой".encode('utf8'))
        return False


def database_connection():
    connection = psycopg2.connect(host="localhost", user="student", password="study", dbname="postgres")
    cursor = connection.cursor()
    print("Database connected")
    return connection


def create_socket():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 9090))
        sock.listen(100)
    except Exception:
        print("Неудалось создать сокет")

    print("Socket created")
    return sock

def chat(sock, name):
    sock.send(name + " присоеденился к чату".encode('utf8'))
    while True:
        message = sock.recv(1024)
        if len(message) > 0:
            sock.send(message)
            pass
