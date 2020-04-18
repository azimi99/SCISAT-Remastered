//jshint esversion:6

const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const querystring = require('querystring');
const app = express();
//q4QbxT9vVV5WW6DO
mongoose.connect("mongodb+srv://admin:q4QbxT9vVV5WW6DO@cluster0-hc4da.mongodb.net/testDB", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useFindAndModify: false
});

testSchema = {
  name: String,
  description: String
};

pointSchema = {
  x: Number,
  y: Number
};

const Test = mongoose.model("Test", testSchema);
const Point = mongoose.model("Point", pointSchema);

app.use(bodyParser.urlencoded({
  extended: true
}));

app.route("/").get(function(req, res) {
  res.send("Archit and Haren use /api route");
});

app.route("/api/:paramName")
  .get(function(req, res) {
    const queryObject = req.query;
    const q = queryObject.q;
    const collection = req.params.paramName;
    if (collection === "points") {
      Point.find({}, (err, foundItems) => {
        if(err){
          res.send(err);
        } else {
          res.send(foundItems);
        }
      });
    } else if(collection==="tests") {
      console.log(q);
      Test.find({name: q}, (err, foundItems) => {
        if(err){
          res.send(err);
        } else {
          res.send(foundItems);
        }
      });
    }




  });

let port = process.env.PORT;
if (port == null || port == ""){
  port = 3000;
}

app.listen(port, function(){
  console.log("Server started on port "+port);
});
