import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const ClientCount = () => {
    const [client_count, setClientCount] = useState([{}])
    
    useEffect(() => {
        getClientCount()
    }, [])
    
    let getClientCount = async () => {
        let response = await fetch(BASE_URL + "/client/count")
        let data = await response.json()
        setClientCount(data)
    }
    return client_count.message
}
