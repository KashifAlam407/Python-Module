##################################
from string import ascii_letters, punctuation   ## importing a specific methods
print(ascii_letters)  # Outputs all ASCII letters
print(punctuation)    # Outputs all punctuation characters


##################################
import string    ## importing all methods

#--------------- METHODS ---------------#
print(string.ascii_letters)   # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)  # '0123456789'
print(string.puctuation)  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.printable)  # a string containing all printable characters (digits, letters, punctuation, and whitespace)
print(string.whitespace)  # ' \t\n\r\x0b\x0c'

 

##############################################
import string

#---------------- FUNCTIONS ------------------#
s = "Md kashif alam"
print(string.capwords(s))  # it capitalize the first letter of each word

from string import Template
t = Template('Hello, $name!')
print(t.substitute(name="Alice"))  # 'Hello, Alice!'
t = Template("$Hello, name!")
print(t.substitute(Hello="Alice"))  # 'Alice, name!'




