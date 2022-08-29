const fs = require('fs');
const yaml = require('js-yaml');
try{
    const txtData = fs.readFileSync('birds.txt','utf8');
    console.log("TXT");
    console.log(txtData);
    const jsonData = JSON.parse(fs.readFileSync('birds.json','utf8'));
    console.log("JSON");
    console.log(jsonData);
    console.log('yaml')
    const yamlData = yaml.load(fs.readFileSync('birds.yaml','utf8'));
    console.log(yamlData)
    console.log('xml')
    const xmlData = fs.readFileSync('birds.xml','utf8')
    console.log(xmlData)
    console.log('csv')
    const csvData = fs.readFileSync('birds.csv','utf8')
    console.log(csvData)
} catch(e){
    console.log(e);
}

