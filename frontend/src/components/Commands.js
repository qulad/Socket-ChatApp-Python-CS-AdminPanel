import { ClientCommands } from "../endpoints/GetServerCommands"

export const Commands = () => {
    let client_commands = ClientCommands();
    return (
        <div className="commands">
            {(typeof client_commands === 'undefined') ? (
                <p>Loading commands...</p>
            ) : (
                <ul className="list-group">
                    {Object.entries(client_commands).map(([key, value]) => (
                        <li key={key} className="list-group-item">
                            <span className="font-weight-bold">Command Name:</span> {value.command}<br />
                            <span className="font-weight-bold">Command Description:</span> {value.description}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}
