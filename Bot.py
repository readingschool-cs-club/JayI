from JayI import JayI
from base64 import urlsafe_b64encode as b64encode

class Bot(object):
    def __init__(self):
        self.instances = {}

    def respond(self, username, data):
        return self.get(username).respond(data)

    def get(self, username):
        if username in self.instances:
            return self.instances[username]
        else:
            self.instances[username] = self.new_instance(username)
            return self.get(username)

    def new_instance(self, username):
        filename = b64encode(username.encode("utf-8")).decode("utf-8") + ".csv"
        return JayI(filename=filename)

if __name__ == "__main__":
    print(r"""

  +-------------------------+
  |  DO NOT RUN THIS FILE!  |
  +-------------------------+
  
  This is an abstract class for
  use in a specific implementation!

    """)
