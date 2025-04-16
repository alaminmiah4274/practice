const Button = ({ color = "primary", children, handleAlert, className }) => {
  const btnColor = {
    primary: "bg-blue-500",
    success: "bg-green-500",
    warning: "bg-yellow-500",
    info: "bg-cyan-500",
    danger: "bg-red-500",
  };
  return (
    <>
      <button
        onClick={handleAlert}
        className={`${className} text-white p-3 rounded-sm ${btnColor[color]}`}
      >
        {children}
      </button>
    </>
  );
};

export default Button;
