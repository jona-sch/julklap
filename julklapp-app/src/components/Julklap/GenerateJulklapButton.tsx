import axios from 'axios';
import { EmailConnector, Person } from './types';

export interface GenerateButtonProps {
    people: Person[];
    exclusions: Person[][];
    emailConnector: EmailConnector;
}

const GenerateJulklapButton = ({
        people,
        exclusions,
        emailConnector
    }: GenerateButtonProps) => {

    const handleSubmit = async () => {
        try {
            const response = await axios.post(
                '/julklap',
                {
                    group: {
                        people: people,
                        exclusions: exclusions
                    },
                    email_connector_model: {
                        sender_address: emailConnector.address,
                        sender_password: emailConnector.password
                    }
                }
            );
            alert(`${response.data.message}`);
        } catch (error) {
            console.error('There was an error submitting the items!', error);
        }
    };

    return (
        <h2>
            <button
                className="button-julklap"
                type="button"
                onClick={handleSubmit}
                disabled={
                    people === undefined ||
                    people.length === 0 ||
                    emailConnector.address == '' ||
                    emailConnector.password == ''
                }
            >
                <b>Generate Julklap</b>
            </button>
        </h2>
    );
};

export default GenerateJulklapButton;
