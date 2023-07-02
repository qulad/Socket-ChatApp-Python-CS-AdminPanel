import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const BackendDefaultIp = () => {
    const [ip, setIp] = useState([{}])
    
    useEffect(() => {
        getIp()
    }, [])
    
    let getIp = async () => {
        let response = await fetch(BASE_URL + "/server/ip/default")
        let data = await response.json()
        setIp(data)
    }
    return ip.message
}
