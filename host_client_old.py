import http.server
import ssl
import os

# Change to the directory you want to serve
os.chdir('./client')

# Create a simple HTTP server
server_address = ('', 443)  # You can change the port as needed
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Specify the path to your SSL key and certificate
keyfile = '/home/cash/VoiceStreamAI/certs/privkey1.pem'
certfile = '/home/cash/VoiceStreamAI/certs/fullchain1.pem'

# Wrap the HTTP server with SSL
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=keyfile, certfile=certfile, server_side=True)

print(f"Serving on port {server_address[1]} with SSL...")
httpd.serve_forever()
