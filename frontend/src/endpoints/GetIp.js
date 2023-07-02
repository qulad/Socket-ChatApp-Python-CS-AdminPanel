import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const BackendIp = () => {
    const [ip, setIp] = useState([{}])
    
    useEffect(() => {
        getIp()
    }, [])
    
    let getIp = async () => {
        let response = await fetch(BASE_URL + "/server/ip/get")
        let data = await response.json()
        setIp(data)
    }
    return ip.message
}
