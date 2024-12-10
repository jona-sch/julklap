// src/ItemListForm.js
import React from 'react';
import { Person } from './types';
import ExclusionsListElement from './ExclusionsListElement';

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
                        <ExclusionsListElement
                            index={ index }
                            match={ match }
                            removeExclusion={ removeExclusion }    
                        />
                    ))} 
                </tbody>
            </table>
        </div>
    );
};

export default ExclusionsList;
