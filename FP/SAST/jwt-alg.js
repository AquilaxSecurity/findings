const express = require('express');
const jwt = require('jsonwebtoken');
const dotenv = require('dotenv');

dotenv.config();
const app = express();

app.use(express.json());

const JWT_SECRET = process.env.JWT_SECRET || "SuperSecretKey";

function generateToken(payload) {
    return jwt.sign(payload, JWT_SECRET, { algorithm: 'HS256', expiresIn: '1h' });
}

function verifyToken(req, res, next) {
    const token = req.headers.authorization?.split(" ")[1];

    if (!token) {
        return res.status(401).json({ message: "Unauthorized: No token provided" });
    }

    try {
        const decoded = jwt.verify(token, JWT_SECRET, { algorithms: ['HS256'] });

        req.user = decoded; // Attach user info to request
        next();
    } catch (err) {
        return res.status(403).json({ message: "Forbidden: Invalid token" });
    }
}

app.get('/protected', verifyToken, (req, res) => {
    res.json({ message: "Secure data", user: req.user });
});

app.post('/login', (req, res) => {
    const { username } = req.body;
    if (!username) return res.status(400).json({ message: "Username required" });

    const token = generateToken({ username });
    res.json({ token });
});

app.listen(3000, () => console.log("Server running on port 3000"));
