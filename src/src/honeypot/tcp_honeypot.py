import multiprocessing
import socket
import time

log = []

def start_honeypot():
    proc = multiprocessing.Process(target=run_honeypot)
    proc.start()
    return proc

def run_honeypot():
    s = socket.socket()
    s.bind(("127.0.0.1", 8888))
    s.listen(5)
    while True:
        client, addr = s.accept()
        log.append(f"Connection from {addr[0]}")
        client.close()

def show_log():
    if log:
        for entry in log:
            print(entry)
    else:
        print("No data")
