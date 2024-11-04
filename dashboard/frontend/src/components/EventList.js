// frontend/src/components/EventList.js
import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const EventList = ({ events }) => {
    return (
        <div>
            <h2>Significant Events</h2>
            {events.map((event, index) => (
                <Card key={index} style={{ margin: '10px 0' }}>
                    <CardContent>
                        <Typography variant="h6">{event.event}</Typography>
                        <Typography color="textSecondary">{event.date}</Typography>
                    </CardContent>
                </Card>
            ))}
        </div>
    );
};

export default EventList;
