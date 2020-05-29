const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
    res.json("Home page - city guide");
  });

app.get("/cityguide", (req, res) => {
    res.json("Welcome to Paris");
  });

app.listen(PORT, () => {
    console.log(`Listening on PORT: ${PORT}`);
})
