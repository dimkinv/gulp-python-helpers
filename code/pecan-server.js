'use strict';

const process = require('process');
const spawn = require('child_process').spawn;
const path = require('path');

const stdout = process.stdout;
const stderr = process.stderr;
const serverPath = path.join(__dirname + '/server.py');

module.exports = (configPath, port)=> {
    let ps = spawn('python', [serverPath, configPath, port], {
       stdio: ['ignore', stdout, stderr]
    });


};