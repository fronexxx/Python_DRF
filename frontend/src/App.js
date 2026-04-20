import React, {useEffect, useState} from 'react';


const App = () => {
    const [pizzas, setPizzas] = useState([]);
    useEffect(() => {
        fetch('/api/pizzas')
            .then((response) => response.json())
            .then(data => setPizzas(data.data));
    }, []);
    return (
        <div>
            {
                pizzas.map(pizza => <div key={pizza.id}>{JSON.stringify({pizza})}</div>)
            }
        </div>
    );
};

export default App;