import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { Navigate } from "react-router-dom";

export const Private = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      {store.auth === false ? (
        <Navigate to="/" />
      ) : (
        <div className="container">
          <h1>
            Esta Página és privada pero puedes acceder porque estás logueado ​😉
          </h1>
        </div>
      )}
    </>
  );
};
