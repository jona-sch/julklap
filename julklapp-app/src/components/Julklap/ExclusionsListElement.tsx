// src/ItemListForm.js
import React from 'react';
import { Person } from './types';

export interface ExclusionsListElementProps {
    index: number;
    match: Person[];
    removeExclusion: (index: number) => void;
}

const ExclusionsListElement = ({
        index,
        match,
        removeExclusion
    }: ExclusionsListElementProps) => {

    return (
        <tr key={index}>
            <th>{`${match[0].name}`}</th>
            <th>{`${match[1].name}`}</th>
            <th style={{textAlign: 'right'}}>
                <button className="button-18" onClick={() => removeExclusion(index)}>Remove</button>
            </th>
        </tr>
    );
};

export default ExclusionsListElement;
