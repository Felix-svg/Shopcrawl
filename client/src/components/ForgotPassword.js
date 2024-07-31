import React, { useState } from "react";
import { Link } from "react-router-dom";

const ForgotPassword = () => {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleEmailChange = (e) => setEmail(e.target.value);

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsSubmitting(true);

    fetch("https://shopcrawl-server.onrender.com/forgot-password", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email }),
    })
      .then((resp) => resp.json())
      .then((data) => {
        setMessage(data.message || "Error sending password reset email");
      })
      .catch(() => setMessage("Error sending password reset email"))
      .finally(() => setIsSubmitting(false));
  };

  const isError = message.toLowerCase().includes("error") || message.toLowerCase().includes("not");

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
          Forgot Password
        </h2>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label
              htmlFor="email"
              className="block text-sm font-medium text-gray-700"
            >
              Email address
            </label>
            <input
              type="email"
              className="form-control mt-1 block w-100 p-2 border border-gray-300 rounded-full shadow-sm focus:ring-blue-500 focus:border-blue-500"
              id="email"
              value={email}
              onChange={handleEmailChange}
              required
            />
          </div>
          <button
            type="submit"
            className={`btn w-100 text-white font-semibold rounded-full shadow-sm focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 mb-4 ${
              isSubmitting
                ? "opacity-50 cursor-not-allowed"
                : "hover:bg-blue-600"
            }`}
            disabled={isSubmitting}
            style={{ backgroundColor: "teal" }}
          >
            {isSubmitting ? "Sending..." : "Send Password Reset Email"}
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

          <Link
            to="/login"
            className="block text-center hover:text-blue-400"
            style={{ color: "teal" }}
          >
            Back to login
          </Link>
        </form>
      </div>
    </div>
  );
};

export default ForgotPassword;