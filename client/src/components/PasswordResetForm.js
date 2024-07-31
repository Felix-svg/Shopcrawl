import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";

const PasswordResetForm = () => {
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [message, setMessage] = useState("");
  const location = useLocation();
  const navigate = useNavigate();
  const query = new URLSearchParams(location.search);
  const token = query.get("token");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setMessage("Passwords do not match.");
      return;
    }

    try {
      const response = await fetch(
        `https://shopcrawl-server.onrender.com/reset-password/${token}`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ password }),
        }
      );

      const data = await response.json();
      if (response.ok) {
        setMessage(
          "Password reset successful. You can now log in with your new password."
        );
        navigate("/login");
      } else {
        setMessage(`Error: ${data.error}`);
      }
    } catch (error) {
      setMessage("An error occurred. Please try again later.");
    }
  };

  const isError = message.toLowerCase().includes("error");

  return (
    <div
      className="container-fluid min-vh-100 d-flex justify-content-center align-items-center bg-light"
      style={{ backgroundColor: "#90AEAD" }}
    >
      <div
        className="bg-white rounded-lg shadow-lg p-4"
        style={{ width: "100%", maxWidth: "400px" }}
      >
        <h2 className="text-2xl font-bold mb-6 text-gray-800 text-center">
          Reset Password
        </h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label
              htmlFor="password"
              className="block text-sm font-medium text-gray-700"
            >
              New Password
            </label>
            <input
              type="password"
              className="form-control mt-1 block w-100 p-2 border border-gray-300 rounded-full shadow-sm focus:ring-blue-500 focus:border-blue-500"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <div className="mb-4">
            <label
              htmlFor="confirmPassword"
              className="block text-sm font-medium text-gray-700"
            >
              Confirm Password
            </label>
            <input
              type="password"
              className="form-control mt-1 block w-100 p-2 border border-gray-300 rounded-full shadow-sm focus:ring-blue-500 focus:border-blue-500"
              id="confirmPassword"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </div>
          <button
            type="submit"
            className="btn w-100 text-white font-semibold rounded-full shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 mb-4"
            style={{ backgroundColor: "teal" }}
          >
            Reset Password
          </button>
          {message && (
            <p
              className={`mt-4 text-center ${
                isError ? "text-danger" : "text-success"
              }`}
            >
              {message}
            </p>
          )}
        </form>
      </div>
    </div>
  );
};

export default PasswordResetForm;