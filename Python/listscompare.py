list1 =['red','blue','green','yellow'] # set list 1
list2 =['red','blue','green','yellow'] # set list 2
list3 = set(list1) & set(list2) # compare list1 vs list2 creates a set of matches

x=len(list1) #length of each list
y=len(list2)
z=len(list3)

if x!=y:			
	print "lists don't match" # if list 1 doesn't equal list 2 in length they can't match

elif z==x and z==y:			
	print "lists match"		  # if list1 does match list2 length then we compare list3 length to both x and y if those lengths match all is good.
	
	