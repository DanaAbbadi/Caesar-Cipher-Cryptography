# Caesar Cipher Cryptography

## Problem Domain:

Devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

The encryption process will follow the Ceasar Cipher technique, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. 

![img](https://media.geeksforgeeks.org/wp-content/uploads/ceaserCipher.png)

## Functionalties

* encrypt(msg, key) - Function that takes in a plain text phrase and a numeric key and encrypts it useng ceasar cipher with the shift equals to key. The plain text can be anything in english letters, function will return encrypted lowercased text with the original punctuation marks and spaces
  
* decrypt(msg, key) - Function that takes in encrypted text and numeric key which will restore the encrypted text back to its original form as long as correct key is supplied.
  
* cipher_breaker(msg) - Function to decrypt a cipher without having an access to the key.

## Technologies and packages:

* Python3
* Pytest
* nltk: Natural Language Tool Kit


