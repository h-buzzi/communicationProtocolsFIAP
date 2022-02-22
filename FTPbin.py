# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:52:29 2022

@author: hbuzzi
"""

from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
ftp.cwd('/pub/linux/logos/pictures') #Change Working Directory
with open ('pai_do_linux.jpg', 'wb') as arq: #nome do arquivo que será escrito como binário
    ftp.retrbinary('RETR linus-father-of-linux.jpg', arq.write) #Retrieve e esquece no arq
ftp.quit()