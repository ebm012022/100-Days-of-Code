import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

HOSTNAME = "localhost"
PORT = 8080
Handler = http.server.BaseHTTPRequestHandler

class MyServer(Handler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        url = self.path
        parsed_url = urlparse(url)
        captured_value = parse_qs(parsed_url.query)['given'][0]
        self.wfile.write(bytes("<html>" + str(captured_value[::-1]) + "<html/>", "utf-8"))
        return
    def serve_forever(port):
        socketserver.TCPServer(('', port), MyServer).serve_forever()

print("serving at port", PORT)
MyServer.serve_forever(PORT)
    
