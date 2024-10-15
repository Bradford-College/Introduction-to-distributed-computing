'''
Install Pyro4 using:
    pip install pyro4 
'''

import Pyro4

@Pyro4.expose
class Calculator():
    def add(self, x, y):
        return x + y

# Server
daemon = Pyro4.Daemon(host="localhost", port=9090)  # Specify host and port
uri = daemon.register(Calculator)
print(f"Ready. Object URI = {uri}")
daemon.requestLoop()
