import { BASE_URL } from "./CONFIG"

export const SetBackendIp = (new_ip) => {
    fetch(BASE_URL + "/server/ip/set", {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ip: new_ip
        })
    }).then(() => {
        window.location.reload();
    })
}
