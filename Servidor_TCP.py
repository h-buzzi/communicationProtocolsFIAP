# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 09:59:10 2022

@author: hbuzzi
"""

from socket import *
servidor="127.0.0.1"
porta=43210
obj_socket = socket(AF_INET, SOCK_STREAM)
#AF_INET -> Parâmetro de identificação de origem/destino, este é utilizado para IP/DNS.
#SOCK_STREAM -> Protocolo de comunicação, neste caso é TCP, poderia usar SOCK_DGRAM para UDP
obj_socket.bind((servidor,porta)) #Conecta/víncula
obj_socket.listen(2) #Define o máximo de clientes que irá atender simultaneamente
print("Aguardando cliente....")
while True:
    con, cliente = obj_socket.accept() #Objeto de conexão e cliente
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024)) #Msg recebida acessada por meio do objeto de conexão
        print("Recebemos: ", str(msg_recebida)[2:-1]) #List slicing para retirar o b'xxString das msgs recebidas
        msg_enviada = bytes(input("Sua resposta: "), 'utf-8') #Recebe utf-8 do input e traduz pra byte
        con.send(msg_enviada) #Pega o objeto de conexão e utiliza para enviar a msg
        break
    con.close()