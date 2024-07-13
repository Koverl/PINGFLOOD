import os
import ping3
import time
from colorama import init, Fore, Back, Style

init()

os.system('cls')

print(Fore.RED + """### ##     ####   ###  ##   ## ##            ### ###  ####      ## ##    ## ##   ### ##   
 ##  ##     ##      ## ##  ##   ##            ##  ##   ##      ##   ##  ##   ##   ##  ##  
 ##  ##     ##     # ## #  ##                 ##       ##      ##   ##  ##   ##   ##  ##  
 ##  ##     ##     ## ##   ##  ###            ## ##    ##      ##   ##  ##   ##   ##  ##  
 ## ##      ##     ##  ##  ##   ##            ##       ##      ##   ##  ##   ##   ##  ##  
 ##         ##     ##  ##  ##   ##            ##       ##  ##  ##   ##  ##   ##   ##  ##  
####       ####   ###  ##   ## ##            ####     ### ###   ## ##    ## ##   ### ##   
                                                                                          
""")

print ("made by koverl_3x, korrality, koverty or github/koverl ")


def ping_host(host, interval=1):
    try:
        while True:
            response = ping3.ping(host)
            if response is not None:
                print(f"Ping to {host} successful. Round-trip time: {response} ms")
            else:
                print(f"Ping to {host} failed.")
            
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nstopped ping")


host_to_ping = input("Enter the IP address or hostname you want to ping: ")


interval = float(input("Enter the interval between pings: "))

ping_host(host_to_ping, interval)
