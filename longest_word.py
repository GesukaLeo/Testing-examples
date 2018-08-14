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
            print ("the longest string is " + word)
        else:
            print("No longest")


longest_word()
