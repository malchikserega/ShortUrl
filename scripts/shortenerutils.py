import string
import random
import hashlib
import time

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits


def getalphabet():
    alphabet = list()
    alphabet.extend(LOWERCASE)
    alphabet.extend(UPPERCASE)
    alphabet.extend(DIGITS)
    return alphabet


def getmd5(url):
    m = hashlib.md5()
    m.update(url.encode())
    return m.hexdigest()


def getbinpartmd5(hashmd5):
    partmd5 = list()
    binhash = bin(int(hashmd5, 16))[2:]
    i = 1
    part = ''
    for char in binhash:
        if i < 7:
            part += char
            i += 1
        else:
            partmd5.append(part)
            i = 1
            part = ''

    return partmd5


def getshorturl(url):
    alphabet = getalphabet()
    shorturl = ''
    salt = random.randint(1, int(time.time()))
    hashmd5hex = getmd5(url=url + str(salt))
    parts = getbinpartmd5(hashmd5=hashmd5hex)
    i = 0
    while len(shorturl) < 6:
        try:
            shorturl += alphabet[int(parts[i], 2)]
            i += 1
        except:
            i += 1
            pass
    return shorturl
