const express = require("express");
const cors = require("cors");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const jwt = require("jsonwebtoken");

const app = express();
app.use(express.json());

app.use(cors({
    origin: ["https://yourfrontend.com"],
    methods: "GET,POST",
    credentials: true
}));

app.use(helmet()); 

const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, // 15 minutes
    max: 100, // Max 100 requests per 15 mins
    message: "Too many requests, please try again later."
});
app.use(limiter);

const authenticate = (req, res, next) => {
    const token = req.headers.authorization?.split(" ")[1]; // Extract Bearer token
    if (!token) return res.status(401).json({ message: "Unauthorized" });

    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET || "your-secure-key");
        req.user = decoded;
        next();
    } catch (err) {
        return res.status(403).json({ message: "Invalid token" });
    }
};

app.get("/user-data", authenticate, (req, res) => {
    res.json({
        username: req.user.username,
        email: req.user.email,
        balance: "500 USD"
    });
});


app.listen(3000, () => console.log("Secure Server running on port 3000"));
