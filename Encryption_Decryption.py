"""
Encryption Algo :

-> Each Character {Letter (UpperCase or LowerCase) or Number or Spl. Char.} is converted in it's ASCII Value (An Integer)...
-> ASCII Value is then converted into Binary Format (8 Digits is Confirmed by adding leading Zeros for Uniformity...
-> Random Key of Value 4-8 {Too Huge Key might result in Much Wierd Characters showing Up} is Selected FOR EACH CHARACTER
-> Now, First 4 (Index 0-3) Binary Nos. will be same... If Key is say 6... Then Nos. 5 (index 4-5) will be Same & Rest (Index 6-8) will be Swapped as... 0 is Replaced with 1 & 1 with 0...
-> Now, Modified Binary is Converted back into ASCII & then to Characters
-> Finally, the String is Reversed & Outputted & Copied to the ClipBoard...

-> Key is Safely Stored inside a text File in Binary Format

Running the Code 2 Times can Never have the Same Output because of Different Key for Each Character in String EveryTime that too Randomly Generated but Output is the Same...

Reverse is Done in Decryption ;-)
"""

import pyperclip                    # For Copy to ClipBoard
from termcolor import colored       # For Stylish Heading
from pyfiglet import figlet_format  # For Stylish Heading
import time                         # For End of Terminal Extra Time
import random                       # For Random Key
import pickle                       # For Sending text to Text File in Binary Format

# Converting Binary to Decimal
def Dec2Bin(a):
    # a : DECIMAL int
    # Output : BINARY int
    b = 0
    x = []
    y = []
    z = []
    while a > 1:
        b = a % 2
        x.append(b)
        a //= 2
    x.append(a)

    for i in range((len(x) - 1), -1, -1):
        y.append(x[i])

    for i in range(8 - len(y)):
        z.append(0)

    for i in y:
        z.append(i)

    # print(z)       # Debugging Statement
    return z


# Converting Binary to Decimal
def Bin2Dec(a):
    # a : BINARY int
    # Output : DECIMAL int
    b = str(a)
    c = 0
    count = 0

    for i in range((len(b) - 1), -1, -1):
        c += int(b[i]) * 2 ** count
        count += 1

    # print(c)       # Debugging Statement
    return c


# Encrypting Algo
def Encrypt(a):
    # Encrypting String 'a'
    b = []
    c = []
    d = []
    e = []
    key = []
    en = ''
    en1 = ''
    en_2 = ''
    count = 0
    x = ''
    for i in a:
        b.append(ord(i))

    for i in b:
        c.append(Dec2Bin(i))

    for i in c:
        d = []
        k = random.randrange(4, 9, 1)
        n = ['', '', '', '', '{', ']', '|', '`', '/']
        key.append(n[k])
        for j in range(4) :
            d.append(i[j])
        for j in range(4, k):
            d.append(i[j])
        for j in range(k, 8, 1):
            if i[j] == 0:
                d.append(1)
            elif i[j] == 1:
                d.append(0)
        e.append(d)

    #print(c)       # Debugging Statement
    #print(key)     # Debugging Statement
    #print(e)       # Debugging Statement

    for i in e :
        x = ''
        for j in i :
            x += str(j)
            x = x.lstrip('0')
        en += chr(Bin2Dec(int(x)))
        count += 1

    for i in range((len(key) - 1), -1, -1) :
        en1 += key[i]

    try :
        f = open("Text.txt", 'x')
        f.close()
    except :
        pass

    with open("Text.txt", 'wb') as f :
         pickle.dump(en1, f)

    for i in range((len(en) - 1), -1, -1) :
        en_2 += str(en[i])

    print(en_2)
    #print(en1)     # Debugging Statement
    pyperclip.copy(en_2)


def Decrypt(a) :
    n = ['', '', '', '', '{', ']', '|', '`', '/']
    key = ''
    key_1 = ''
    key_2 = ''
    b = []
    c = []
    d = []
    e = []
    count = 0
    x = 0
    y = ''
    z = ''
    a_1 = ''

    for i in range((len(a) - 1), -1, -1) :
        a_1 += str(a[i])

    with open("Text.txt", "rb") as f :
        key_1 = pickle.load(f)

    #print(key_1)       # Debugging Statement

    for i in key_1 :
        key_2 += str(n.index(i))

    for i in range((len(key_2) - 1), -1, -1) :
        key += key_2[i]

    for i in a_1 :
        b.append(Dec2Bin(ord(i)))

    #print(key)     # Debugging Statement
    #print(b)       # Debugging Statement

    for i in b :
        c = []
        count = 0
        while count < int(key[x]) :
            c.append(i[count])
            count += 1
        while count < 8 :
            if i[count] == 0 :
                c.append(1)
            elif i[count] == 1 :
                c.append(0)
            count += 1
        d.append(c)
        x += 1

    #print(d)       # Debugging Statement

    for i in d :
        y = ''
        for j in i :
            y += str(j)
        y = y.lstrip('0')
        z += chr(Bin2Dec(y))
        e.append(z)


    print(z)
    pyperclip.copy(z)

    #print(e)       # Debugging Statement
    #print(b)       # Debugging Statement
    #print(key)     # Debugging Statement
    #print(d)       # Debugging Statement
    #print(key_1)   # Debugging Statement


# Stylised Font
f = figlet_format("[ - -  E N C R Y P T I O N   2 . 0 - - ]", font="slant", width = 1000)
print(colored(f, "green"), end="\n\n\n")

# User-based Choice
choice = input("Enter What Do You Wanna Do (1 for Encrypt/ 2 for Decrypt) ? ")

if choice == "1" :
    a = input("Enter String to be Encrypted : ")
    Encrypt(a)

elif choice == "2" :
    a = input("Enter String to be Decrypted : ")
    Decrypt(a)

else :
    print("Please Recheck Options")

time.sleep(100)  # So that terminal doesn't crash if opened by double clicking before the User has Read the Output