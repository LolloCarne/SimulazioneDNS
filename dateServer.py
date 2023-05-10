import socketserver, datetime

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data=self.request.recv(1024).decode()
        if not data or data != 'GET':
            self.finish()
        self.request.sendall(str(datetime.datetime.now()).encode())

    def finish(self):
        self.request.close()

class Server(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass

server_address=('',1111)
server=Server(server_address,RequestHandler)
try:
    print(f'server started at port:{server_address[1]}')
    server.serve_forever()
except KeyboardInterrupt:
    print("bye...")
    server.server_close()