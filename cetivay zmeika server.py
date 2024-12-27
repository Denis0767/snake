import socket
import threading
import random
import time

# Задаем порт и хост
HOST = 'localhost'
PORT = 5555

# Создаем сокет
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Сервер запущен на {HOST}:{PORT}")

# Список подключенных клиентов
clients = []

def handle_client(conn, addr):
    # Генерируем случайные координаты для змейки
    snake_x = random.randint(1, 10)
    snake_y = random.randint(1, 10)

    while True:
        # Принимаем действия от клиента
        data = conn.recv(1024).decode()
        print(f"Получено от {addr}: {data}")

        # Обрабатываем действие клиента
        if data == 'UP':
            snake_y -= 1
        elif data == 'DOWN':
            snake_y += 1
        elif data == 'LEFT':
            snake_x -= 1
        elif data == 'RIGHT':
            snake_x += 1

        # Отправляем новые координаты змейки клиенту
        conn.send(f"{snake_x},{snake_y}".encode())

        time.sleep(0.1)

def start_server():
    while True:
        # Принимаем нового клиента
        conn, addr = server.accept()
        clients.append((conn, addr))
        print(f"Подключен клиент {addr}")

        # Запускаем обработчик клиента в отдельном потоке
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

start_server()