import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { IoMdEyeOff, IoMdEye } from "react-icons/io";
import "bootstrap/dist/css/bootstrap.min.css";

const Login = ({ onLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);
  const [message, setMessage] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const navigate = useNavigate();

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleRememberMeChange = () => {
    setRememberMe(!rememberMe);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("https://shopcrawl-cjfb.onrender.com/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password, rememberMe }),
    })
      .then((resp) => {
        if (!resp.ok) {
          throw new Error("Login failed");
        }
        return resp.json();
      })
      .then((data) => {
        if (data.access_token) {
          localStorage.setItem("access_token", data.access_token);
          setMessage("Login successful!");
          setPassword("");
          setEmail("");
          onLogin(data.access_token);
          navigate("/search");
        } else {
          throw new Error("Token not found in response");
        }
      })
      .catch((error) => {
        console.error(error);
        setMessage("Login failed. Please try again.");
      });
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <section
      className="d-flex justify-content-center align-items-center"
      style={{
        backgroundColor:"#90AEAD",
        minHeight: "100vh",
        position: "relative",
      }}
    >
      <div
        className="position-absolute w-100 h-100"
      ></div>
      <div className="container py-5">
        <div className="row justify-content-center">
          <div className="col-lg-6 col-md-8 col-sm-10">
            <div className="card border" >
              <div className="card-body">
                <h1 className="text-center mb-4" style={{ color: "teal" }}>
                  Welcome Back
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
                      htmlFor="email"
                      className="form-label"
                      style={{ color: "teal" }}
                    >
                      Your email
                    </label>
                    <input
                      type="email"
                      name="email"
                      id="email"
                      className="form-control"
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
                        name="password"
                        id="password"
                        placeholder="••••••••"
                        className="form-control"
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
                  <div className="form-check mb-3">
                    <input
                      type="checkbox"
                      className="form-check-input"
                      id="rememberMe"
                      checked={rememberMe}
                      onChange={handleRememberMeChange}
                    />
                    <label
                      className="form-check-label"
                      htmlFor="rememberMe"
                      style={{ color: "teal" }}
                    >
                      Remember Me
                    </label>
                  </div>
                  <div className="d-grid">
                    <button
                      type="submit"
                      className="btn btn-primary"
                      style={{ backgroundColor: "teal" }}
                    >
                      Sign in
                    </button>
                  </div>
                  <div className="text-center mt-3">
                    <Link to="/forgot-password" style={{ color: "teal" }}>
                      Forgot Password?
                    </Link>
                  </div>
                  <p className="text-center mt-3" style={{ color: "black" }}>
                    Don’t have an account yet?{" "}
                    <Link to="/signup" style={{ color: "teal" }}>
                      Sign up
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

export default Login;