import { BASE_URL } from "./CONFIG"

export const SetBackendPort = (new_port) => {
    fetch(BASE_URL + "/server/port/set", {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            port: new_port
        })
    }).then(() => {
        window.location.reload();
    })
}
