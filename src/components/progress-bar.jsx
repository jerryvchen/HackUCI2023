import React from "react";
const ProgressBar = (props) => {
  const { bgcolor, completed } = props;

  const containerStyles = {
    height: 25,
    width: '93%',
    backgroundColor: "#F9D3B4",
    borderRadius: 50,
    margin: 50
  }

  const fillerStyles = {
    height: '100%',
    width: `${completed}%`,
    borderRadius: 'inherit',
    textAlign: 'right',
    transition: 'width 1s ease-in-out',
  }

  const labelStyles = {
    padding: 10,
    color: '#F9D364',
    fontWeight: 'bold'
  }

  return (
    <div style={containerStyles}>
      <div style={fillerStyles}>
      </div>
    </div>
  );
};


export default ProgressBar;