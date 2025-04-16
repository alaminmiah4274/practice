import { useState } from "react";
import Alert from "./Alert";
import Button from "./Button";

const PlayWithButton = () => {
  const [alertVisibility, setAlertVisibility] = useState(false);
  return (
    <>
      {alertVisibility && (
        <Alert color="info" onClose={() => setAlertVisibility(false)}>
          You have clicked the button
        </Alert>
      )}
      <Button
        className="font-bold hover:bg-black"
        handleAlert={() => setAlertVisibility(true)}
        color="success"
      >
        Click Me
      </Button>
    </>
  );
};

export default PlayWithButton;
