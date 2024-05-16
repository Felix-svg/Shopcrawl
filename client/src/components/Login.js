import React, { useState } from "react";
import { Link } from "react-router-dom";
import { IoMdEyeOff, IoMdEye } from "react-icons/io";
import "bootstrap/dist/css/bootstrap.min.css";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);
  const [message, setMessage] = useState("");
  const [showPassword, setShowPassword] = useState(false);

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
    fetch("http://127.0.0.1:5000/login", {
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
      .then(() => {
        setMessage("Login successful!");
        setPassword("");
        setEmail("");
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
      className="bg-gray-50"
      style={{
        backgroundImage: `url("https://images.unsplash.com/photo-1714918161431-1bbafd741557?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHw0NHx8fGVufDB8fHx8fA%3D%3D")`,
        backgroundPosition: "center",
        backgroundSize: "cover",
        backgroundRepeat: "no-repeat",
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        position: "relative",
      }}
    >
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
          backgroundColor: "rgba(0, 0, 0, 0.3)",
        }}
      ></div>
      <div className="container py-8">
        <div className="row justify-content-center">
          <div className="col-lg-6">
            <div className="card border-primary" style={{ backgroundColor: "lavender" }}>
              <div className="card-body">
                <h1 className="text-center mb-4" style={{ color: "teal" }}>Welcome Back</h1>
                {message && (
                  <p
                    className={`text-center text-sm ${
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
                    <label htmlFor="email" className="form-label" style={{ color: "teal" }}>
                      Your email
                    </label>
                    <input
                      type="text"
                      name="email"
                      id="email"
                      className="form-control"
                      placeholder="Username"
                      required
                      value={email}
                      onChange={handleEmailChange}
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="password" className="form-label" style={{ color: "teal" }}>
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
                  <div className="mb-3 d-flex justify-content-between align-items-center">
                    <div className="form-check">
                      <input
                        type="checkbox"
                        className="form-check-input"
                        id="rememberMe"
                        checked={rememberMe}
                        onChange={handleRememberMeChange}
                        style={{ backgroundColor: rememberMe ? "teal" : "transparent" }}
                      />
                      <label className="form-check-label" htmlFor="rememberMe" style={{ color: "teal" }}>
                        Remember Me
                      </label>
                    </div>
                    <Link to="/forgot-password" style={{ color: "teal" }}>
                      Forgot Password?
                    </Link>
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
