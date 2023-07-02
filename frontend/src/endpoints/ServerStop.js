import { BASE_URL } from "./CONFIG"

export const ServerStop = () => {
    fetch(BASE_URL + "/server/close", {
        mode: "no-cors",
    }).then(() => {
        window.location.reload();
    })
}
