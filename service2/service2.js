const express = require('express');
const os = require('os');
const { execSync } = require('child_process');

const app = express();
const PORT = 5000;

function getIpAddress() {
  const interfaces = os.networkInterfaces();
  for (let iface of Object.values(interfaces)) {
    for (let details of iface) {
      if (details.family === 'IPv4' && !details.internal) {
        return details.address;
      }
    }
  }
  return 'IP not found';
}

function getRunningProcesses() {
  return execSync('ps -ax').toString();
}

function getDiskSpace() {
  return execSync('df -h /').toString();
}

function getUptime() {
  return execSync('uptime -p').toString();
}

app.get('/', (req, res) => {
  const service2Info = {
    Service2: {
      ip_address: getIpAddress(),
      running_processes: getRunningProcesses(),
      disk_space: getDiskSpace(),
      uptime: getUptime(),
    }
  };
  res.json(service2Info);
});

app.listen(PORT, () => {
  console.log(`Service2 is running on port ${PORT}`);
});
