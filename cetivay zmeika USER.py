import socket

# Задаем хост и порт сервера
HOST = 'localhost'
PORT = 5555

# Создаем сокет
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    # Отправляем управляющие действия серверу
    action = input("Введите действие (UP, DOWN, LEFT, RIGHT): ")
    client.send(action.encode())

    # Получаем координаты змейки от сервера
    snake_pos = client.recv(1024).decode()
    print(f"Координаты змейки: {snake_pos}")
