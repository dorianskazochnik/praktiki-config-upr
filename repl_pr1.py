import getpass
import socket
import string
import re

def runcommand(command, arr):
    print(command)
    if (arr != []):
        print(*arr, sep=' ')

name = getpass.getuser()
host = socket.gethostname()
command = ''
commandslist = ['ls', 'cd', 'exit']
while(command != 'exit'):
    print(name + '@' + host + ':~$ ', end='')
    s = input()
    s = re.sub(r'\s+', ' ', s).strip()
    arr = s.split(' ')
    command = arr[0]
    arr = arr[1:]
    if command in commandslist:
        runcommand(command, arr)
    else:
        print('\"' + command + '\"', end='')
        print('не является внутренней или внешней командой, исполняемой программой или пакетным файлом.')
