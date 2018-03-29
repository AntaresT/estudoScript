import socket

target_host = "www.google.com" #Host Alvo
target_port = 80 #Porta do Host

#Criando um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Efetua a conexão com o alvo
client.connect((target_host, target_port))

#Envia alguns dados
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#Recebe alguns dados
response = client.recv(4096)

print response