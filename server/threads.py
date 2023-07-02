from logic import login_client, logout_client, list_rooms, list_users_in_room, enter_room, whereami, create_room, exit_room, get_all_client_ids_in_room
from socket import socket
from typing import List, Dict

CLIENTS:Dict[str, socket] = {}
RUNNING:bool = True

def client_count() -> None:
    return len(CLIENTS)

def handle_client(conn:socket, addr:int, HEADER:int, FORMAT:str) -> None:
    global CLIENTS
    CLIENTS[str(addr)] = conn
    # print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        msg_length:str = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg:str = conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] {msg}")
            match str(msg).split():
                case [":login", *arg]:
                    if len(arg) != 1:
                        # invalid command
                        conn.send("[-] Invalid command, for help please use ':help' command.".encode(FORMAT))
                    else:
                        # :login arg
                        if login_client(client_id=addr, client_name=arg[0]):
                            conn.send("[+] You have successfully logged in, directing to lobby...".encode(FORMAT))
                        else:
                            conn.send("[-] You are already logged in!".encode(FORMAT))
                case [":logout"]:
                    # :logout
                    if logout_client(client_id=addr):
                        CLIENTS.pop(str(addr))
                        conn.send("[+] You have successfully logged out, closing app...".encode(FORMAT))
                        break
                    else:
                        conn.send("[-] You are not logged in!".encode(FORMAT))
                case [":list_users"]:
                        # :list_users
                        users:str = list_users_in_room(client_id=addr)
                        if users:
                            conn.send(users.encode(FORMAT))
                        else:
                            conn.send("[-] There are no users online!".encode(FORMAT))
                case [":list_rooms"]:
                        # :list_rooms
                        rooms:str = list_rooms()
                        if rooms:
                            conn.send(rooms.encode(FORMAT))
                        else:
                            conn.send("[-] You are not in a room!".encode(FORMAT))
                case [":enter", *arg]:
                    if len(arg) != 1:
                        # invalid command
                        conn.send("[-] Invalid command, for help please use ':help' command.".encode(FORMAT))
                    else:
                        # :enter arg
                        status:int = enter_room(client_id=addr, room_name=arg[0])
                        if status == 1:
                            conn.send(f"[+] You have successfully entered room '{arg[0]}'".encode(FORMAT))
                        elif status == -1:
                            conn.send("[-] Invalid room name!".encode(FORMAT))
                        elif status == -2:
                            conn.send("[-] You are not logged in!".encode(FORMAT))
                        else:
                            conn.send("[-] Something unexpected happened, please contact admin!".encode(FORMAT))
                case [":whereami"]:
                    # :whereami
                    room_name:str = whereami(client_id=addr)
                    if room_name:
                        conn.send(f"[+] You are in room '{room_name}'".encode(FORMAT))
                    else:
                        conn.send("[-] You are not in a room.".encode(FORMAT))
                case [":open", *arg]:
                    if len(arg) != 1:
                        # invalid command
                        conn.send("[-] Invalid command, for help please use ':help' command.".encode(FORMAT))
                    else:
                        # :open arg
                        status:int = create_room(client_id=addr, room_name=arg[0])
                        if status == 1:
                            conn.send(f"[+] You have successfully created room '{arg[0]}', redirecting you to new room.".encode(FORMAT))
                        elif status == -1:
                            conn.send("[-] This room name is taken!".encode(FORMAT))
                        elif status == -2:
                            conn.send("[-] You are not logged in!".encode(FORMAT))
                        else:
                            conn.send("[-] Something unexpected happened, please contact admin!".encode(FORMAT))
                case [":close"]:
                    # :close
                    status:List[int] = exit_room(client_id=addr)
                    if not status:
                        conn.send("[-] You are not logged in!".encode(FORMAT))
                    else:
                        for socket_id in status:
                            if str(socket_id) in CLIENTS.keys():
                                    CLIENTS[str(socket_id)].sendall("[:] Room is closing, you are being redirected to LOBBY...".encode(FORMAT))
                case [":help"]:
                    # :help
                    conn.send("Command             ----->  Affect\n:login <user_name>  ----->  login as <user_name>\n:logout             ----->  logout\n:list_rooms         ----->  list all rooms that are open\n:list_users         ----->  list all users in the room you are in\n:enter <room_name>  ----->  enter room <room_name>\n:whereami           ----->  see what room you are in\n:open <room_name>   ----->  create room <room_name>\n:close <room_name>  ----->  exit room <room_name>\n:help               ----->  see all commands".encode(FORMAT))
                case _:
                    # msg is not a command
                    if str(msg).startswith(":"):
                        conn.send("[-] Invalid command, for help please use ':help' command.".encode(FORMAT))
                    else:
                        socket_ids:List[int] = get_all_client_ids_in_room(addr)
                        if not socket_ids:
                            conn.send("[-] You are not logged in!".encode(FORMAT))
                        else:
                            for socket_id in socket_ids:
                                if str(socket_id) in CLIENTS.keys():
                                    CLIENTS[str(socket_id)].sendall(msg.encode(FORMAT))
    conn.close()
