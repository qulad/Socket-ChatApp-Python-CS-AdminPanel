import React, { useState } from "react";
import { SetBackendFormat } from "../endpoints/SetFormat";
import { ResetBackendFormat } from "../endpoints/ResetFormat";

export const ChangeFormat = () => {
    const [isChangingIP, setIsChangingIP] = useState(false); // IP değiştirme durumu
    const [newIPAddress, setNewIPAddress] = useState(""); // Yeni IP adresi

    const handleIPChange = () => {
        setIsChangingIP(true);
    };
    
    const handleConfirm = () => {
        SetBackendFormat(newIPAddress);
    };
    const handleCancel = () => {
        setIsChangingIP(false);
        setNewIPAddress("");
    };
    const handleReset = () => {
        ResetBackendFormat();
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
                    <button onClick={handleIPChange} className="col-12">CHANGE FORMAT</button>
            )}
        </div>
    );
}
