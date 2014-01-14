import re


s = 'salut [[toto]], comment ca va [[titi]] dfkjsdkl j?'

# Replace [[URL]] to [URL](URL)
patternStr = ur'\[{2}([^\]]*)\]{2}'   # OR '\[\[([^\]]*)\]\]'  
repStr = ur'[\1](\1)'

print re.sub(patternStr, repStr, s)

# output : salut [toto](toto), comment ca va [titi](titi) dfkjsdkl j?
