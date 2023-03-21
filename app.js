const express=require('express');
const bodyParser=require('body-parser');
const path = require('path');
const mongoose=require('mongoose')
const ejs=require('ejs')
const app=express();
console.log(__dirname)
app.use(bodyParser.urlencoded({extended:true}));
app.set('views','./views')
app.set('view engine','ejs')
//static files
app.use(express.static('public'))


app.get('/',(req,res)=>{
  res.render('index',{ text:  'this is ejs'})
})
app.get('/reg',(req,res)=>{
  res.render('reg',{ text:  'this is ejs'})
})
app.post("/",(req,res)=>{
  var first=req.body.fname;
  var last=req.body.lname;
  var email=req.body.email;
  console.log(`${first},${last},${email}`)
})
https://app.wotnot.io/bot-preview/68sRweX8o5rX032139084896TB578Zmw
app.listen(3000,()=>{
  console.log("running on port 3000");
})
