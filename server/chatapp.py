from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gethostname
import threading
from configparser import ConfigParser
from threads import handle_client, CLIENTS
import threads
import logic
from typing import Dict, List

config:ConfigParser = ConfigParser()
config.read("config.ini")

HEADER:str = config.get("CHAT", "HEADER")
PORT:int = int(config.get("CHAT", "PORT"))
IP:str = config.get("CHAT", "IP")
FORMAT:str = config.get("CHAT", "FORMAT")

RUNNING:bool = False
server:socket = None

def close_server() -> None:
    global RUNNING, server
    RUNNING = False
    for val in CLIENTS.values():
        val.close()
        server.close()

def run_server(ip:str=None, port:int=None, format:str=None) -> None:
    global HEADER, PORT, IP, FORMAT, RUNNING
    threads.CLIENTS:Dict[str, socket] = {}
    logic.rooms: List[logic.Room] = []
    logic.LOBBY = logic.Room(room_id=0, room_name="LOBBY")
    logic.rooms.append(logic.LOBBY)
    if RUNNING:
        return
    RUNNING = True
    ip = IP if ip == None else ip
    port = PORT if port == None else port
    format = FORMAT if format == None else format
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, port))
    print("[STARTING] server is starting...")
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}")
    while RUNNING:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, int(HEADER), format))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 3}")
    print("SERVER IS SHUTTING DOWN")
    for thread in threading.enumerate():
        thread.join()
    quit()

if __name__ == "__main__":
    run_server()
