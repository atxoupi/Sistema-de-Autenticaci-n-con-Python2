import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

export const Navbar = () => {
  const { store, actions } = useContext(Context);
  const logout = () => {
    actions.logout();
  };
  return (
    <nav className="navbar navbar-light bg-light">
      <div className="container">
        <Link to="/">
          <span className="navbar-brand mb-0 h1">Login</span>
        </Link>

        {store.auth === true ? (
          <div className="ml-auto">
            <button className="btn btn-primary" onClick={logout}>
              logout
            </button>
          </div>
        ) : (
          <div className="ml-auto">
            <Link to="/">
              <button className="btn btn-primary">login</button>
            </Link>
          </div>
        )}
      </div>
    </nav>
  );
};
