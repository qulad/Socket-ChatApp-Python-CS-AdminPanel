import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const AllRooms = () => {
    const [rooms, setRooms] = useState([{}])
    
    useEffect(() => {
        getRooms()
    }, [])
    
    let getRooms = async () => {
        let response = await fetch(BASE_URL + "/server/room/all")
        let data = await response.json()
        setRooms(data)
    }
    return rooms.message
}
