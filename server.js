const express = require('express');
const app = express();
const port = 8000;
const host = 'localhost';
const path = require('path');
const fs = require('fs');
let userInput;

app.use(express.json()); 
app.use(express.urlencoded({extended: true})); 

app.use(express.static(__dirname+"/public"));

app.get("/",(req,res)=>{
    res.sendFile(__dirname+"/index.html");
});

app.post('/',(req,res)=>{
    userInput = req.body.userInput;
    console.log(userInput);
    res.redirect("/");
    data=JSON.stringify({user:userInput});
    fs.writeFile("userInput.json",data,err=>{
        if (err)
        {
            console.log("error");
        }
    })
});

app.get('/about',(req,res)=>{
    res.setHeader('Content-Type','application/json');
    data=JSON.stringify({user:userInput});
    res.end(data);
})

app.listen(port,(err)=>{
    console.log(err? "Something wrong lol":`Listening to http://${host}:${port}`);
});