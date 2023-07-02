import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const BackendDefaultPort = () => {
    const [port, setPort] = useState([{}])
    
    useEffect(() => {
        getPort()
    }, [])
    
    let getPort = async () => {
        let response = await fetch(BASE_URL + "/server/port/default")
        let data = await response.json()
        setPort(data)
    }
    return port.message
}
