import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
          <Link to="/" className="nav-text">Home</Link>
          <Link to="/planner" className="nav-text">Planner</Link>
    </nav>
  );
}

export default Navbar;