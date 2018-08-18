def longest_word():
    #read the user inputs

    x=input("Enter any First word of your choice \n")
    
    y=input("Enter any Second word of your choice \n")
    
    #check for longest word as keyed in
    if(len(x)>len(y)):
        print("The longest word is :",x)
    elif(len(y)>len(x)):
        print("The longest word is :",y)
    else:
        print(x+"\n"+y)

#call the function
print(longest_word())
