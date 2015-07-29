# coding=utf-8

class ListenMeMiddleware(object):
    def __init__(self, application, publish=None, tags=None):
        """Initialize the middleware
        
        Args:
            application (object): The application instance
            publish (str, optional): Socket path or port where to publish all request and responses
            tags (list, optional): List of string tags to attach to all request and responses
        """
        self.application = application
        self.publish = publish
        self.tags = tags

    def __call__(self, environ, response):
        """Call the application and capture request and responses to later
        publish to `self.publish` address
        """
        response = self.application(environ, response)

        for event in response:
            yield event

    def capture_request(self):
        pass

    def capture_response(self):
        pass