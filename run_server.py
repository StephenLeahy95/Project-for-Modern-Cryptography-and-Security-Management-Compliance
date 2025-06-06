from logging import basicConfig, INFO, info
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from api.conf import PORT, EncryptionKey
from api.app import Application

def main():
    basicConfig(level=INFO)
    info(f" The Encryption Key: {EncryptionKey}")

    http_server = HTTPServer(Application())
    http_server.listen(PORT)

    info('Starting server on port ' + str(PORT) + '...')
    IOLoop.current().start()

if __name__ == '__main__':
    main()
