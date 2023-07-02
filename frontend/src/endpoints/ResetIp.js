import { BASE_URL } from "./CONFIG"

export const ResetBackendIp = () => {
    fetch(BASE_URL + "/server/ip/reset").then(() => {
        window.location.reload();
    })
}
