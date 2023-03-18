# Encryption-Algorithm

**Encryption Algorithm based on Bit Manipulation in Python3**

**Use this Easy to Use GitHub Repository to Converse in a Binary Encryption Format**

## Special Instruction for Shared Encryption-Decryption 
> If Encrypted Text is Shared with someone for Decryption, they must have the Code along with "Text.txt" file which is atomatically created while Encryption takes place

**Self-Explanatory Code with Ample amount of Comments**

## Installation
You can install the all requirements from **requirements.txt** by using pip.

    pip install -r requirements.txt


## Encryption-Decryption Algorithm : 

> Each Character {Letter (UpperCase or LowerCase) or Number or Special Character} is converted in it's ASCII Value (An Integer)...  

> ASCII Value is then converted into Binary Format (8 Digits is Confirmed by adding leading Zeros for Uniformity...  

> Random Key of Value 4-8 {Too Huge Key might result in Much Wierd Characters showing Up} is Selected FOR EACH CHARACTER  

> Now, First 4 (Index 0-3) Binary Nos. will be same... If Key is say 6... Then Nos. 5 (index 4-5) will be Same & Rest (Index 6-8) will be Swapped as... 0 is Replaced with 1 & 1 with 0...  

> Now, Modified Binary is Converted back into ASCII & then to Characters  

> Finally, the String is Reversed & Outputted & Copied to the ClipBoard...  

> Key is stored in Special Character Format and also Reversed Safely Stored inside a text File in Binary Format  

Running the Code 2 Times cannot have the Same Output because of Different Key for Each Character in String EveryTime that too Randomly Generated but Output is the Same...

### Reverse is Done in Decryption ;-)
