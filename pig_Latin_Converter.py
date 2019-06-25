#Pig latin translator program
original = input('Enter your first name \n')
pgy = "ay"
pgy2 = "way"

word = original.lower()

#check for starting letter using regular expressions
#jjujjhhjj
#ffggggg
first = word[0]
if first in 'aeiou':
    newword = word + pgy2
    print(newword)
else:
    newword = word + first + pgy
    print(newword[1:])


#using list comprehension to separate vowels and constants

AnyWord = input('Type any word or name \n')

new = AnyWord.lower()

#create an empty list
myLetters = []


#iterate through the word and append to the list so created
for letter in new:
    myLetters.append(letter)


#print the list resulted
print(myLetters)


#isolate vowels by creating a list constiting only vowels
vowels = ['a', 'e', 'i', 'o', 'u']


#now use list comprehension to unearth the divergent pairs
Consonants = [item for item in myLetters if item not in vowels]

#The result is so amazing as shown below
print(Consonants)


#Finally reconstruct the word without vowels
for item in Consonants:
    print(item,end='')
