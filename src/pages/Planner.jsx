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
  
    async function handleButtonClick() {
        try {
            let res = await fetch(`http://127.0.0.1:5000/get-popular-languages?q=chess`, {method: "POST", credentials: 'include', body: inputValue}); //change to store the value where we want it
            
            let resJson = await res.json();
            if (res.status === 200) {
                setInputValue(resJson);
            } else {
                setInputValue("Some error occured");
            }
        } catch (err) {
            console.log(err);
          }
            
        };
      //const storedInfo = localStorage.getItem("inputValue");

    return(
        <div className="App">
            <h1>Optimal Language</h1>
             {testData.map((item, idx) => (
                <ProgressBar
                   key={idx}
                   bgcolor={item.bgcolor}
                   completed={item.completed}
                />

             ))}
             <div className="App">
                 <p className='question'>Please enter a value:</p>
                 <input type="text" id = "inputValue" value = {inputValue} onChange={handleInputChange} className="title-q" />
                 <button onClick={handleButtonClick} className="title-button"> Store Value </button>

                 <h3>Final Value: {finalValue}</h3>
             </div>
           
        </div>
    
    );
}
export default Planner;
