# This is the template code for the CNE335 Final Project
# Justin Ellis
# CNE 335 Fall

from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Nwamaka Okalla")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    server = Server("54.68.76.21")

    # TODO - Call Ping method and print the results
    result = server.ping()  # Call the ping method
    print(result)  # Print the results
