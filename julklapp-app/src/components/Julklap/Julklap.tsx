// src/ItemListForm.js
import React, { useState } from 'react';
import AddPerson from './AddPerson';
import PeopleList from './PeopleList';
import SenderEmail from './SenderEmail';
import GenerateJulklapButton from './GenerateJulklapButton';
import ResetButton from './ResetButton';
import ExclusionsList from './ExclusionsList';
import { EmailConnector, Person } from './types';


const Julklap = () => {
    const [people, setPeople] = useState<Person[]>([]);
    const [exclusions, setExclusions] = useState<Person[][]>([]);

    const [emailConnector, setEmailConnector] = useState<EmailConnector>(
        { address: '', password: '' }
    );
    
    const addPerson = (person: Person) => { 
        setPeople([...people, person]);
    };
    
    const addExclusion = (exclusion: Person[]) => { 
        setExclusions([...exclusions, exclusion]);
    };
    
    const removeExclusion = (index: number) => {
        setExclusions(exclusions.filter((_, i) => i !== index));
    };
    
    const removePerson = (index: number) => {
        var removedPerson = people[index];
        setPeople(people.filter((_, i) => i !== index));
        setExclusions(exclusions.filter(
            (match, _) => (match[0].name !== removedPerson.name && match[1].name !== removedPerson.name)
        ));
    };

    return (
        <div>
            <h1>JULKLAP</h1> 
            <AddPerson addPerson={ addPerson } />
            <PeopleList
                people={ people }
                removePerson={ removePerson }
                addExclusion={ addExclusion }
            />
            <ExclusionsList
                exclusions={ exclusions }
                removeExclusion={ removeExclusion }
            />
            <SenderEmail
                setEmailConnector={ setEmailConnector }
            />

            <p>
                E-mail address: {emailConnector.address},
                e-mail password: {'*'.repeat(emailConnector.password.length)}
            </p>

            <GenerateJulklapButton
                people={ people }
                exclusions={ exclusions }
                emailConnector={ emailConnector }
            />
            <ResetButton
                people={ people }
                emailConnector={ emailConnector }
                setPeople={ setPeople }
                setExclusions={ setExclusions }
                setEmailConnector={ setEmailConnector }
            />
        </div>
    );
};

export default Julklap;
