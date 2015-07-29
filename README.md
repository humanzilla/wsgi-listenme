wsgi-listenme documentation
===========================

.. image:: https://api.travis-ci.org/humanzilla/wsgi-listenme.png
   :target: https://travis-ci.org/humanzilla/wsgi-listenme

.. image:: https://pypip.in/v/wsgi-listenme/badge.png
   :target: https://crate.io/packages/wsgi-listenme/


WSGI middleware for capture and browse requests and responses

.. contents::


Install
-------


.. code-block:: shell

    pip install wsgi-listenme


Usage
-----

In your wsgi.py file your WSGI application with our middleware.

.. code-block:: python

    from wsgi_listenme import ListenMeMiddleware

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

.. code-block:: shell

    listenme --listen /tmp/listenme.socket --http :8000

Open your browser at http://localhost:8000 and browse the requests and responses


License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_.

Please refer to the `license file <https://github.com/humanzilla/wsgi-listenme/blob/master/LICENSE.txt>`_.


© 2015 Mario César Señoranis Ayala