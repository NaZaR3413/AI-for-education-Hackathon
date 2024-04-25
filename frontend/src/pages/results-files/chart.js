import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';

function Chart() {
    const [numbers, setNumbers] = useState([]); // State to store the list of numbers

    useEffect(() => {
        axios.get('http://localhost:5001/data') // Adjust the URL/port as needed
            .then(response => {
                setNumbers(response.data); // Set the fetched numbers to state
;            })
            .catch(error => {
                console.error('There was an error fetching the data:', error);
            });
    }, []);

    // Sample data for Chart
    const data = [
        { name: 'Overall Skills', x: numbers[0] * 10 },
        { name: 'Experience Match', x: numbers[1] },
        { name: 'Impact Keywords', x: numbers[2] },
        { name: 'Job Responsibilities', x: numbers[3] },
        { name: 'Job Summary', x: numbers[4] },
    ];

    return (
        <div>
            {/* Display the message from Flask <p>Data from Flask: {numbers}</p> */}
            <div>
                <RadarChart height={400} width={600} 
                    outerRadius="80%" data={data}>
                    <PolarGrid />
                    <PolarAngleAxis dataKey="name" />
                    <PolarRadiusAxis angle={0} domain={[0, 100]} tick={{ fill: 'black'}} />
                    <Radar name="Skills" dataKey="x" stroke="green"
                    fill="green" fillOpacity={0.6} />
                </RadarChart>
            </div>
        </div>
    );
}

export default Chart;
