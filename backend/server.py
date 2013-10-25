import SocketServer
import SimpleHTTPServer

PORT = 12080

def index():
    """ serve up index data """
    return 'test'

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/data':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(index())
            return
        elif "backend" in self.path:
            self.send_response(403)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Forbidden")
        else:
            super(CustomHandler, self).do_GET()

httpd = SocketServer.ThreadingTCPServer(('localhost', PORT),CustomHandler)

print "serving at port", PORT
httpd.serve_forever()
