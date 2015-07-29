wsgi-listenme documentation
===========================

WSGI middleware for capture and browse requests and responses


Install
-------


.. code-block:: shell

    pip install listenme


Usage
-----

In your wsgi.py file your WSGI application with our middleware.

.. code-block:: python

    from listenme import ListenMeMiddleware

    def application(environ, start_response):
        response_body = 'Hello Mundo!'
        status = '200 OK'
        response_headers = [
            ('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))
        ]
        start_response(status, response_headers)
        return [response_body]

    application = ListenMeMiddleware(application, publish="/tmp/listenme.socket")


Start your application and start:

.. code-block:: python

    listenme --listen /tmp/listenme.socket --http :8000

Open your browser at http://localhost:8000 and browse the requests and responses