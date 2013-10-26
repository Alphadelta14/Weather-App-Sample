import SocketServer
import SimpleHTTPServer
import random
import json

PORT = 12080

weather_types = ["sunny", "cloudy", "rainy"]
temperatures = range(40, 85, 5)

def day_data():
    """ serve up single day data """
    hourly = {}
    for hour in range(8, 21, 4):
        hourly[hour] = {
            "weather": random.choice(weather_types),
            "temperature": random.choice(temperatures)
        }
    return json.dumps(hourly)

def week_data():
    """ serve up week data """
    week = {}
    for day in range(0, 7):
        week[day] = {
            "weather": random.choice(weather_types),
            "temperature": random.choice(temperatures)
        }
    return json.dumps(week)

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/day':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(day_data())
            return
        elif self.path == "/week":
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(week_data())
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
