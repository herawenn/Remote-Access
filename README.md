# Reverse Shell

![Image](https://i.imgur.com/x9r6DIW.png)

This Python script creates a reverse shell using an fake 'HWID spoofer'. It allows a remote connection to execute commands on the target machine, while also simulating the process of spoofing the Hardware ID (HWID) and MAC address. When the 'spoofing' is complete the target will be asked to press enter to continue. This is when the remote connection is established and the window is hidden.

## Features

-   **Reverse Shell:** Establishes a connection back to a specified IP address and port, allowing remote command execution.
-   **Simulated HWID Spoofing:** Simulates the process of changing the HWID and MAC address using a visual interface with `tqdm` progress bars and `pyfiglet` for stylized text.
-   **System Information Gathering:** Retrieves and displays user, PC name, OS version, and IP address.
-   **Hides Console Window:** Option to hide the console window on Windows.

## Requirements

-   Python 3.x
-   `colorama`: For colored terminal output.
-   `tqdm`: For progress bars.
-   `pyfiglet`: For ASCII art fonts.
-   `netcat`: For a listener to discover new connections
-   `pyinstaller`: For compiling the script to an executable

To install the required packages, run:

```bash
pip install -r requirements.txt
```

Installing Netcat

Debian/Ubuntu:
```bash
sudo apt update
sudo apt install netcat
```

Fedora/CentOS:
```bash
sudo dnf install netcat
```

macOS:
```bash
brew install netcat
```
*If you don't have brew, install it from: https://brew.sh/*

Verify the installation by running `nc -h`

### Compiling with PyInstaller

You can compile the Python script into an executable using PyInstaller. Follow these steps:

```bash
pyinstaller --onefile reverse.py
```

This will generate a standalone executable in the dist directory. You can then distribute this executable to run on machines without Python installed (this also obfuscates the scripts contents).

## Usage

1. Modify the TARGET_IP and TARGET_PORT variables in the script to match the IP address and port of your listening server.

TARGET_IP = '127.0.0.1'  # Replace with your listening IP
TARGET_PORT = 4444       # Replace with your listening port

2. Use netcat or a similar tool to listen on the specified port.
```bash
nc -lvnp 4444
```

3. Run the Script on the target machine:
```py
python reverse.py
```

Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer
This script is intended for educational and testing purposes only. Use it responsibly and only on systems you have permission to access. *The HWID spoofing part of the script is a simulation and does not actually change the HWID or MAC address of the system.*
