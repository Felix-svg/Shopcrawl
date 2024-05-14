const fetchdata = async () => {
    try {
        const response = await fetch('https://api.escuelajs.co/api/v1/products');
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Fetch error:', error);
        throw error; 
    }
};

export default fetchdata;
