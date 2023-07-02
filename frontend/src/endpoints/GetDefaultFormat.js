import { useState, useEffect } from "react"
import { BASE_URL } from "./CONFIG"

export const BackendDefaultFormat = () => {
    const [format, setFormat] = useState([{}])
    
    useEffect(() => {
        getFormat()
    }, [])
    
    let getFormat = async () => {
        let response = await fetch(BASE_URL + "/server/format/default")
        let data = await response.json()
        setFormat(data)
    }
    return format.message
}
