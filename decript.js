const rc4 = require('rc4-crypt');
var CryptoJS = require('crypto-js');

// Initialize encrypt/decrypt
// The keys need to match
let decrypt = rc4('key 123');
let encrypt = rc4('key 123');
// The data we're about to encrypt
let plainData = 'text';

// Actually encrypt the data
let ciphertext = encrypt(plainData);

console.log(ciphertext);

// Let's decrypt it again

const buffer = Buffer.from('34d39eda', 'hex');
console.log(buffer.toString('hex'));

let decrypted = decrypt(ciphertext);

console.log(decrypted.toString('hex'));

// function unpack(str) {
//   var bytes = [];
//   for (var i = 0; i < str.length; i++) {
//     var char = str.charCodeAt(i);
//     bytes.push(char >>> 8);
//     bytes.push(char & 0xff);
//   }
//   return bytes;
// }

// // Encrypt
// var ciphertext = CryptoJS.RC4.encrypt('text', 'secret key 123');
// console.log(ciphertext.toString(CryptoJS.format.Hex));
// // Decrypt
// var bytes = CryptoJS.RC4.decrypt(ciphertext, 'secret key 123');
// var originalText = bytes.toString();

// console.log(originalText); // 'my message'
