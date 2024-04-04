import { Radar, RadarChart, PolarGrid, 
    PolarAngleAxis, PolarRadiusAxis } from 'recharts';

    const Chart = () => {
 
        // Sample data
        const data = [
            { name: 'Overall Skills', x: 4 * 20},
            { name: 'Action Keywords', x: 77 },
            { name: 'Impact Keywords', x: 70 },
            { name: 'Job Match', x: 69 },
        ];
     
        return (
            <div>
                <div className='radar-text'>
                    {/**text representation */}
                    <p>
                        text for radar chart
                    </p>
                </div>
                <div>
                    <RadarChart height={300} width={500} 
                        outerRadius="80%" data={data}>
                        <PolarGrid />
                        <PolarAngleAxis dataKey="name" />
                        <PolarRadiusAxis />
                        <Radar dataKey="x" stroke="green"
                        fill="green" fillOpacity={0.5} />
                    </RadarChart>
                </div>
                
            </div>
        );
    }
     
    export default Chart;