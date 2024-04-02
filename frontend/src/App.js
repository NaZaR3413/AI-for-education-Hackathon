import React from "react";
import "./styles.scss";
import CustomNav from "./navbar-components/navbar.js";
import { Route, Routes } from "react-router-dom"
import Home from "./pages/home.js"

export default function App() {
  return (
    <CustomNav
      li={[
        ["Home", "img/dashboard.svg", "./pages/home"],
        ["Restautant’s", "img/restaurant.svg"],
        ["Manage User’s", "img/manage user.svg"],
        ["Manage Order’s", "img/manage  order.svg"],
        ["Manage Coupon’s", "img/manage coupon.svg"]
      ]}
    />
  );
}
