import socket
import pickle
from datetime import date
import time

HOST = '0.0.0.0'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

print("Server running at port: 5000")
while True:
    arr = []

    # requisição chegando no servidor
    clientTime, client = udp.recvfrom(1024)
    print("Requisição recebida")
    
    # definição dos timestamps
    ts2 = time.time() # ts2, tempo em que a requisição chega
    ts1 = pickle.loads(clientTime) # ts1, tempo em que a requisição saiu do cliente
    ts3 = time.time() # ts3, tempo em que a resposta sai do servidor 

    # preenchimento do array que será a resposta ao cliente
    arr.append(ts1)
    arr.append(ts2)
    arr.append(ts3)

    # serilização do array para enviar
    packet = pickle.dumps(arr)


    # envio da resposta
    udp.sendto(packet, client)
    print(pickle.loads(packet))

    arr = []
udp.close()
