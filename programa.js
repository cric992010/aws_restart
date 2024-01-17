const os = require('os');

console.log('informacion del sistema operativo');


console.log('informacion del sistema, ' + os.platform());
console.log('informacion del sistema operativo, ' + os.release());
console.log('Arquitectura ', os.arch());
console.log('CPUs', os.cpus());
console.log('Memory', os.freemem());

console.log('uptime', os.uptime() / 60 / 60);