import json
import socketserver
import datetime

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data=self.request.recv(1024).decode()
        if not data or data != 'GET':
            self.finish()
        print(f'received:{data}')
        with open("orari.json") as f:
            data=json.load(f)
        key=str(datetime.datetime.today().weekday()+1)
        self.request.sendall(f"{data[key][0]}: {data[key][1]}".encode())


    def finish(self):
        self.request.close()

class Server(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass

server_address=('',2222)
server=Server(server_address,RequestHandler)
try:
    print(f'server started at port:{server_address[1]}')
    server.serve_forever()
except KeyboardInterrupt:
    print("bye...")
    server.server_close()