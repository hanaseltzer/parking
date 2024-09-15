import React, { useEffect, useState } from 'react';
import './Searchbar.css';
import search from './search.svg';

const Searchbar = () => {
  const [expanded, setExpanded] = useState(false);

  useEffect(() => {
    // Trigger the animation after the component mounts
    setTimeout(() => {
      setExpanded(true);
    }, 100);  // Small delay before starting the animation
  }, []);

  return (
    <div className={`searchbar-input ${expanded ? 'expanded' : ''}`}>
      <input type='text' />
      <button className='search-button'>
        <img src={search} className='search-img' alt="Search" />
      </button>
    </div>
  );
};

export default Searchbar;
