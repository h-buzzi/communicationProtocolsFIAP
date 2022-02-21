# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:04:32 2022

@author: hbuzzi
"""

from socket import *

servidor="127.0.0.1"
porta=43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM) #Define protocolo de comunicação e endereçamento
    obj_socket.connect((servidor, porta)) #Conecta com o servidor
    msg = bytes(input("Sua mensagem: "), 'utf-8') #Input da msg em Bytes
    obj_socket.send(msg) #Envio da msg
    resposta=obj_socket.recv(1024) #Recebe pacotes de 1024bytes
    print("Resposta do Servidor: ", str(resposta)[2:-1]) #List slicing para retirar o b'xxString das msgs recebidas
    if str(msg)[2:-1].upper()=="FIM": #Se digitar FIM termina a comunicação do lado do cliente
        break
obj_socket.close()