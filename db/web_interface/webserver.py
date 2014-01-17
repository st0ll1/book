'''
Веб сервер
В текущем каталоге должны быть подкаталоги
cgi-bin и ntbin
'''
import os,  sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'            # Файлы  html и подкаталог cgi-bin
port = 80               # Порт

os.chdir(webdir)    # перейти в каталог HTML
srvaddr = ('', port)   # имя хоста и порт
srvrobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()     # Запустить как бесконечный фоновый процесс   
