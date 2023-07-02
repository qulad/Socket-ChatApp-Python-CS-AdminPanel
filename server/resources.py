from flask_restful import Resource, reqparse
from configparser import ConfigParser
from typing import Dict
import chatapp
from chatapp import run_server, close_server
from logic import rooms
from threads import client_count

config:ConfigParser = ConfigParser()
config.read("config.ini")

IP:str = None
PORT:int = None
FORMAT:str = None

class ClientCountResource(Resource):
    def get(self):
        if chatapp.RUNNING:
            return {"message": str(client_count())}, 200
        return {"message": "Server is not open"}, 400

class ServerGetIPResource(Resource):
    def get(self):
        global IP, config
        ip:str = config.get("CHAT", "IP") if IP == None else IP
        return {"message": ip}, 200
    
class ServerGetPortResource(Resource):
    def get(self):
        global PORT, config
        port:str = config.get("CHAT", "PORT") if PORT == None else PORT
        return {"message": port}, 200

class ServerGetFormatResource(Resource):
    def get(self):
        global FORMAT, config
        format:str = config.get("CHAT", "FORMAT") if FORMAT == None else FORMAT
        return {"message": format}, 200

class ServerCommandsResource(Resource):
    def get(self):
        data:Dict[str, str] = {
            "0": {"command": ":login <user_name>", "description": "login as <user_name>"},
            "1": {"command": ":logout", "description": "logout"},
            "2": {"command": ":list_rooms", "description": "list all rooms that are open"},
            "3": {"command": ":list_users", "description": "list all users in the room you are in"},
            "4": {"command": ":enter <room_name>", "description": "enter room <room_name>"},
            "5": {"command": ":whereami", "description": "see what room you are in"},
            "6": {"command": ":open <room_name>", "description": "create room <room_name>"},
            "7": {"command": ":close <room_name>", "description": "exit room <room_name>"},
            "8": {"command": ":help", "description": "see all commands"}
            }
        return {"message": data}, 200

class ServerStartResource(Resource):
    def get(self):
        if chatapp.RUNNING:
            return {"message": "Server is already chatapp.RUNNING!"}, 405
        run_server(ip=IP, port=PORT)
        return {"message": "Server is chatapp.RUNNING"}, 200

class ServerCloseResource(Resource):
    def get(self):
        if not chatapp.RUNNING:
            return {"message": "Server is already down!"}, 405
        close_server()
        return {"message": "Server is closed"}, 200

class ServerAllRoomsResource(Resource):
    def get(self):
        if not chatapp.RUNNING:
            return {"message": "Server is down!"}, 405
        rooms_dict:Dict[str, Dict[str, str]] = {}
        for i in range(len(rooms)):
            rooms_dict[str(i)] = {"room": rooms[i].to_dict()}
        return {"message": rooms_dict}, 200

class ServerSetIPResource(Resource):
    def put(self):
        if chatapp.RUNNING:
            return {"message": "Close the server first!"}, 405
        global IP
        parser:reqparse.RequestParser = reqparse.RequestParser()
        parser.add_argument("ip", type=str, required=True, help="ip cannot be empty!")
        args:Dict[str, str] = parser.parse_args()
        IP = args["ip"]
        return {"message": "Ip is updated"}, 200
        
class ServerSetPortResource(Resource):
    def put(self):
        if chatapp.RUNNING:
            return {"message": "Close the server first!"}, 405
        global PORT
        parser:reqparse.RequestParser = reqparse.RequestParser()
        parser.add_argument("port", type=int, required=True, help="port cannot be empty!")
        args:Dict[str, int] = parser.parse_args()
        PORT = args["port"]
        return {"message": "Port is updated"}, 200

class ServerSetFormatResource(Resource):
    def put(self):
        if chatapp.RUNNING:
            return {"message": "Close the server first!"}, 405
        global FORMAT
        parser:reqparse.RequestParser = reqparse.RequestParser()
        parser.add_argument("format", type=str, required=True, help="format cannot be empty!")
        args:Dict[str, str] = parser.parse_args()
        FORMAT = args["format"]
        return {"message": "Format is updated"}, 200

class ServerResetIPResource(Resource):
    def get(self):
        if chatapp.RUNNING:
            return {"message": "Close the server first!"}, 405
        global IP
        IP = None
        return {"message": "Ip is reseted"}, 205

class ServerResetPortResource(Resource):
    def get(self):
        if chatapp.RUNNING:
            return {"message": "Close the server first!"}, 405
        global PORT
        PORT = None
        return {"message": "Port is reseted"}, 205

class ServerResetFormatResource(Resource):
    def get(self):
        if chatapp.RUNNING:
            return {"message": "Close the server first!"}, 405
        global FORMAT
        FORMAT = None
        return {"message": "Format is reseted"}, 205
    
class ServerStatus(Resource):
    def get(self):
        text:str = "Server is active" if chatapp.RUNNING else "Server is not running"
        return {"message": text}, 200

class ServerGetDefaultIp(Resource):
    def get(self):
        return {"message": config.get("CHAT", "IP")}, 200
    
class ServerGetDefaultPort(Resource):
    def get(self):
        return {"message": config.get("CHAT", "Port")}, 200

class ServerGetDefaultFormat(Resource):
    def get(self):
        return {"message": config.get("CHAT", "Format")}, 200

class ServerGetRoomCountResource(Resource):
    def get(self):
        if not chatapp.RUNNING:
            return {"message": "Server is down!"}, 405
        return {"message": str(len(rooms))}, 200
