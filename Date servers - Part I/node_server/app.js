const express =require('express');
const app = express();

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
    console.log(`Server is running on port`, PORT);
});

app.get('/timestamp', (req, res) => {
    return res.json({timestamp: new Date().toISOString(),format: 'ISO8601'});
})