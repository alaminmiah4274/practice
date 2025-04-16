const FirstComponent = () => {
  /* 
  Way ---> 1 

  const name = "Al Amin Miah";

  const content = name ? name : "FirstComponent";

  return (
    <>
      <h1>Hello, {content}</h1>
    </>
  ); */
  /*
	Way ---> 2

  const name = "Al Amin Miah";

  return (
    <>
      <h1>Hello, {name ? name : "First Component"}</h1>
    </>
  );
  */
  /*
  Way ---> 3

  const name = "Al Amin Miah";

  return (
    <>
      <h1>Hello, {name}</h1>
    </>
  );
  */
  /*
  Way ---> 4

  const name = "Al Amin Miah";

  return (
    <>
      <h1>Hello, {name && "First Component"}</h1>
    </>
  );
  */

  // Way ---> 5
  const name = "Al Amin Miah";

  return (
    <>
      <h1>Hello, {name || "First Component"}</h1>
    </>
  );
};

export default FirstComponent;
