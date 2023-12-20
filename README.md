[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=GENERATE+PASSWORD)](https://github.com/komanch7/generatepassword)
---
### 🔥 My Stats :
[![GitHub Streak](https://github-readme-streak-stats.herokuapp.com/?user=komanch7&theme=dark&background=0d1117)](https://github.com/komanch7/generatepassword/pulse)


---
# generatepassword
Password Generator is a simple application that generates a random password. Skills will require a random number generator, working with strings, numbers, displaying, sequences.


## Documentation

[Documentation](https://github.com/komanch7/generatepassword/blob/main/README.md)


## Roadmap

- create_simple_numeric_password (create a simple numeric password)

- create_text_password (creating a text password lower - in lower case, upper - in upper case, mix - mixed mode)

- create_complex_password (create a complex password using mixed-case letters, numbers and special characters)

- create_hash_password (creating a password based on any existing hash function in python)


## Tech Stack

**Server:** Python 3.9^


## Usage/Examples

```python
# all imports

import create_simple_numeric_password
import create_text_password
import create_complex_password
import create_hash_password
```
## Function number 1
```python
# takes one parameter, reads the number

numericPass = create_simple_numeric_password(12)
print(numericPass)
```
- program response
```python
>> 268545026164
```
## Function number 1
```python
# takes one parameter, reads the string

numericPass = create_simple_numeric_password('12')
print(numericPass)
```
- program response
```python
>> 517370785526
```
## Function number 2
```python
# takes two parameters: 
#   1. the first is a number 
#   2. the second is a mode 
#       2.1. three modes ['lower', 'upper', 'mix'])

textPass = create_text_password(16, register='mix')
print(textPass)
```
- program response
```python
>> aPbBnmOlFAllcOPI
```
## Function number 3
```python
# takes one parameter
complexPass = create_complex_password(12)
print(complexPass)
```
- program response
```python
>> wO}s3idhzDc1
```
## Function number 4
```python
# takes two parameters:
#   1. the first is a number
#   2. the second is a mode
#       2.1. {'shake_128', 'md5', 'shake256', 'md5-sha1', 'sha512-256', 
#            'blake2s', 'sha512-224', 'sha3_512', 'sha3-256', 'sha384', 
#            'sha3-224', 'sha256', 'sha3_256', 'whirlpool', 'sha3_384', 
#            'sha1', 'shake128', 'sha3-512', 'md4', 'blake2b512', 'sha512', 
#            'sha224', 'sm3', 'ripemd160', 'blake2s256', 'sha3_224', 
#            'sha3-384', 'shake_256', 'blake2b'}

hashPass = create-hash-password('test', hash='sha256')
print(hashPass)
```
- program response
```python
>> 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
```

## 🚀 About Me
I'm a beginner in Python development. Thank you for your understanding and support.

## License

[MIT](https://github.com/komanch7/generatepassword/blob/main/LICENSE)