
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './components/views/home/Home'
import Users from './components/views/users/Users'
import ParkingLots from './components/views/parkingLots/ParkingLots'
import ParkingSpots from './components/views/parkingSpots/ParkingSpots';
import Sidebar from './components/sidebar/SideBar'
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>parking managment</h1>
      </header>
      <body>
         <BrowserRouter>
          <Sidebar/>
          <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/users" element={<Users/>}/>
            <Route path="/parkinglots" element={<ParkingLots/>}/>
            <Route path="/parkingspots" element={<ParkingSpots/>}/>
          </Routes>
        </BrowserRouter>
      </body>
    </div>
  );
}

export default App;