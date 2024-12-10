// src/ItemListForm.js
import { useState } from 'react';
import { Person } from './types';

export interface AddPersonProps {
    addPerson: (person: Person) => void;
}

const AddPerson = ({
        addPerson
    }: AddPersonProps) => {
    const [personName, setName] = useState('');
    const [personEmail, setEmail] = useState('');

    const addSinglePerson = () => {
        if (personName && personEmail) {
            addPerson({ name: personName, email: personEmail });
            setName('');
            setEmail('');
        }
    };

    return (
        <div>
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
                <button
                    className="button-18"
                    type="button"
                    onClick={addSinglePerson}
                    disabled={!personName || !personEmail}
                >
                    <b>Add Person</b>
                </button>
            </form>
        </div>
    );
};

export default AddPerson;
