//Authors : Aswath Muralidharan
// task
// Create a backend Express.js application (in ui/app.js) that runs on the default port and serves a page with text "Home" (no need for HTML for now). 
// A sidebar, HTML/CSS formatting, and summary of the purpose of the UI will be added to the home page later. 
// Submit changes to UI/app.js in a pull request when complete. 
// Name/date/status: 2018-1-4/assigned to Aswath.
const express = require('express')

const app = express()

app.get('/',(req,res) => res.send('Home'))

app.listen(3000,()=> console.log("App running on port:3000"))

