import React from "react";
// import AboutBackground from "../Assets/about-background.png";
// import AboutBackgroundImage from "../Assets/about-background-image.png";
// import { BsFillPlayCircleFill } from "react-icons/bs";
import VancouverMap from '../assets/vancouver_map.png';
import RecyclePeople from '../assets/recycle-people.png';

const ImageDetection = () => {
  return (
    <div className="image-detection-container">
      {/* <div className="about-background-image-container">
        <img src={AboutBackground} alt="" />
      </div> */}
      <div className="image-detection-image-container">
        <img src={RecyclePeople} alt="" width={"100%"} />
      </div>
      <div className="image-detection-text-container">
        <p className="primary-subheading">Key feature</p>
        <h1 className="primary-heading">
          Image Detection
        </h1>
        <p className="primary-text">
          This project tackles urban waste management with cutting-edge AI. Advanced, open-source artificial intelligence allows for precise waste detection and tracking. 
        </p>
        <p className="primary-text">
          But the secret weapon? Data. The more data we feed the AI, the better it gets at identifying and tracking waste. Finally, by seamlessly plugging this AI into existing city infrastructure, we achieve scalability. 
          This lets us pinpoint overflowing bins with pinpoint accuracy, leading to a major boost in waste management efficiency.
        </p>
        <div className="image-detection-buttons-container">
          <button className="secondary-button">Upload</button>
        </div>
      </div>
    </div>
  );
};

export default ImageDetection;
