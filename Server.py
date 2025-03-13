import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        # response = os.system(f"ping -c 4 {self.server_ip}")  # Linux/macOS
        response = os.system(f"ping -n 4 {self.server_ip}")  # For Windows

        if response == 0:
            return f"Server {self.server_ip} is reachable."
        else:
            return f"Server {self.server_ip} is not reachable."
