// frontend/src/components/FilterPanel.js
import React, { useState } from 'react';
import { TextField, Button, Grid } from '@mui/material';

const FilterPanel = ({ fetchPrices }) => {
    const [start, setStart] = useState('');
    const [end, setEnd] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        fetchPrices(start, end);
    };

    return (
        <form onSubmit={handleSubmit}>
            <Grid container spacing={2}>
                <Grid item xs={6}>
                    <TextField
                        label="Start Date"
                        type="date"
                        value={start}
                        onChange={(e) => setStart(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid item xs={6}>
                    <TextField
                        label="End Date"
                        type="date"
                        value={end}
                        onChange={(e) => setEnd(e.target.value)}
                        fullWidth
                    />
                </Grid>
                <Grid item xs={12}>
                    <Button type="submit" variant="contained" color="primary">Filter</Button>
                </Grid>
            </Grid>
        </form>
    );
};

export default FilterPanel;
