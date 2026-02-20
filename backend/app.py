from http.server import HTTPServer, BaseHTTPRequestHandler
 
class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("Hello from Effective Mobile!".encode("utf-8"))
 
hostName = "backend"
serverPort = 8080
 
webServer = HTTPServer((hostName, serverPort), MyHandler)
print(f"Сервер запущен: http://{hostName}:{serverPort}")
 


try:
    webServer.serve_forever()
except KeyboardInterrupt:
    print("Работа сервера прервана")
             
    webServer.server_close()
    print("Сервер остановлен...")

