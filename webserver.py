# A basic webserver

import http.server
import socketserver


def run():
	PORT = 8080
	Handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(("", PORT), Handler)
	print("serving at port", PORT)
	httpd.serve_forever()
	f = input("press enter")
	httpd.shutdown()
run()

