PHRASE = "It's thanksgiving day. It's my birthday,too!"
POS = PHRASE.find("day")

print PHRASE[POS:POS+3]

NEWPHRASE = PHRASE.replace('day','month',2)

print NEWPHRASE


x=[2,12,55,1,88,99]

MOST = max(x)
MIN = min(x)
print MOST
print MIN

x = ["hello",2,54,-2,7,12,98,"world"]

print x[0]
print x[-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort(reverse =False)
y= x[:len(x)/2]
z= x[len(x)/2:]
print y
print z
z.insert(0,y)
print z