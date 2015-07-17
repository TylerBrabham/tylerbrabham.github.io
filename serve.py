# Code taken directly off of python website.

import SimpleHTTPServer
import SocketServer

PORT = 8003

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()