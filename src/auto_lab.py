import subprocess
import time
from datetime import datetime
from c2 import server, client
from detector import beacon_detector
from honeypot import tcp_honeypot

def main():
    print("[+] SentinelC2 Lab iniciado")
    print("[+] Lanzando servicios...")

    # Lanza C2 server
    server_proc = server.start_server()
    # Lanza C2 client
    client_proc = client.start_client()
    # Lanza honeypot
    honeypot_proc = tcp_honeypot.start_honeypot()

    # Simula laboratorio activo
    duration = 20
    print(f"[+] Laboratorio activo por {duration} segundos...")
    time.sleep(duration)

    print("[+] Deteniendo servicios...")
    server_proc.terminate()
    client_proc.terminate()
    honeypot_proc.terminate()

    print("[+] Ejecutando detección...")
    beacon_detector.detect_beacons()

    print("[+] Generando reporte final...")
    print_report()

def print_report():
    print("\n========== REPORTE SENTINELC2 ==========")
    print(f"Fecha: {datetime.now()}\n")
    print("--- C2 LOG ---")
    server.show_log()
    print("\n--- DETECCIONES ---")
    beacon_detector.show_log()
    print("\n--- HONEYPOT ---")
    tcp_honeypot.show_log()
    print("\n========== FIN DEL REPORTE ==========")

if __name__ == "__main__":
    main()
