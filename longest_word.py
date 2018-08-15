def longest_word():
    results = []

    x=input("Enter any First word of your choice \n")
    results.append(x)

    y=input("Enter any Second word of your choice \n")
    results.append(y)

    #print the list so far
    print(results)

    #check for longest word in the list 
    count = 0
    for i in results: # Go through the whole list
        if len(i) > count: #Checking for the longest word(string)
            count = len(i)
            word = i
        else:
            word =results[0] +"\n" + results[1]
    return ("the longest string is " + word)


#call the function
print(longest_word())





#to be incorporated to the larger code
totalEntries = len(lstName)
  currentEntry = 0
  longestLength = 0
  while currentEntry < totalEntries:
    thisEntry = len(str(lstName[currentEntry]))
    if int(thisEntry) > int(longestLength):
      longestLength = thisEntry
      longestEntry = currentEntry
    currentEntry += 1
  return longestLength
