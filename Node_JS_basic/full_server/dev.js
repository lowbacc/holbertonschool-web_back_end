const { exec } = require('child_process');

const database = process.argv[2] || './database.csv';

const command = `npx nodemon full_server/server.js ${database}`;

exec(command, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`Stderr: ${stderr}`);
    return;
  }
  console.log(stdout);
});