import socket
import threading

class ChatClient:
    def __init__(self, host='127.0.0.1', port=5555):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname = None
    
    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("An error occurred!")
                self.client.close()
                break
    
    def write(self):
        while True:
            message = f'{self.nickname}: {input("")}'
            self.client.send(message.encode('ascii'))

    def start(self):
        self.nickname = input("Choose your nickname: ")
        
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        
        write_thread = threading.Thread(target=self.write)
        write_thread.start()

if __name__ == "__main__":
    client = ChatClient()
    client.start()