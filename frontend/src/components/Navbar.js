import { BackendIp } from '../endpoints/GetIp'
import { BackendPort } from '../endpoints/GetPort'
import { BackendFormat } from '../endpoints/GetFormat'
import { ServerState } from '../endpoints/GetServerStatus'

export const Navbar = () => {
    let ip = BackendIp();
    let port = BackendPort();
    let format = BackendFormat();
    let state = ServerState();
    return (
        <div class="container-fluid bg-dark text-white">
            <div class="row nav">
                <div class="col">{ip}</div>
                <div class="col">{port}</div>
                <div class="col">SERVER NAME</div>
                <div class="col">{format}</div>
                <div class="col">{state}</div>
            </div>
        </div>
    )
}
