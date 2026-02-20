from http.server import HTTPServer, BaseHTTPRequestHandler
 
class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self): 
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("Hello from Effective Mobile!".encode("utf-8"))

webServer = HTTPServer(("backend", 8080), MyHandler)
webServer.serve_forever()

