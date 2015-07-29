

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
        return self.application(environ, response)