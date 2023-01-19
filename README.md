# Random-Password-Gen
This is a mini project created to test my knowledge on python.
**This project is meant to showcase and test my skills in python and you are advised not to clone this repository due to possible import issues. If you wish to copy the code, please just copy the exact file and add it to your system**

## Basic usage
```py
import password

password_gen = password.RandomPasswordGen()
password_gen.generate(length=10) # generate a password that contains alphabets, numbers and symbols of 10 letters

password_gen.generate(exclude_symbols=True) # exclude whatever type of letters you do not want to contain

password_gen.regenerate() # regenerate a new password using the most recent arguments you have used before this
```
