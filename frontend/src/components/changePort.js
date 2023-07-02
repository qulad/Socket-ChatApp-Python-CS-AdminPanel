import React, { useState } from "react";
import { SetBackendPort } from "../endpoints/SetPort";
import { ResetBackendPort } from "../endpoints/ResetPort";

export const ChangePort = () => {
    const [isChangingIP, setIsChangingIP] = useState(false); // IP değiştirme durumu
    const [newIPAddress, setNewIPAddress] = useState(""); // Yeni IP adresi

    const handleIPChange = () => {
        setIsChangingIP(true);
    };
    
    const handleConfirm = () => {
        if (/^((6553[0-5])|(655[0-2][0-9])|(65[0-4][0-9]{2})|(6[0-4][0-9]{3})|([1-5][0-9]{4})|([0-5]{0,5})|([0-9]{1,4}))$/.test(newIPAddress)){
            SetBackendPort(newIPAddress);
        }
        else {
            alert("Invalid PORT");
        }
    };
    const handleCancel = () => {
        setIsChangingIP(false);
        setNewIPAddress("");
    };
    const handleReset = () => {
        ResetBackendPort();
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
                    <button onClick={handleIPChange} className="col-12">CHANGE PORT</button>
            )}
        </div>
    );
}
