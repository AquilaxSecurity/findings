const express = require("express");
const cors = require("cors");

const app = express();
app.use(express.json());

app.use(cors({
    origin: "*",  
    methods: "GET,POST,PUT,DELETE", 
    credentials: true 
}));

app.get("/user-data", (req, res) => {
    res.json({ username: "victim", email: "victim@victim.com", balance: "500 USD" });
});

app.listen(3000, () => console.log("Server running on port 3000"));
