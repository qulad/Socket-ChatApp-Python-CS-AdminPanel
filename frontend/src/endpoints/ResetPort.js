import { BASE_URL } from "./CONFIG"

export const ResetBackendPort = () => {
    fetch(BASE_URL + "/server/port/reset").then(() => {
        window.location.reload();
    })
}
