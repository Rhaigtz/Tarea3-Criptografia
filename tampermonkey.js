// ==UserScript==
// @name         TareaCripto 3
// @namespace    http://tampermonkey.net/
// @include      file:///C:/Users/Nicolas/Desktop/Development/Tarea3Cripto/helloworld.html
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.tampermonkey.net/index.php?version=4.11&ext=dhdg&updated=true
// @grant        none

// ==/UserScript==

(function () {
  "use strict";
  let privateKey = "";
  function RC4(key) {
    privateKey = keySetup(key);
  }

  /**
   * Converts the text into an array of the characters numeric Unicode values
   * @param  {String} text, the text to convert
   * @return {Array} the array of Unicode values
   */
  function convert(text) {
    var codes = [];

    for (var i = 0, ii = text.length; i < ii; i++) {
      codes.push(text.charCodeAt(i));
    }

    return codes;
  }

  /**
   * Sets up the key to use with the byte stream
   * @param  {String} key, The key that you want to use
   * @return {Array}, the key stream which with be used in the byteStreamGenerator
   */
  function keySetup(key) {
    var K = [...Array(256).keys()],
      j = 0,
      key = convert(key);

    for (var i = 0, ii = K.length; i < ii; i++) {
      j = (j + K[i] + key[i % key.length]) % 256;
      [K[i], K[j]] = [K[j], K[i]];
    }

    return K;
  }

  /**
   * byteStreamGenerator uses ES6 generators which will be 'XOR-ed' to encrypt and decrypt
   * @param {Array} K, the array generated from the keySetup
   * @yield {Integer}, the current value which will be 'XOR-ed' to encrypt or decrypt
   */
  var byteStreamGenerator = function* (K) {
    var i = 0,
      j = 0;

    while (true) {
      i = (i + 1) % 256;
      j = (j + K[i]) % 256;
      [K[i], K[j]] = [K[j], K[i]];
      yield K[(K[i] + K[j]) % 256];
    }
  };

  /**
   * Decrypts the input text
   * @param  {String} input, the text to decrypt
   * @return {String}, the decrypted text (if the same key was used)
   */
  function decrypt(input) {
    var outputText = "",
      byteStream = byteStreamGenerator(privateKey.slice(0));

    input = input.match(/[a-z0-9]{2}/gi);

    for (var i = 0, ii = input.length; i < ii; i++) {
      outputText += String.fromCharCode(
        parseInt(input[i], 16) ^ byteStream.next().value
      );
    }

    return outputText;
  }

  new RC4("key 123");
  let encryptedTag = document.getElementsByTagName("div")[0];

  console.log(encryptedTag);

  const decryptedText = decrypt(encryptedTag.id).toString();

  console.log(decryptedText);

  encryptedTag.innerHTML += decryptedText;
})();
