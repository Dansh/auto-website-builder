import socket
import time


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 80     # Port to listen on (non-privileged ports are > 1023)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create TCP socket
    s.bind((HOST, PORT)) # bind the socket with the IP and the port
    s.listen() # open the socket for client connections
    sumElement = ""

    while True:
        print("waiting for clients...")
        client, address = s.accept()
        data = client.recv(1024).decode()
        print(data)
        if data.split("\r\n\r\n")[1] != "":
            infoForPost = data.split("\r\n\r\n")[1]
            post = {}         
            for info in infoForPost.split("&"):
                post[info.split("=")[0]] = info.split("=")[1]
            print("\nPost -----------------------> " + str(post) + "\n")
            sumElement = "<h1>Sum = " + str((int(post["num1"]) + int(post["num2"]))) + "</h1><br>"
        data = """<html>
    <body>

    <h2>HTML Forms</h2>

    <form action="/" method="post">
    <input type="text" id="num1" name="num1">                        
    <input type="text" id="num2" name="num2"><br>"""+ sumElement + """
    <input type="submit" value="Submit">
    </form> 
    </body>
    </html>"""
        header = """HTTP/1.1 200 OK
    Content-Length: """ + str(len(data))+"""
    Content-Type: text/html
    Connection: Closed\r\n\r\n"""
        response = header+data
        client.send(response.encode())
        client.close()
main()