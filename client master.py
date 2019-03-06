try:
    import socket
    import threading
    import time
except:
    print('library not found ')


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def process_data_from_server(x):        # Define function to split Incoming Data
    x1, y1 = x.split(",")
    return x1, y1


def my_client():

    # Define Threadding to run after every 11 seconds
    # dont send Request to often or you will crash server

    threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:        # define socket TCP
        s.connect((HOST, PORT))

        # my = input("Enter command ")
        my_inp = 'Data'

        # encode the message
        my_inp = my.enc ode('utf-8')

        # send request ti server
        s.sendall(my_inp)

        # Get the Data from Server and process the Data
        data = s.recv(1024).decode('utf-8')

        # Process the data i mean split comma seperated value
        x_temperature,y_humidity = process_data_from_server(data)

        print("Temperature {}".format(x_temperature))
        print("Humidity {}".format(y_humidity))

        s.close()
        time.sleep(5)


if __name__ == "__main__":
    while 1:
        my_client()