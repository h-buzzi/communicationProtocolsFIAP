# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 10:40:25 2022

@author: hbuzzi
"""

from socket import *
servidor="127.0.0.1"
porta=43210
obj_socket = socket(AF_INET, SOCK_DGRAM) #UDP
obj_socket.bind((servidor,porta)) #Conecta/víncula
print("Servidor pronto....")
while True:
    #Não utiliza liste pois UDP não tem a confiabilidade do TCP
    dados, origem = obj_socket.recvfrom(65535) #Tamanho máximo
    #não existe con.recv, pois não possui ligação com objeto de conexão
    print("Origem..........: ", origem)
    print("Dados recebidos.: ", dados.decode()) #Utiliza-se a função decode no lugar de list slicing + conversão pra bytes
    resposta=input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem) #Encode serve pra codificar String para byte, utiliza tb a origem pra enviar de volta a resposta
obj_socket.close()