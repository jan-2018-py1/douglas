
def coin():
    heads = []
    tails = []
    for x in range(5001):
        
        from random import *
        flip = randint(0,1)
        if flip ==0:
            heads.append("Heads")
            print 'Attempt #'+str(x)+ ': Throwing a coin......It''s a head! ....... Got '+str(len(heads))+ ' heads so far and '+str(len(tails))+' tails so far'
        else:
            tails.append("Tails")
            print 'Attempt #'+str(x)+ ': Throwing a coin......It''s a tail! ....... Got '+str(len(heads))+ ' heads so far and '+str(len(tails))+' tails so far'
       
    print ('Ending the program, thank you!')
   

coin()
