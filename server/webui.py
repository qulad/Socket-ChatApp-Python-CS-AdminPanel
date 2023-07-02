from configparser import ConfigParser
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources import ClientCountResource, ServerGetIPResource, ServerGetPortResource, ServerGetFormatResource, ServerCommandsResource, ServerStartResource, ServerCloseResource, ServerAllRoomsResource, ServerSetIPResource, ServerSetPortResource, ServerSetFormatResource, ServerResetIPResource, ServerResetPortResource, ServerResetFormatResource, ServerStatus, ServerGetDefaultIp, ServerGetDefaultPort, ServerGetDefaultFormat, ServerGetRoomCountResource

app:Flask = Flask(__name__)
CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
config:ConfigParser = ConfigParser()
config.read("config.ini")

PORT:int = int(config.get("WEBUI", "PORT"))
IP:str = config.get("WEBUI", "IP")

app.config["SQLALCHEMY_DATABASE_URI"] = config.get("WEBUI", "DB_URI")

api:Api = Api(app=app, prefix="/api/v1")

api.add_resource(ClientCountResource, "/client/count")
api.add_resource(ServerGetIPResource, "/server/ip/get")
api.add_resource(ServerGetPortResource, "/server/port/get")
api.add_resource(ServerGetFormatResource, "/server/format/get")
api.add_resource(ServerCommandsResource, "/server/commands")
api.add_resource(ServerStartResource, "/server/start")
api.add_resource(ServerCloseResource, "/server/close")
api.add_resource(ServerAllRoomsResource, "/server/room/all")
api.add_resource(ServerSetIPResource, "/server/ip/set")
api.add_resource(ServerSetPortResource, "/server/port/set")
api.add_resource(ServerSetFormatResource, "/server/format/set")
api.add_resource(ServerResetIPResource, "/server/ip/reset")
api.add_resource(ServerResetPortResource, "/server/port/reset")
api.add_resource(ServerResetFormatResource, "/server/format/reset")
api.add_resource(ServerStatus, "/server/status")
api.add_resource(ServerGetDefaultIp, "/server/ip/default")
api.add_resource(ServerGetDefaultPort, "/server/ip/default")
api.add_resource(ServerGetDefaultFormat, "/server/format/default")
api.add_resource(ServerGetRoomCountResource, "/server/room/count")

def run_webui() -> None:
    app.run(debug=True, host=IP, port=PORT)

if __name__ == "__main__":
    run_webui()
