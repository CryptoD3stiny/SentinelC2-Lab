import subprocess
import time
import multiprocessing

def start_client():
    proc = multiprocessing.Process(target=run_client)
    proc.start()
    return proc

def run_client():
    import socket
    while True:
        try:
            s = socket.socket()
            s.connect(("127.0.0.1", 9999))
            s.recv(1024)
            s.close()
        except:
            pass
        time.sleep(5)
