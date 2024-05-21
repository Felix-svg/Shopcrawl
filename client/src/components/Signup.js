import React, { useState } from "react";
import { Link } from "react-router-dom";
import { IoMdEyeOff, IoMdEye } from "react-icons/io";
import "bootstrap/dist/css/bootstrap.min.css";
import { useNavigate } from "react-router-dom";

const Signup = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [message, setMessage] = useState("");
  const navigate = useNavigate()

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleConfirmPasswordChange = (e) => {
    setConfirmPassword(e.target.value);
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setMessage("Passwords do not match");
      return;
    }
    fetch("http://127.0.0.1:5000/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password, email }),
    })
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Signup failed");
        }
        return resp.json();
      })
      .then(() => {
        setPassword("");
        setUsername("");
        setEmail("");
        setConfirmPassword("");
        setMessage("Signup successful!");
        navigate("/login");
      })
      .catch((error) => {
        console.error(error);
        setMessage("Signup failed. Please try again.");
      });
  };

  return (
    <section
      className=" d-flex justify-content-center align-items-center"
      style={{
        backgroundColor:"#90AEAD",
        minHeight: "100vh",
        position: "relative"
      }}
    >
      <div
        className="position-absolute w-100 h-100"
      ></div>
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-lg-6 col-md-8 col-sm-10">
            <div className="card">
              <div className="card-body" >
                <h1 className="text-center mb-4" style={{ color: "teal" }}>
                  Create Account
                </h1>
                {message && (
                  <p
                    className={`text-center ${
                      message.includes("successful")
                        ? "text-success"
                        : "text-danger"
                    }`}
                  >
                    {message}
                  </p>
                )}

                <form onSubmit={handleSubmit}>
                  <div className="mb-3">
                    <label
                      htmlFor="username"
                      className="form-label"
                      style={{ color: "teal" }}
                    >
                      Your Username
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      id="username"
                      placeholder="Username"
                      required
                      value={username}
                      onChange={handleUsernameChange}
                    />
                  </div>
                  <div className="mb-3">
                    <label
                      htmlFor="email"
                      className="form-label"
                      style={{ color: "teal" }}
                    >
                      Your Email
                    </label>
                    <input
                      type="email"
                      className="form-control"
                      id="email"
                      placeholder="Email"
                      required
                      value={email}
                      onChange={handleEmailChange}
                    />
                  </div>
                  <div className="mb-3">
                    <label
                      htmlFor="password"
                      className="form-label"
                      style={{ color: "teal" }}
                    >
                      Password
                    </label>
                    <div className="input-group">
                      <input
                        type={showPassword ? "text" : "password"}
                        className="form-control"
                        id="password"
                        placeholder="••••••••"
                        required
                        value={password}
                        onChange={handlePasswordChange}
                      />
                      <button
                        className="btn btn-outline-secondary"
                        type="button"
                        onClick={togglePasswordVisibility}
                      >
                        {showPassword ? <IoMdEyeOff /> : <IoMdEye />}
                      </button>
                    </div>
                  </div>
                  <div className="mb-3">
                    <label
                      htmlFor="confirmPassword"
                      className="form-label"
                      style={{ color: "teal" }}
                    >
                      Confirm Password
                    </label>
                    <div className="input-group">
                      <input
                        type={showPassword ? "text" : "password"}
                        className="form-control"
                        id="confirmPassword"
                        placeholder="••••••••"
                        required
                        value={confirmPassword}
                        onChange={handleConfirmPasswordChange}
                      />
                      <button
                        className="btn btn-outline-secondary"
                        type="button"
                        onClick={togglePasswordVisibility}
                      >
                        {showPassword ? <IoMdEyeOff /> : <IoMdEye />}
                      </button>
                    </div>
                  </div>
                  <button
                    type="submit"
                    className="btn btn-primary btn-block"
                    style={{ backgroundColor: "teal", width: "100%" }}
                  >
                    Sign up
                  </button>
                  <p className="text-center mt-3" style={{ color: "black" }}>
                    Already have an account?{" "}
                    <Link to="/login" style={{ color: "teal" }}>
                      Sign in
                    </Link>
                  </p>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Signup;