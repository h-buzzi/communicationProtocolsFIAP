# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:54:08 2022

@author: hbuzzi
"""

import os
from ftplib import *

ftp_ativo=False #FTP passivo
ftp = FTP(input("Digite o FTP que se deseja conectar: "))
#Digite o url do FTP, tal como ftp.ibiblio.org
print(ftp.getwelcome()) #Msg de boas-vindas do ftp
usuario=input("Digite o usuario: ") #Login
senha=input("Digite a senha: ") #Senha
#Caso não coloque nada como usuario e senha, entrará como anônimo
ftp.login(usuario, senha) #Login no ftp

print("Conexão bem sucedida. Diretório atual de trabalho: ", ftp.pwd(),"") #Printa o diretório atual

menu="1" #Variável de opção do menu
while menu=="1" or menu=="2" or menu=="3":
    menu=input("Escolha a opção desejada: "
               "<1> - para Listar arquivos"
               "<2> - para definir um diretório"
               "<3> - para baixar um arquivo: ") #Listagem de opções printadas na tela
    if menu=="1":
        print(ftp.dir()) #Lista os arquivos do diretório
    elif menu=="2":
        ftp.cwd(input("Digite o diretório que deseja entrar: ")) #Change Working Directory para o diretório informado, exemplo: /pub/linux/logos/pictures
        print("Diretório corrente é: ", ftp.pwd()) #Printa o diretório atual após mudar
    elif menu=="3":
        tipo=input("Digite <B> para arquivo binário ou "
                   "qualquer outra letra para arquivo ASCII: ").upper() #Pega que tipo de arquivo o usuário quer baixar
        if tipo=="B":
            with open(input("Digite o nome do arquivo destino: "), 'wb') as arq: #Se for binário, ele informa o nome do arquivo que deseja CRIAR na máquina
                ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write) #Retrieve do arquivo de ORIGEM, arquivo que está no FTP, e escreve no arquivo criado
        else: #CASO SELECIONE PADRÃO ASCII (texto)
            with open(input("Digite o nome do arquivo destino: "), 'w') as arq: #Nome do arquivo que será criado
                def escreverLinha(data): #Função que escreve o texto no arquivo e faz quebra de linha
                    arq.write(data)
                    arq.write(os.linesep) #Qubra de linha
                ftp.retrlines('RETR ' + input("Arquivo de origem:"), escreverLinha) #Retrievelines onde coloca o nome do arquivo de ORIGEM, arquivo que está no FTP, e usa a função escrever linha acima
        print("Arquivo baixado com sucesso!")
ftp.quit()