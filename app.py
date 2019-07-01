import SimpleHTTPServer
import SocketServer

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        print self.headers
        if 'Content-Length' in self.headers:
          print self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        with open("response.json", "r") as file:
          self.wfile.write(file.read())

httpd = SocketServer.TCPServer(("", 9090), Handler)

httpd.serve_forever()

