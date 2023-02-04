import fs from 'fs'

fs.appendFile('my_file.txt', 'File is created Node.js', (err) => {
    if (err) throw  err
    console.log("File is saved!")
})