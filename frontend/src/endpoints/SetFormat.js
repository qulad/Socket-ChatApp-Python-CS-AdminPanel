import { BASE_URL } from "./CONFIG"

export const SetBackendFormat = (new_format) => {
    fetch(BASE_URL + "/server/format/set", {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            format: new_format
        })
    }).then(() => {
        window.location.reload();
    })
}
