// src/ItemListForm.js
import React from 'react';
import { Person } from './types';

export interface PeopleListProps {
    exclusions: Person[][];
    removeExclusion: (index: number) => void;
}

const ExclusionsList = ({
        exclusions,
        removeExclusion
    }: PeopleListProps) => {

    if (exclusions.length === 0) {
        return <></>
    }
    return (
        <div>
            <h3>Exclusions:</h3>
            <table>
                <tbody>
                    {exclusions.map((match, index) => (
                        <tr key={index}>
                            <th>{`${match[0].name}`}</th>
                            <th>{`${match[1].name}`}</th>
                            <th style={{textAlign: 'right'}}>
                                <button className="button-18" onClick={() => removeExclusion(index)}>Remove</button>
                            </th>
                        </tr>
                    ))} 
                </tbody>
            </table>
        </div>
    );
};

export default ExclusionsList;
