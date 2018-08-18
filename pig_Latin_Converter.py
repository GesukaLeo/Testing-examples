#Pig latin translator program
original ="akuseg"
pgy = "ay"
pgy2 = "way"

word = original.lower()

#check for starting letter using regular expressions
first = word[0]
if first in 'aeiou':
    newword = word + pgy2
    print(newword)
else:
    newword = word + first + pgy
    print(newword[1:])