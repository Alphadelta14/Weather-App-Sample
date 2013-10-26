import SocketServer
import SimpleHTTPServer
import random

PORT = 12080

weather_types = ["sunny", "cloudy", "rainy"]
temperatures = range(40, 85, 5)

def data():
    """ serve up data """
    return 'test'

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/data':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(data())
            return
        elif "backend" in self.path:
            self.send_response(403)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("Forbidden")
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.ThreadingTCPServer(('localhost', PORT),CustomHandler)

print "serving at port", PORT
httpd.serve_forever()
