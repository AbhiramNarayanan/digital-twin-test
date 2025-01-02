const express = require("express");
const bodyParser = require("body-parser");
const dataRoutes = require("./routes/data");

const app = express();
app.use(bodyParser.json());

app.use("/api/data", dataRoutes);

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
