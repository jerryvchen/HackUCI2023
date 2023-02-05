import React from 'react';
import ProgressBar from "../components/progress-bar"
import { useState, useEffect} from 'react';

const testData = [{ bgcolor: "#6a1b9a", completed: 69 }];



function Planner() 
{
    const [inputValue, setInputValue] = useState("");
  
    const [finalValue, setFinalValue] = useState("");

    const handleInputChange = (event) => {
      setInputValue(event.target.value);
      setFinalValue(event.target.value);
    };
  
    function handleButtonClick() {
      console.log("Value: ", inputValue); //change to store the value where we want it
      setInputValue("");
      //const storedInfo = localStorage.getItem("inputValue");
    };

    return(
        <div className="App">
            <h1>this is the planner</h1>
             {testData.map((item, idx) => (
                <ProgressBar
                   key={idx}
                   bgcolor={item.bgcolor}
                   completed={item.completed}
                />

             ))}
             <div className="App">
                 <p>Please enter a value:</p>
                 <input type="text" id = "inputValue" value = {inputValue} onChange={handleInputChange} />
                 <button onClick={handleButtonClick}> Store Value </button>

                 <h3>Final Value: {finalValue}</h3>
             </div>
           
        </div>
    
    );
}
export default Planner;
