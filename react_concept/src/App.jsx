import FirstComponent from "./components/FirstComponent";
import List from "./components/List";
import PlayWithButton from "./components/PlayWithButton";

function App() {
  const fruits = ["apple", "mango", "orange", "lemon", "cherry"];
  const cities = ["dhaka", "rajshahi", "khulna", "chittagong", "sylhet"];

  return (
    <>
      <FirstComponent />
      <List items={fruits} heading="Fruits" />
      <List items={cities} heading="Cities" />

      <PlayWithButton />
    </>
  );
}

export default App;
