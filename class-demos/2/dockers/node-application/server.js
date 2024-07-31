// Import the express module
const express = require('express');

// Create an instance of express
const app = express();

// Define a port number
const PORT = process.env.PORT || 3000;

// Define a /health route
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'OK' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
