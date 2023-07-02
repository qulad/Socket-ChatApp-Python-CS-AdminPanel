import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const RoomCount = () => {
    const [count, setCount] = useState([{}])
    
    useEffect(() => {
        getCount()
    }, [])
    
    let getCount = async () => {
        let response = await fetch(BASE_URL + "/server/room/count")
        let data = await response.json()
        setCount(data)
    }
    return count.message
}
