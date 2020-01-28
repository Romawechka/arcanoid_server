import Start

if __name__ == "__main__":
    while True:
        command = input("Введите команду\n").upper()
        if command == 'START':
            Start.start()
        elif command == 'EXIT':
            print("Досвидания")
            exit(0)
        elif command == 'HELP':
            print("Start\nExit")
        else:
            print("Такой команды не существует, вы можете увидеть список команд, написав \"help\".")