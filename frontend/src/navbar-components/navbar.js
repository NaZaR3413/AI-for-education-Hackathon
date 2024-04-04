import React, { useState } from "react";
import { Link } from "react-router-dom";

const CustomNav = ({ li }) => {
  // default window to closed 
  const [window, setWindow] = useState(true);

  // open the window if proper section is clicked, keep closed otherwise 
  let openClose = () => {
    if (window === false) {
      setWindow(true);
    } else {
      setWindow(false);
    }
  };

  return (
    <nav className="navbar-menu" style={{ width: window === false ? 250 : 60 }}> {/** sizes for an extended/closed window */}
      {/**the section that handles opening/closing of the window */}
      <div className="burger" onClick={openClose}> 
        <img src="img/menu.svg" alt="burger" />
      </div>

      <ul className="navbar__list">
        {li.map((item, index) => ( // start off by indexing through all of the names/locations inported through li in the app.js file
          <div className="navbar__li-box" key={index}>
            <Link to={item[2] || "/"} style={{ display: "flex", alignItems: "center" }}> {/**assign the proper link to the img and description */}
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
                {item[0]} {/**display the text description if the window is open, dont if not */}
              </li>
            </Link>
          </div>
        ))}
      </ul>
    </nav>
  );
};

export default CustomNav;
