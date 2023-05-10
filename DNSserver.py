import socketserver
import json

class RequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        with open("DNS.json") as f:
            ddns=json.load(f)
        print(ddns)
        data=self.request.recv(1024).decode()
        if not data:
            self.finish()
        print(f'received:{data}')
        if data in ddns.keys():
            self.request.sendall(str(ddns[data]).encode())
        else:
            self.request.sendall("0".encode())

    def finish(self):
        self.request.close()

class Server(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass

server_address=('',8888)
server=Server(server_address,RequestHandler)
try:
    print(f'server started at port:{server_address[1]}')
    server.serve_forever()
except KeyboardInterrupt:
    print("bye...")
    server.server_close()