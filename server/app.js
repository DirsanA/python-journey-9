import express from "express";
import axios from "axios";

const app = express();
const port = 4000;

const url = "https://api.chapa.co/v1/banks";
const headers = {
  Authorization: "Bearer CHASECK_TEST-JtDJOY9dPwM3dg2fxpaucz0uJKFDeRv1",
};

app.get("/banks", async (req, res) => {
  try {
    const response = await axios.get(url, { headers });
    const banks = response.data.data;
    console.log(banks);
    const banksName = banks.map(function (bank) {
      return bank.name;
    });
    return res.send(banksName);
  } catch (error) {
    console.error(error.response?.data || error.message);
    res.status(500).send("Error fetching banks from Chapa API");
  }
});

app.listen(port, () => {
  console.log(`The server is listening at port ${port}`);
});
