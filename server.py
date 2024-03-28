# 1. Написать простейший веб-сервер. Сервер должен принимать входящие соединения на порту 80 и 
# отдавать пользователю содержимое запрошенного ресурса из определенной директории (рабочей директории сервера).

# 2. Разместите в рабочей директории сервера простой веб сайт, содержащий страницу index.html. 
# Убедитесь, что при подключении к серверу, если не указан необходимый ресурс он отдает содержимое страницы index.html.
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Указываем порт, на котором будет работать сервер
port = 80

# Класс для обработки HTTP запросов
class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Определяем директорию, из которой будут отдаваться файлы
        root = 'C:/Users/HP/Downloads'
        return SimpleHTTPRequestHandler.translate_path(self, root + path)

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

try:
    # Создаем HTTP сервер
    server = HTTPServer(('localhost', port), MyHTTPRequestHandler)
    print(f"Сервер запущен на порту {port}")
    server.serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен")
    server.socket.close()



