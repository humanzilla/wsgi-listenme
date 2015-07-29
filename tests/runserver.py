#!/usr/bin/env python
import wsgi
from wsgi_listenme import ListenMeMiddleware

application = ListenMeMiddleware(wsgi.application)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8000, application)
    print "Serving on port 8000..."
    httpd.serve_forever()