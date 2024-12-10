// src/ItemListForm.js
import React, { useState } from 'react';
import { EmailConnector } from './types';

export interface SenderEmailProps {
    setEmailConnector: (emailConnector: EmailConnector) => void;
}


const SenderEmail = ({
        setEmailConnector
    }: SenderEmailProps) => {
    const [emailConnectorAddress, setSenderAddress] = useState('');
    const [emailConnectorPassword, setSenderPassword] = useState('');

    const addEmailSender = () => {
        if (emailConnectorAddress && emailConnectorPassword) {
            if (/\S+@\S+\.\S+/.test(emailConnectorAddress)) {
                setEmailConnector( { address: emailConnectorAddress, password: emailConnectorPassword });
            } else {
                alert("Put in a correct e-mail address please.");
            }
        }
    };

    return (
        <div>
            <h2>Add the e-mail sender:</h2>
            <form onSubmit={(e) => e.preventDefault()}>
                <table>
                    <tbody>
                        <tr>
                            <th>
                                <label htmlFor="email">E-mail address:</label>
                            </th>
                            <th>
                                <input 
                                    type="text" 
                                    value={emailConnectorAddress} 
                                    onChange={(e) => setSenderAddress(e.target.value)} 
                                />
                            </th>
                        </tr>
                        <tr>
                            <th>
                                <label htmlFor="text">E-mail password:</label>
                            </th>
                            <th>
                                <input 
                                    type="password" 
                                    value={emailConnectorPassword} 
                                    onChange={(e) => setSenderPassword(e.target.value)} 
                                />
                            </th>
                        </tr>
                    </tbody>
                </table>
                <button
                    className="button-18"
                    type="button"
                    onClick={addEmailSender}
                    disabled={
                        !emailConnectorAddress ||
                        !emailConnectorPassword||
                        !/\S+@\S+\.\S+/.test(emailConnectorAddress)
                    }
                >
                    <b>Add Sender</b>
                </button>
            </form>
        </div>
    );
};

export default SenderEmail;
