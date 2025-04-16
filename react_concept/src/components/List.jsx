import { useState } from "react";

const List = ({ items = [], heading }) => {
  const [selectedIndex, setSelectedIndex] = useState(-1);

  return (
    <>
      <h1 className="text-2xl mt-10">{heading}</h1>
      {items.map((item, index) => {
        return (
          <li
            onClick={() => setSelectedIndex(index)}
            className={
              selectedIndex === index ? "bg-orange-300 text-red-700 p-3" : ""
            }
            key={index}
          >
            {item}
          </li>
        );
      })}
    </>
  );
};

export default List;
