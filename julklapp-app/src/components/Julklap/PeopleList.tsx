// src/ItemListForm.js
import React, { useState } from 'react';
import { Person } from './types';

export interface PeopleListProps {
    people: Person[];
    removePerson: (index: number) => void;
    addExclusion: (exclusion: Person[]) => void;
}

const PeopleList = ({
        people,
        removePerson,
        addExclusion
    }: PeopleListProps) => {
    const [matches, setMatches] = useState<Person[]>([]);

    const selectPerson = (index: number) => {
        const person = people[index];
        if (matches.length < 1) {
            setMatches([person]);
        }
        else if (matches.length === 1) {
            addExclusion([...matches, person]);
            setMatches([]);
        }
    };

    if (people.length === 0) {
        return <></>
    }
    return (
        <div>
            <h3>People:</h3>
            <table>
                <thead>
                    <tr>
                        <th><b>Name</b></th>
                        <th><b>E-mail address</b></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {people.map((person, index) => (
                        <tr key={index}>
                            <th> {`${person.name}`} </th>
                            <th> {`${person.email}`}</th>
                            <th style={{textAlign: 'right'}}>
                                <button className="button-18" onClick={() => removePerson(index)}>Remove</button>
                                <button className="button-18" onClick={() => selectPerson(index)}>Select for exclusion</button>
                            </th>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default PeopleList;
