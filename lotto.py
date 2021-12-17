
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
from random import *

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

numbers = sample(liste,6)

n = sorted (numbers)
t = str(n)
a = t.replace("[","")
b = a.replace("]","")

print (b)

urllib.urlopen('https://api.telegram.org/TELEGRAMBOT_TOKEN/sendMessage?chat_id=CHATID&text=' + b)