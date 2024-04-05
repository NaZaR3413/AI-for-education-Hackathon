import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';

function Chart() {
    const [message, setMessage] = useState('');

    useEffect(() => {
      axios.get('http://localhost:5000/data')  // Adjust the URL/port as needed
        .then(response => {
          setMessage(response.data.message);
          alert(response.data.message); // This will display the message fetched from Flask
        })
        .catch(error => {
          console.error('There was an error fetching the data:', error);
        });
    }, []);

    // Sample data for Chart
    const data = [
        { name: 'Overall Skills', x: 80 },
        { name: 'Action Keywords', x: 77 },
        { name: 'Impact Keywords', x: 70 },
        { name: 'Job Match', x: 69 },
    ];

    return (
        <div>
            <p>Data from Flask: {message}</p> {/* Display the message from Flask */}
            <div>
                <RadarChart height={300} width={500} 
                    outerRadius="80%" data={data}>
                    <PolarGrid />
                    <PolarAngleAxis dataKey="name" />
                    <PolarRadiusAxis angle={30} domain={[0, 100]} tick={{ fill: 'black'}} />
                    <Radar name="Skills" dataKey="x" stroke="green"
                    fill="green" fillOpacity={0.6} />
                </RadarChart>
            </div>
        </div>
    );
}

export default Chart;
