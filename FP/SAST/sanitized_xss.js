const express = require('express');
const csrf = require('csurf'); // Import CSRF middleware
const cookieParser = require('cookie-parser');

const app = express();
app.use(cookieParser());
app.use(csrf({ cookie: true })); // Enable CSRF protection

app.get('/', (req, res) => {
  const name = req.query.name || "Guest"; // Default value to avoid null/undefined
  const sanitized = name.replace(/</g, "&lt;").replace(/>/g, "&gt;");
  
  // Example of using CSRF token in the response
  res.cookie('XSRF-TOKEN', req.csrfToken());
  res.send(`<h1>Hello ${sanitized}</h1>`);
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
