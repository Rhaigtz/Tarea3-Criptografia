const RC4 = require('rc4.js');
var test = new RC4('key 123');

console.log(test.encrypt('text'));

console.log(test.decrypt('34d39eda'));
