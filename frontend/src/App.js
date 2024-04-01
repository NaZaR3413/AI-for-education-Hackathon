import React from "react";
import "./styles.scss";
import CustomNav from "./navbar-components/navbar.js";
import Home from "./pages/home.js"

export default function App() {
  return (
    <CustomNav
      li={[
        ["Dashboard", "img/dashboard.svg"],
        ["Restautant’s", "img/restaurant.svg"],
        ["Manage User’s", "img/manage user.svg"],
        ["Manage Order’s", "img/manage  order.svg"],
        ["Manage Coupon’s", "img/manage coupon.svg"]
      ]}
    />
  );
}
