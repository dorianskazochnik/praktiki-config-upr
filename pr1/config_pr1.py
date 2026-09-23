import getpass
import socket
import string
import re

def run_script(current_location, script_path, file_system):
    name = getpass.getuser()
    host = socket.gethostname()
    s = ''
    commandslist = ['ls', 'cd', 'mkdir', 'pwd', 'touch', 'cat', 'rm']
    while(s != 'exit'):
        print(name + '@' + host + ':~$ ', end='')
        s = input()
        s = re.sub(r'\s+', ' ', s).strip()
        arr = s.split(' ')
        command = arr[0]
        argument = arr[1] if len(arr) > 1 else None
        match (command, argument):
            case ("ls", None):
                print(*file_system[current_location], sep=' ')
            case ("ls", path):
                if path in file_system:
                    print(*file_system[path], sep=' ')
            case ("cd", None):
                print(current_location)
            case ("cd", path):
                if path in file_system:
                    current_location = path
                    print(current_location)
            case ("mkdir", name_loc):
                file_system[current_location].append(name_loc)
                file_system[name_loc] = []
            case ("pwd", None):
                print(current_location)
            case ("touch", name_file):
                file_system[current_location].append(name_file)
            case ("cat", name_file):
                if name_file in file_system[current_location]:
                    print('file is empty')
                else:
                    print('file does not exist')
            case ("rm", name_file):
                if name_file in file_system[current_location]:
                    file_system[current_location].remove(name_file)
                else:
                    print('file does not exist')

file_system = {}
file_system[''] = []
run_script('', '', file_system)