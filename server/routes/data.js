const express = require("express");
const { exec } = require("child_process");

const router = express.Router();

router.get("/", (req, res) => {
    exec("python ../omniverse/src/data_simulator.py", (error, stdout, stderr) => {
        if (error) {
            return res.status(500).send(stderr);
        }
        res.send(stdout);
    });
});

module.exports = router;
