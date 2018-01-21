def listdict(list1,list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1 >= len2:
        keys=list1
        values=list2
    else:
        keys=list2
        values=list1

    dictionary = dict(zip(keys,values))

    print dictionary

listdict(
 ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar","joe"],
 ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])
