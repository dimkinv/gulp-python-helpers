import cherrypy
from cherrypy import wsgiserver
from pecan.deploy import deploy
from sys import argv

app = deploy(argv[1])

application = wsgiserver.WSGIPathInfoDispatcher({
    '/': app
})
port = int(argv[2])
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', port), application, server_name='testapp')

try:
    print('starting server at port {0}'.format(port))
    server.start()
except KeyboardInterrupt:
    print('stopping server!')
    server.stop()
