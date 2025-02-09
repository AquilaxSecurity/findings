const express = require('express');
const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');

dotenv.config();

const app = express();
app.use(express.json());

const secretKey = process.env.JWT_SECRET;
if (!secretKey) {
    console.error("Missing JWT_SECRET in environment variables!");
    process.exit(1);
}

const verifyToken = (req, res, next) => {
  const token = req.headers.authorization?.split(" ")[1];

  if (!token) {
    return res.status(401).json({ message: 'Unauthorized: No token provided' });
  }

  try {
    const decoded = jwt.verify(token, secretKey); 
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(403).json({ message: 'Invalid token' });
  }
};

app.get('/admin', verifyToken, (req, res) => {
  if (req.user.role !== 'admin') { 
    return res.status(403).json({ message: 'Unauthorized access' });
  }
  res.status(200).json({ message: 'Admin access granted' });
});

app.post('/generate-token', (req, res) => {
  const { username, role } = req.body;

  if (!username || !role) {
    return res.status(400).json({ message: 'Username and role required' });
  }

  const payload = { username, role };
  const token = jwt.sign(payload, secretKey, { expiresIn: '1h' });

  res.status(200).json({ token });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Secure Server running on port ${PORT}`));
