
def draw_star(a_list):
    for i in a_list:
        print '*' * i

#draw_star([2,5,8,9])




def draw_stars(a_list):
    for i in a_list:
        if type(i).__name__=='int':
            print '*' * i
        else:
            print i[0]*len(i)

draw_stars([1,'boston',9,'red'])