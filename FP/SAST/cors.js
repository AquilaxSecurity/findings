const express = require("express");
const cors = require("cors");

const app = express();
app.use(express.json());

const allowedOrigins = ["https://trusted.com"];

app.use(cors({
    origin: function (origin, callback) {
        if (!origin || allowedOrigins.includes(origin)) {
            callback(null, true);
        } else {
            callback(new Error("CORS Not Allowed"));
        }
    },
    methods: "GET,POST",
    credentials: false
}));

app.get("/user-data", (req, res) => {
    res.json({ username: "victim", email: "victim@victim.com", balance: "500 USD" });
});

app.listen(3000, () => console.log("Server running on port 3000"));
