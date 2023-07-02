import { useState } from "react";
import { AllRooms } from "../endpoints/GetAllRooms";

export const Rooms = () => {
    const [show, setShow] = useState(false);
    let all_rooms = AllRooms();

    const handleShow = () => {
        setShow(true);
    };
    const handleHide = () => {
        setShow(false);
    };

    return (
        <div className="rooms">
            {show ? (
                <div className="rooms-show">
                    <button onClick={handleHide} className="rooms-button-hide">HIDE ROOMS</button>
                    {(typeof all_rooms === 'undefined') ? (
                        <h3 className="rooms-null">NO ROOMS AVAILABLE</h3>
                    ) : (
                        Object.entries(all_rooms).map(([room_key, room]) => (
                            <div key={room_key} className="rooms-room-div">
                                <p className="rooms-room">room id: {room.room_id}, room name: {room.room_name}, owner: {room.owner}</p>
                                {Object.entries(room.clients).map(([client_key, client]) => (
                                    <p key={client_key} className="rooms-client">client id: {client.client_id}, client name: {client.client_name}, client room id: {client.room_id}</p>
                            ))}
                            </div>
                        ))
                    )}

                </div>
                ) : (
                    <button onClick={handleShow} className="col-12">SHOW ROOMS</button>
                )
            }
        </div>
    );
}
