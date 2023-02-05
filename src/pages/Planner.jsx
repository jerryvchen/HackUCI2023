import React from 'react';
import ProgressBar from "../components/progress-bar"
import { useState, useEffect} from 'react';

const testData = [{ bgcolor: "#6a1b9a", completed: 69 }];

function Planner() {
    return (
        <div className="App">
            <h1>this is the planner</h1>
             {testData.map((item, idx) => (
        <ProgressBar
          key={idx}
          bgcolor={item.bgcolor}
          completed={item.completed}
        />
      ))}
    </div>
    );
}
export default Planner;
