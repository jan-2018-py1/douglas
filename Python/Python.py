# num = 7 #integer
# word ="scott" #string
# flag = True #Boolean
# pi = 3.14 #Float

# print num,word,flag,pi

#conditionals
# if flag == 7 or flag == False:
#    print word
# else:
#    print "Def not true!"

animals = ["Cat", "Dog", "Frog", "Hog"] # list
#print animals[0]

#Loops
for number in range(0, 11):
    square = number * number
    print square

for idx in range(0, 4):
    print animals[idx]

for animal in animals:
    print animal

#Function
def makenoise(animal):
    if animal == "Cat":
        print "Meow"
    if animal == "Dog":
        print "Bark"

#() invoking "Doing"
makenoise("Cat")
