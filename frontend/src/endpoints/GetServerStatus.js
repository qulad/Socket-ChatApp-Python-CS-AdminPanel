import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const ServerState = () => {
    const [state, setState] = useState([{}])
    
    useEffect(() => {
        getState()
    }, [])
    
    let getState = async () => {
        let response = await fetch(BASE_URL + "/server/status")
        let data = await response.json()
        setState(data)
    }
    return state.message
}
