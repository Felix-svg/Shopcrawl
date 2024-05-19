import { Link } from "react-router-dom";

const LandingPage = () => {
  return (
    <div className="container mt-5">
      <div className="row">
        <div className="col-md-6 d-flex flex-column justify-content-center">
          <h1>Welcome to Shopcrawl</h1>
          <p className="lead">Sign in or create an account to start comparing prices!</p>
          <div className="d-flex justify-content-center">
            <Link to="/login" className="btn btn-primary me-2">Sign In</Link>
            <Link to="/signup" className="btn btn-outline-primary">Create Account</Link>
          </div>
          <div className="mt-4"> {/* Add margin top */}
            <p className="lead">Or explore a range of available products</p>
            <Link to="/products" className="btn btn-outline-primary d-flex justify-content-center">Explore</Link>
          </div>
        </div>
        <div className="col-md-6">
          <img src="https://img.freepik.com/premium-vector/yong-man-woman-shopping-flat-desin-concept-ready-animation-characters-design-elements-with-shopping-bags-boxes_171919-216.jpg?w=2000" className="img-fluid" alt="Welcome" />
        </div>
      </div>
    </div>
  );
};

export default LandingPage;
