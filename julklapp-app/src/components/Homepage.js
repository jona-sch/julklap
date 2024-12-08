// src/ItemListForm.js
import React, { useState } from 'react';
import axios from 'axios';

const Homepage = () => {
    const [personName, setName] = useState('');
    const [personEmail, setEmail] = useState('');

    const [exclusions, setExclusions] = useState([]);
    const [matches, setMatches] = useState([]);

    const [emailConnectorAddress, setSenderAddress] = useState('');
    const [emailConnectorPassword, setSenderPassword] = useState('');
    const [emailConnectorAddressDisplay, setSenderAddressDisplay] = useState('');
    const [emailConnectorPasswordDisplay, setSenderPasswordDisplay] = useState('');
    const [emailConnector, setEmailConnector] = useState({});

    const [people, setPeople] = useState([]);

    const addPerson = () => {
        if (personName && personEmail) {
            setPeople([...people, { name: personName, email: personEmail }]);
            setName('');
            setEmail('');
        }
    };

    const removePerson = (index) => {
        var removedPerson = people[index];
        setPeople(people.filter((person, i) => i !== index));
        setExclusions(exclusions.filter(
            (match, i) => (match[0].name !== removedPerson.name && match[1].name !== removedPerson.name)
        ));
    };

    const removeMatch = (index) => {
        setExclusions(exclusions.filter((match, i) => i !== index));
    };

    const addEmailSender = () => {
        if (emailConnectorAddress && emailConnectorPassword) {
            setEmailConnector({ sender_address: emailConnectorAddress, sender_password: emailConnectorPassword });
            setSenderAddressDisplay(emailConnectorAddress);
            setSenderPasswordDisplay("*".repeat(emailConnectorPassword.length));
        }
    };

    const selectPerson = (index) => {
        const person = people[index];
        if (matches.length < 1) {
            setMatches([person]);
        }
        else if (matches.length === 1) {
            setExclusions([...exclusions, [...matches, person]]);
            setMatches([]);
        }
    };

    const resetJulklap = () => {
        setMatches([]);
        setPeople([]);
        setExclusions([]);
        setSenderAddressDisplay('');
        setSenderPasswordDisplay('');
        setSenderAddress('');
        setSenderPassword('');
        setEmailConnector({});
    };

    const handleSubmit = async () => {
        try {
            const response = await axios.post(
                '/julklap',
                {
                    group: {
                        people: people,
                        exclusions: exclusions
                    },
                    email_connector_model: emailConnector
                }
            );
            alert(`${response.data.message}`);
            // setPeople([]);
        } catch (error) {
            console.error('There was an error submitting the items!', error);
        }
    };

    return (
        <div>
            <div>
            <h1>JULKLAP</h1>
            <h2>Add a person:</h2>
            <form onSubmit={(e) => e.preventDefault()}>
                <table>
                    <tbody>
                        <tr>
                            <th>
                                <label htmlFor="name">Name:</label>
                            </th>
                            <th>
                                <input 
                                    type="text" 
                                    value={personName} 
                                    onChange={(e) => setName(e.target.value)} 
                                />
                            </th>
                        </tr>
                        <tr>
                            <th>
                                <label htmlFor="email">E-mail address:</label>
                            </th>
                            <th>
                                <input 
                                    type="text" 
                                    value={personEmail} 
                                    onChange={(e) => setEmail(e.target.value)} 
                                />
                            </th>
                        </tr>
                    </tbody>
                </table>
                <button className="button-18" type="button" onClick={addPerson}><b>Add Person</b></button>
            </form>

            <h3>People:</h3>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>E-mail address</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {people.map((person, index) => (
                        <tr key={index}>
                            <th> {`${person.name}`} </th>
                            <th> {`${person.email}`}</th>
                            <th style={{"text-align": 'right'}}>
                                <button className="button-18" onClick={() => removePerson(index)}>Remove</button>
                                <button className="button-18" onClick={() => selectPerson(index)}>Select for exclusion</button>
                            </th>
                        </tr>
                    ))}
                </tbody>
            </table>

            <h3>Exclusions:</h3>
            <table>
                <tbody>
                    {exclusions.map((match, index) => (
                        <tr key={index}>
                            <th>{`${match[0].name}`}</th>
                            <th>{`${match[1].name}`}</th>
                            <th style={{"text-align": 'right'}}>
                                <button className="button-18" onClick={() => removeMatch(index)}>Remove</button>
                            </th>
                        </tr>
                    ))} 
                </tbody>
            </table>

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
                <button className="button-18" type="button" onClick={addEmailSender}><b>Add Sender</b></button>
            </form>

            <p>
                E-mail address: {emailConnectorAddressDisplay}, e-mail password: {emailConnectorPasswordDisplay}
            </p>
            </div>
            <div>
            <h2><button className="button-julklap" type="button" onClick={handleSubmit}><b>Generate Julklap</b></button></h2>
            <h2><button className="button-julklap" type="button" onClick={resetJulklap}><b>Reset</b></button></h2>
            </div>
        </div>
    );
};

export default Homepage;
