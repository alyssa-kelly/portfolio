import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.py4e.org/romeo.txt')
for line in fhand:
    print(line.decord().strip())