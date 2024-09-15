import React from 'react';
import Searchbar from './searchbar/Searchbar'
import UsersData from './usersdata/UsersData';

const Users = () => {
  return (
    <div className='content'>
      <h2 className='content-header'>Users View</h2>
      <Searchbar/>
      <UsersData/>
    </div>
  );
};

export default Users;