from tornado import ioloop, gen, iostream
from tornado.tcpserver import TCPServer


class MyTcpServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        try:
            while True:
                msg = yield stream.read_bytes(20, partial=True)
                print(msg, 'from', address)
                # stream.write(str(msg).encode("utf8"))
                stream.write(str(msg[::-1]).encode("utf8"))
                print("ok")
                if msg == 'over':
                    stream.close()
        except iostream.StreamClosedError:
            pass


if __name__ == '__main__':
    server = MyTcpServer()
    server.listen(8036)
    server.start()
    ioloop.IOLoop.current().start()
