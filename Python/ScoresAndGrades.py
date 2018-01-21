
def scores(v):
    
        if v in range(90,101):
            print 'Score :'+str(v)+'; Your grade is A'
        elif v in range(80,90):
            print 'Score :'+str(v)+'; Your grade is B'
        elif v in range(70,80):
            print 'Score :'+str(v)+'; Your grade is C'
        elif v in range(60,70):
            print 'Score :'+str(v)+'; Your grade is D'
        else:
            print 'End of program. Bye Felicia!'

for x in range (0,12):
    from random import *
    x = randint(60,100)
    scores(x)

