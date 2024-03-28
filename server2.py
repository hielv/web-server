from http.server import SimpleHTTPRequestHandler, HTTPServer

# Указываем рабочую директорию сервера
directory = 'C:/Users/HP/OneDrive - НИУ Высшая школа экономики/Рабочий стол/web-server/index.html/'

# Создаем класс-обработчик запросов, наследуясь от SimpleHTTPRequestHandler
class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=directory, **kwargs)

# Запускаем сервер на порту 80
server_address = ('', 80)
httpd = HTTPServer(server_address, MyHandler)
print('Сервер запущен...')
httpd.serve_forever()
