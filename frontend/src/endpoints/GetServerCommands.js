import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const ClientCommands = () => {
    const [commands, setCommands] = useState([{}])
    
    useEffect(() => {
        getCommands()
    }, [])
    
    let getCommands = async () => {
        let response = await fetch(BASE_URL + "/server/commands")
        let data = await response.json()
        setCommands(data)
    }
    return commands.message
}
