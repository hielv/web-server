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
        self.send_response(200)  # Отправляем код состояния 200 (OK)
        self.send_header('Content-type', 'text/html')  # Указываем тип содержимого
        self.end_headers()
        
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_HEAD(self):
        self.send_response(200)  # Отправляем код состояния 200 (OK)
        self.send_header('Content-type', 'text/html')  # Указываем тип содержимого
        self.end_headers()

try:
    # Создаем HTTP сервер
    server = HTTPServer(('localhost', port), MyHTTPRequestHandler)
    print(f"Сервер запущен на порту {port}")
    server.serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен")
    server.socket.close()
