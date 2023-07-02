import { BASE_URL } from "./CONFIG"

export const ResetBackendFormat = () => {
    fetch(BASE_URL + "/server/format/reset").then(() => {
        window.location.reload();
    })
}
