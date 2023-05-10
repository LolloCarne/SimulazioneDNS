import socketserver
import meteoAPI
class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data=self.request.recv(1024).decode()
        if not data or data != 'GET':
            self.finish()
        print(f'received:{data}')
        self.request.sendall(f"Meteo Modena: {str(meteoAPI.description)} \nTemp: {str(meteoAPI.temp)} \nTemp Min: {str(meteoAPI.temp_min)}\nTemp Max: {str(meteoAPI.temp_max)}".encode())


    def finish(self):
        self.request.close()

class Server(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass

server_address=('',3333)
server=Server(server_address,RequestHandler)
try:
    print(f'server started at port:{server_address[1]}')
    server.serve_forever()
except KeyboardInterrupt:
    print("bye...")
    server.server_close()