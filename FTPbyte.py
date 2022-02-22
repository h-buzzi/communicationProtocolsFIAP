# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:50:03 2022

@author: hbuzzi
"""

import os
from ftplib import *

def escreverLinha(data):
    arq.write(data)#Escreve a informação
    arq.write(os.linesep)#Separador de linha
    
ftp_ativo=False #FTP passivo
ftp = FTP('ftp.ibiblio.org') #Endereço FTP para criar o FTP
print(ftp.getwelcome()) #Printa msg de boas-vindas
ftp.login() #Faz o login anônimo
arquivo='LEIAME' #Nome do arquivo que será criado
ftp.set_pasv(ftp_ativo) #Seta a comunicação como FTP passivo
with open (arquivo, 'w') as arq: #Escrita arquivo
    ftp.retrlines('RETR README', escreverLinha) #Retrieve README, passa a função para escrever no arquivo
ftp.quit() #Fecha a conexão