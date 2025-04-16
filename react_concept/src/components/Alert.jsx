import { CircleX } from "lucide-react";

const Alert = ({ color = "success", children, onClose }) => {
  const alertStyles = {
    success: "bg-green-100 text-green-700 border-green-700",
    danger: "bg-red-100 text-red-700 border-red-300",
    warning: "bg-yellow-100 text-yellow-700 border-yellow-300",
    info: "bg-cyan-100 text-cyan-700 border-cyan-300",
    primary: "bg-blue-100 text-blue-700 border-blue-700",
  };

  return (
    <>
      <div
        className={`flex items-center justify-between mt-10 p-4 ${alertStyles[color]}`}
      >
        <span>{children}</span>
        <button onClick={onClose}>
          <CircleX className="text-red-700 hover:text-red-400" />
        </button>
      </div>
    </>
  );
};

export default Alert;
