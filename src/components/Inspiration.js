import React from "react";

const Inspiration = () => {
  const workInfoData = [
    {
      title: "Streamline Waste Inspection",
      text: "Replace manual inspection with a semi-automated system using open-source AI for image detection. This ensures consistent, reliable, and time-efficient waste condition assessment.",
    },
    {
      title: "Empower Informed Action",
      text: "Get insightful analysis of waste items, allowing users to make data-driven decisions for improved waste management.",
    },
    {
      title: "Foster Community Engagement",
      text: "Track waste disposal and participate in responsible waste management. Combining advanced technology with community involvement is key to achieving sustainbility.",
    },
  ];
  return (
    <div className="inspiration-section-wrapper">
      <div className="inspiration-section-top">
        <p className="primary-subheading">Inspiration</p>
        <h1 className="primary-heading">Our Goals</h1>
        <p className="primary-text">
        As urban populations continue to surge, the parallel challenge of ensuring efficient and sustainable waste management becomes increasingly crucial. 
        </p>
      </div>
      <div className="inspiration-section-bottom">
        {workInfoData.map((data) => (
          <div className="inspiration-section-info" key={data.title}>
            <h2>{data.title}</h2>
            <p>{data.text}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Inspiration;
