def longest_word():
    myList = []

    x=input("Enter any word of your choice")
    myList.append(x)

    y=input("Enter any word of your choice")
    myList.append(y)

    #check for longest word in the list 
    print(max(myList, key=len))