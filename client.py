import socket
import pickle
from datetime import date
import time

HOST = '192.168.43.233'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

# captação do ts1, horario do cliente
ts1 = time.time()

# serialização do pacote a ser enviado
msg = pickle.dumps(ts1)

# envio do pacote através do socket
udp.sendto(msg, dest)

# reposta do servidor sendo recebida
reply = udp.recv(4096)
ts4 = time.time()

# serialização inversa dos dados recebidos do servidor
response = pickle.loads(reply)

ts1 = response[0]
ts2 = response[1]
ts3 = response[2]

ttl = ((ts4 - ts1) - (ts3 - ts2)) / 2
print("TTL: " + str(ttl))
udp.close()

















# "alecio_filho@hotmail.com", "pedrosancotrim@outlook.com", "b.soaresgusmao@gmail.com"


