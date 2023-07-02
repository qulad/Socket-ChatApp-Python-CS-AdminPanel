from typing import List, Dict

class Client:
    def __init__(self, client_id:int, client_name:str, room_id:int):
        self.client_id:int = client_id
        self.client_name:str = client_name
        self.room_id:int = room_id

    def to_dict(self) -> Dict[str, str]:
        client_dict:Dict[str, str] = {
            "client_id": str(self.client_id),
            "client_name": str(self.client_name),
            "room_id": str(self.room_id)
        }
        return client_dict

class Room:
    def __init__(self, room_id:int, room_name:str, owner:Client=None, clients:List[Client]=[]) -> None:
        self.room_id:int = room_id
        self.room_name:str = room_name
        self.owner:Client = owner
        self.clients:List[Client] = clients

    def add_client(self, client_id:int, client_name:str) -> None:
        client = Client(client_id=client_id, client_name=client_name, room_id=self.room_id)
        self.clients.append(client)
    
    def check_client_in_room(self, client_id:int) -> bool:
        for client in self.clients:
            if client_id == client.client_id:
                return True
        return False
    
    def remove_client(self, client_id:int) -> None:
        for client in self.clients:
            if client_id == client.client_id:
                self.clients.remove(client)
    
    def get_all_client_name(self) -> List[str]:
        client_list:List[Client] = []
        for client in self.clients:
            print(client, client.client_name)
            client_list.append(client.client_name)
        return client_list
    
    def get_client_name(self, client_id:int) -> str:
        for client in self.clients:
            if client_id == client.client_id:
                return client.client_name
        return ""
    
    def get_all_client_id(self) -> List[int]:
        client_ids:List[int] = []
        for client in self.clients:
            client_ids.append(client.client_id)
        return client_ids
    
    def to_dict(self):
        clients_dict:Dict[str, Dict[str, str]] = {}
        for i in range(len(self.clients)):
            clients_dict[str(i)] = {"client": self.clients[i].to_dict()}

        room_dict:Dict[str, str] = {
            "room_id": str(self.room_id),
            "room_name": str(self.room_name),
            "owner": "" if self.owner == None else self.owner.to_dict(),
            "clients": clients_dict
        }
        return room_dict

rooms: List[Room] = []

LOBBY = Room(room_id=0, room_name="LOBBY")
rooms.append(LOBBY)

def login_client(client_id:int , client_name:str) -> bool:
    global rooms
    global LOBBY
    for room in rooms:
        if room.check_client_in_room(client_id=client_id):
            return False
    LOBBY.add_client(client_id=client_id, client_name=client_name)
    return True

def logout_client(client_id:int) -> bool:
    global rooms
    for room in rooms:
        if room.check_client_in_room(client_id=client_id):
            room.remove_client(client_id=client_id)
            return True
    return False

def list_rooms() -> str:
    global rooms
    room_str:str = ""
    for room in rooms:
        room_str += ";" if room_str != "" else ""
        room_str += f"{room.room_name},{len(room.clients)}"
    return room_str

def list_users_in_room(client_id:int) -> str:
    global rooms
    client_str:str = ""
    for room in rooms:
        if room.check_client_in_room(client_id=client_id):
            print(room.get_all_client_name())
            client_str = ";".join(room.get_all_client_name())
            break
    return client_str

def enter_room(client_id:int, room_name:str) -> int:
    global rooms
    target_room:Room = None
    for room in rooms:
        if room_name == room.room_name:
            target_room = room
            break
    if target_room == None:
        return -1 # Target room cannot be found
    client_name:str = ""
    for room in rooms:
        if room.check_client_in_room(client_id=client_id):
            client_name = room.get_client_name(client_id=client_id)
            room.remove_client(client_id=client_id)
            break
    if client_name == "":
        return -2 # Client is not logged in
    target_room.add_client(client_id=client_id, client_name=client_name)
    return 1

def whereami(client_id:int) -> str:
    global rooms
    room_name:str = ""
    for room in rooms:
        if room.check_client_in_room(client_id=client_id):
            room_name = room.room_name
    return room_name

def create_room(client_id:int, room_name:str) -> int:
    global rooms
    for room in rooms:
        if room_name == room.room_name:
            return -1 # Room name taken
    client_name:str = ""
    for room in rooms:
        if room.check_client_in_room(client_id=client_id):
            client_name = room.get_client_name(client_id=client_id)
            room.remove_client(client_id=client_id)
            break
    if not client_name:
        return -2 # Client is not logged in
    owner:Client = Client(client_id=client_id, client_name=client_name, room_id=len(rooms))
    new_room:Room = Room(len(rooms), room_name=room_name, owner=owner, clients=[owner])
    rooms.append(new_room)
    return 1

def exit_room(client_id:int) -> List[int]:
    global rooms
    logged_in:bool = False
    room_to_exit:Room = None
    for room in rooms:
        if room.check_client_in_room(client_id=client_id):
            room_to_exit = room
            logged_in = True
            break
    if not logged_in:
        return []
    clients:List[int] = []
    if client_id == room_to_exit.owner.client_id:
        for client in room_to_exit.clients:
            client_name:str = room_to_exit.get_client_name(client_id=client.client_id)
            room_to_exit.remove_client(client_id=client.client_id)
            clients.append(client.client_id)
            LOBBY.add_client(client_id= client.client_id, client_name=client_name)
        return clients
    else:
        client_name:str = room_to_exit.get_client_name(client_id=client_id)
        room_to_exit.remove_client(client_id=client_id)
        clients.append(client_id)
        LOBBY.add_client(client_id=client_id, client_name=client_name)
        return client_id

def get_all_client_ids_in_room(client_id:int) -> List[int]:
    global rooms
    client_ids:List[int] = []
    for room in rooms:
        if room.check_client_in_room(client_id=client_id):
            client_ids = room.get_all_client_id()
            break
    return client_ids
