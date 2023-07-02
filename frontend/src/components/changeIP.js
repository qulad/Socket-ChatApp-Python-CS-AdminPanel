import React, { useState } from "react";
import { SetBackendIp } from "../endpoints/SetIp";
import { ResetBackendIp } from "../endpoints/ResetIp";

export const ChangeIP = () => {
    const [isChangingIP, setIsChangingIP] = useState(false); // IP değiştirme durumu
    const [newIPAddress, setNewIPAddress] = useState(""); // Yeni IP adresi

    const handleIPChange = () => {
        setIsChangingIP(true);
    };
    
    const handleConfirm = () => {
        if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(newIPAddress)){
            SetBackendIp(newIPAddress);
        }
        else {
            alert("Invalid IP ADDRESS");
        }
    };
    const handleCancel = () => {
        setIsChangingIP(false);
        setNewIPAddress("");
    };
    const handleReset = () => {
        ResetBackendIp();
    };
    const handleChange = (event) => {
        setNewIPAddress(event.target.value);
    };
    return (
        <div className="change">
            {isChangingIP ? (
                <div>
                    <div className="row-md-6">
                        <input type="text" value={newIPAddress} onChange={handleChange} className="col-md-8"/>
                        <button onClick={handleReset} className="col-md-4">RESET</button>
                    </div>
                    <div className="row">
                        <button onClick={handleConfirm} className="col">CONFIRM</button>
                        <button onClick={handleCancel} className="col">DENY</button>
                    </div>
                </div>
            ) : (
                    <button onClick={handleIPChange} className="col-12">CHANGE IP ADDRESS</button>
            )}
        </div>
    );
}
