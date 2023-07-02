import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const BackendPort = () => {
    const [port, setPort] = useState([{}])
    
    useEffect(() => {
        getPort()
    }, [])
    
    let getPort = async () => {
        let response = await fetch(BASE_URL + "/server/port/get")
        let data = await response.json()
        setPort(data)
    }
    return port.message
}
