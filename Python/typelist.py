#input
l = [27,"red sox",2004,"bloody sock","yankees","world series"]
l.sort(reverse=False)

print "Your list---",l
#output
total = 0
sentence=[]
string =''


for element in l:
	if isinstance(element,int):
		total = total+element
	else:
		sentence.append(element)

for i in sentence:
	string = string + ' ' + i

print 'sum: ',total
print 'string: ',string

if total!=0 and string != '':
	print "The list you entered is mixed type"

elif total == 0 and string !='':
	print "The list you entered is string data"

else:
	print "The list you entered is integer data"

