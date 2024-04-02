import React, { useState } from "react";
import { Link } from "react-router-dom";

const CustomNav = ({ li }) => {
  const [window, setWindow] = useState(false);

  let openClose = () => {
    if (window === false) {
      setWindow(true);
    } else {
      setWindow(false);
    }
  };

  return (
    <nav className="navbar-menu" style={{ width: window === false ? 250 : 60 }}>
      <div className="burger" onClick={openClose}>
        <img src="img/menu.svg" alt="burger" />
      </div>
      <ul className="navbar__list">
        {li.map((item, index) => (
          <div className="navbar__li-box" key={index}>
            <Link to={item[2] || "/"} style={{ display: "flex", alignItems: "center" }}>
              <img  width="35" height="28"
                src={item[1]}
                alt={item[0]}
                // style attribute blow is used to adjust the img size for the open and closed window as needed.
                // style={{ paddingLeft: window === false ? 0 : 0 }}
              />
              <li
                className="navbar__li"
                style={{ display: window === false ? "inline-block" : "none" }}
              >
                {item[0]}
              </li>
            </Link>
          </div>
        ))}
      </ul>
    </nav>
  );
};

export default CustomNav;
