fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    if fname == "na na boo boo":
        print('UNACCEPTABLE')
    else:
        print('File cannot be opened: ', fname)
    exit()

count = 0
total = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        line = line.rstrip()
        numpos = line.find(' ')
        conval = line[numpos+1:]
        conval = float(conval)
        count = count + 1
        total = total + conval

average = total/count

print('The average spam confidence is ', format(average, '.4f'))
