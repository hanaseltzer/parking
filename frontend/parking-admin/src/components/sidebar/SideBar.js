
import React from 'react';
import './SideBar.css';
import users from './icons/users.svg'
import parking from './icons/parking.svg'
import home from './icons/home.svg'
import {Link} from 'react-router-dom'

const Sidebar = () => {
  return (
    <div className="sidebar">
      <Link className='sidebar-item' to="/">
        <img className='sidebar-icon' src={home} alt='users-icon' />
        <h5>Home</h5>
      </Link>
      <Link className='sidebar-item' to="/users">
        <img className='sidebar-icon' src={users} alt='users-icon' />
        <h5>users</h5>
      </Link>
      <Link className='sidebar-item' to="/parkinglots">
        <img className='sidebar-icon' src={parking} alt='users-icon' />
        <h5>parking lot</h5>
      </Link>
      <Link className='sidebar-item' to="/parkingspots">
        <img className='sidebar-icon' src={parking} alt='users-icon' />
        <h5>parking spots</h5>
      </Link>
    </div>
  );
};

export default Sidebar;
