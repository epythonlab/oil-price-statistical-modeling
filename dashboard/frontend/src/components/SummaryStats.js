// frontend/src/components/SummaryStats.js
import React from 'react';
import { Paper, Typography } from '@mui/material';

const SummaryStats = ({ prices }) => {
    const averagePrice = (prices.reduce((acc, curr) => acc + curr.Price, 0) / prices.length).toFixed(2);
    const maxPrice = Math.max(...prices.map(price => price.Price));
    const minPrice = Math.min(...prices.map(price => price.Price));

    return (
        <Paper style={{ padding: '20px', marginTop: '20px' }}>
            <Typography variant="h5">Summary Statistics</Typography>
            <Typography>Average Price: ${averagePrice}</Typography>
            <Typography>Maximum Price: ${maxPrice}</Typography>
            <Typography>Minimum Price: ${minPrice}</Typography>
        </Paper>
    );
};

export default SummaryStats;
