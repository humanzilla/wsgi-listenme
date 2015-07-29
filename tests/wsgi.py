
def application(environment, start_response):
      data = "Hello Mundo!\n"
      start_response("200 OK", [
          ("Content-Type", "text/plain"),
          ("Content-Length", str(len(data)))
      ])
      return iter([data])