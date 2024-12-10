import { EmailConnector, Person } from "./types";

export interface ResetButtonProps {
    people: Person[],
    emailConnector: EmailConnector,
    setPeople: (people: Person[]) => void;
    setExclusions: (people: Person[][]) => void;
    setEmailConnector: (emailConnector: EmailConnector) => void;
}

const ResetButton = ({
        people,
        emailConnector,
        setPeople,
        setExclusions,
        setEmailConnector
    }: ResetButtonProps) => {

    const resetJulklap = () => {
        setPeople([]);
        setExclusions([]);
        setEmailConnector({ address: '', password: '' });
    };

    return (
        <h2>
            <button
                className="button-julklap"
                type="button"
                onClick={resetJulklap}
                disabled={
                    (people === undefined ||
                    people.length === 0) &&
                    (emailConnector.address == '' ||
                    emailConnector.password == '')
                }
            >
                <b>Reset</b>
            </button>
        </h2>
    );
};

export default ResetButton;
