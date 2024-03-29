from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import mimetypes
from datetime import datetime

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Date', datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT'))
        self.send_header('Content-type', 'text/html')
        self.send_header('Server', 'CustomServer')
        
        if self.path.endswith('.html') or self.path.endswith('.css') or self.path.endswith('.js'):
            file_path = os.path.join(directory, self.path.lstrip('/'))
            if os.path.exists(file_path):
                content_length = os.path.getsize(file_path)
                self.send_header('Content-length', str(content_length))
                with open(file_path, 'rb') as file:
                    self.wfile.write(file.read())
            else:
                self.send_error(404)
        else:
            self.send_error(403)

    def log_message(self, format, *args):
        log_entry = '{} - {} - {}'.format(datetime.now(), self.client_address[0], self.path)
        print(log_entry)

# Указываем рабочую директорию сервера
directory = 'C:/Users/HP/OneDrive - НИУ Высшая школа экономики/Рабочий стол/web-server/index.html/'

# Создаем класс-обработчик запросов, наследуясь от SimpleHTTPRequestHandler
class MyHandler(SimpleHTTPRequestHandler):
    def init(self, *args, **kwargs):
        super().init(*args, directory=directory, **kwargs)

# Запускаем сервер на порту 80
server_address = ('', 80)
httpd = HTTPServer(server_address, MyHandler)
print('Сервер запущен...')
httpd.serve_forever()
