import { ServerState } from "../endpoints/GetServerStatus";
import { ClientCount } from "../endpoints/GetClientCount";
import { RoomCount } from "../endpoints/GetRoomCount";
import { ServerStart } from "../endpoints/ServerStart";
import { ServerStop } from "../endpoints/ServerStop";

export const Control = () => {
    let state = ServerState();
    let client_count = ClientCount();
    let room_count = RoomCount();
    const close_click = () => {
        ServerStop();
    };
    let start_click = () => {
        ServerStart();
    };
    return (
        <div className="control">
            {(state === "Server is active") ? (
                <div className="row">
                    <h3 className="col">CLIENT COUNT: {client_count}</h3>
                    <h3 className="col">ROOM COUNT: {room_count}</h3>
                    <button type="button" className="col d-flex justify-content-center" onClick={close_click}>CLOSE CHATAPP</button>
                </div>
            ) : ( (state === "Server is not running") ? (
                <div className="row">
                    <button type="button" className="row d-flex justify-content-center" onClick={start_click}>START CHATAPP</button>
                </div>
            ) : (
                <div className="row">
                    <h3 className="col d-flex justify-content-center">LOADING...</h3>
                </div>
            )
            )}
        </div>
    )
}
