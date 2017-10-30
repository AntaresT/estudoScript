#Servidor TCP Multithreads Padrao

import socket
import threading

bind_ip = "192.168.1.102"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port)) #Ip e porta que ficara ouvindo

server.listen(5) #Comeca a ouvir com conexoes acumuladas passadas como parametro

print "[*] Listening on %s:%d " % (bind_ip,bind_port)

#Thread para tratamento de clientes
def handle_client(client_socket):

	#exibe o que o cliente enviar
	request = client_socket.recv(1024)

	print "[*] Recived: %s" % request

	#envia um pacote de volta
	client_socket.send("ACK")
	client_socket.close()

	while True:
		client,addr = server.accpet()
		print "[*] Accepted connection from %s:%d" % (addr[0],addr[1])

		#coloca nossa Thread de cliente em acao para tratar dados de entrada
		client_handler = threading.Thread(target=handle_client, args=(client,))
		client_handler.start()