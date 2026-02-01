import subprocess
import time
import multiprocessing

log = []

def start_server():
    proc = multiprocessing.Process(target=run_server)
    proc.start()
    return proc

def run_server():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 9999))
    s.listen(1)
    while True:
        client, addr = s.accept()
        log.append(f"{time.time()}|{addr[0]}|heartbeat")
        client.send(b"heartbeat")
        client.close()

def show_log():
    for entry in log:
        print(entry)
