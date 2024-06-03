import React from "react";
import { MapContainer } from 'react-leaflet/MapContainer'
import { TileLayer } from 'react-leaflet/TileLayer'
import VancouverMap from '../assets/vancouver_map.png';
import RecycleMan from '../assets/recycle-man.png';
import RecyclePeople from '../assets/recycle-people.png';

const Home = () => {
    return (
      <div>
        <div className="home-banner-container">
          <div className="home-text-section">
            <h1 className="primary-heading">
              WasteWise
            </h1>
            <p className="primary-text">
              Identify and track the key components of urban waste to build greener, more sustainable cities.
            </p>
            {/* TODO: Link to Github, maybe video? */}
            <button className="secondary-button"> 
              Learn more
            </button>
          </div>
          <div className="home-image-section">
            <img src={VancouverMap} alt="" width="100%" height="100%" />

            {/* TODO: Map glitching - showing in multiple segments instead of one map */}
            {/* <MapContainer
            
            center={[49.2827, -123.1207]} // Coordinates of Vancouver
            dragging={false} // Disable dragging
            doubleClickZoom={false} // Disable double click zoom
            scrollWheelZoom={false} // Disable scroll wheel zoom
            touchZoom={false} // Disable touch zoom
            zoomControl={false} // Hide zoom control
            zoom={15}
            style={{ height: "400px", width: "100%" }}
          >
            <TileLayer
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
          </MapContainer> */}
          </div>
        </div>
      </div>
    );
  };
  
  export default Home;
  