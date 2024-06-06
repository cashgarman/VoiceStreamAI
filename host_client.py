import http.server
import ssl
import os
import logging

logging.basicConfig(level=logging.INFO)

# Change to the directory you want to serve
os.chdir('./api_client')

class SingleFileHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		logging.info(f"Request for {self.path}")
		if self.path == '/index.html' or self.path == '/':
			super().do_GET()
		else:
			self.send_error(404, "File not found.")

# Create a simple HTTP server
server_address = ('', 443)  # You can change the port as needed
httpd = http.server.HTTPServer(server_address, SingleFileHTTPRequestHandler)

# Specify the path to your SSL key and certificate
keyfile = '/home/cash/VoiceStreamAI/certs/privkey1.pem'
certfile = '/home/cash/VoiceStreamAI/certs/fullchain1.pem'

# Wrap the HTTP server with SSL
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=keyfile, certfile=certfile, server_side=True)

print(f"Serving on port {server_address[1]} with SSL...")
httpd.serve_forever()