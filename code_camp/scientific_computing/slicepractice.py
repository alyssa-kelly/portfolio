str = 'X-DSPAM-Confidence: 0.8475'
print(str)
zpos = str.find(' ')
print(zpos)

piece = str[zpos+1:]
print(piece)
print(type(piece))

value = float(piece)
print(value)
print(type(value))
