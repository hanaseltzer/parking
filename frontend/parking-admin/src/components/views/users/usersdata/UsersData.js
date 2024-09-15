import React, { useState, useEffect } from 'react';
import './UsersData.css';

function parkingLots(parkings) {
  if (parkings) {
    return <button>Parking Lots</button>;
  }
  return null; // Return null if there are no parking spots
}

const UsersData = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch data from the API
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/get_users_data');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        setData(result); // Set the fetched data to state
        setLoading(false); // Set loading to false after data is fetched
      } catch (error) {
        setError(error);
        setLoading(false);
      }
    };

    fetchData();
  }, []); // Empty dependency array to run this effect only once (on mount)

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div className='content'>
      <table className="user-table">
        <thead>
          <tr>
            <th>Username</th>
            <th>Phone Number</th>
            <th>Parking Spots</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.full_name}</td>
              <td>{item.phone_number}</td>
              <td>{parkingLots(item.parking_spots)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UsersData;
