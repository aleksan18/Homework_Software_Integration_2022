const express =require('express');
const fs = require('fs');
const app = express();

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log(`Server is running on port`, PORT);
});
app.get("/txtRoute", (req, res) =>
{ 
    const txtData = JSON.parse(fs.readFileSync('birds.txt','utf8'));
    console.log("TXT");
    console.log(txtData);
    res.json({
        dataParsedType:"txt",
        fileData:txtData
    })

})
app.get("/jsonRoute", (req, res) =>
{ 
    const jsonData = JSON.parse(fs.readFileSync('birds.json','utf8'));
    console.log("JSON");
    console.log(jsonData);
    res.json({
        dataParsedType:"json",
        fileData:jsonData})

})