import Conections as con
import Auntification as auntf


def start():
    connection = con.database_connection()  # конект к базе данных
    sock = con.create_socket()  # создание сокета
    cursor = connection.cursor()

    print('Server started')
    menu(sock, connection, cursor)


def menu(sock, connection, cursor):
    sock, addr = sock.accept()
    print("Client connected with address " + addr[0])
    name = auntf.auntification_client(sock, connection, cursor)
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




