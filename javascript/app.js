const express = require('express');
const app = express();

app.get('/hello', (req, res) => {
  const htmlResponse = '<html><body><h1>Hello, World!</h1></body></html>';
  res.send(htmlResponse);
});

app.get('/random', (req, res) => {
  const randomData = {
    data: Math.random(),
    timestamp: new Date()
  };
  res.json(randomData);
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});