import { useState } from "react";
import { Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";


const Signup = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleEmailChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
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
        setMessage("Signup successful!");
      })
      .catch((error) => {
        console.error(error);
        setMessage("Signup failed. Please try again.");
      });
  };

  return (
    <section className="bg-light">
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-md-6">
            <div className="card">
              <div className="card-body">
                <h1 className="text-center mb-4">Create Account</h1>
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
                  <div className="form-group">
                    <label htmlFor="username">Your Username</label>
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
                  <div className="form-group">
                    <label htmlFor="email">Your Email</label>
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
                  <div className="form-group">
                    <label htmlFor="password">Password</label>
                    <input
                      type="password"
                      className="form-control"
                      id="password"
                      placeholder="••••••••"
                      required
                      value={password}
                      onChange={handlePasswordChange}
                    />
                  </div>
                  <button type="submit" className="btn btn-primary btn-block">
                    Sign up
                  </button>
                  <p className="text-center mt-3">
                    Already have an account? <Link to="/login">Log in</Link>
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

