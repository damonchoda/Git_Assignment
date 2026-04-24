const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// MongoDB connection
mongoose.connect("mongodb://127.0.0.1:27017/todoDB")
  .then(() => console.log("MongoDB connected"))
  .catch(err => console.log(err));

// Schema
const TodoSchema = new mongoose.Schema({
  itemName: String,
  itemDescription: String
});

const Todo = mongoose.model("Todo", TodoSchema);

// Route
app.post("/submittodoitem", async (req, res) => {
  const { itemName, itemDescription } = req.body;

  const newItem = new Todo({ itemName, itemDescription });
  await newItem.save();

  res.json({ message: "Item saved successfully" });
});

// Server
app.listen(5000, () => {
  console.log("Server running on port 5000");
});