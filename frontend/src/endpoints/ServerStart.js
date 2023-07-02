import { BASE_URL } from "./CONFIG"

export const ServerStart = () => {
    fetch(BASE_URL + "/server/start", {
        mode: "no-cors",
    }).then(() => {
        window.location.reload();
    })
}
