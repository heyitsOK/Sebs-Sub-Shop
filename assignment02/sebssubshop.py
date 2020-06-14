#Name: Omar Khan
#Student ID: 101168124
#Welcoming function (Could have added it to sub selection function but I seperated to make it more organized)
def welcome():
    print("----------------------------------------")
    print("| Welcome to Seb's Savoury Sub Shoppe! |")
    print("----------------------------------------")
    print()

#sub selection function
def subselect():
    print("S U B  S E L E C T I O N")
    print()
    print("1. \"Meat\"-ball sub - $7.99")
    print("2. Cold-cut Club sub - $8.25")
    print("3. Philly's Cheese Mis-Steak sub - $9.55")
    print("4. Veggie Pile sub - $6.75")
    print()
    inp = 0 
    #Used a while loop so that if the user enters bad input I can print an error message and loop back to the beginning
    #See how my condition basically checks if the input is good. If the user gives good input the conditionis satisfied and loops ends
    while (inp > 4 or inp < 1):
        #Getting input
        inp = int(input("What kind of sub would you like? "))
        if (inp > 4 or inp < 1):
            print("I'm sorry " + str(inp) + " is not an available option.")
        else:
            if (inp == 1):
                return 1
            elif (inp == 2):
                return 2
            elif (inp == 3):
                return 3
            elif (inp == 4):
                return 4

#This variable is to count the guacamole
count = 0
#Toppings function
def toppings():
    #This statement basically says that any time I use the variable count in this function it is being used as a globals variable
    #Using the global variable count inside the function without this statement leads to an error saying "Local variable reference before assignment"
    global count
    print("T O P P I N G  S E L E C T I O N")
    print()
    print("Select your toppings.")
    print("Type any of the following and hit enter: ")
    print("lettuce, tomatoes, onions, peppers, jalepenos, pickles, cucumbers, olives, or guacamole.")
    print("Please note: guacamole costs an extra $1.50")
    print("Type done to stop. ")
    #this variable is to accumulate all the toppings
    top = ''
    #this variable is to get input
    inp = ''
    #Again we use a while loop to check when the user inputs the word "done" so we can stop asking for toppings
    while (inp != 'done'):
        #here we get the input
        inp = input("> ")
        #here we check what the input is and then add it to the top variable
        if (inp == 'lettuce'):
            top += 'lettuce '
        elif (inp == 'tomatoes'):
            top += 'tomatoes '
        elif (inp == 'onions'):
            top += 'onions '
        elif (inp == 'peppers'):
            top += 'peppers '
        elif (inp == 'jalepenos'):
            top += 'jalepenos '
        elif (inp == 'pickles'):
            top += 'pickles '
        elif (inp == 'cucumbers'):
            top += 'cucumbers '
        elif (inp == 'olives'):
            top += 'olives '
        elif (inp == 'guacamole'):
            top += 'guacamole '
            count += 1
        elif (inp == 'done'):
            top += ''
        else:
            print("Sorry " + inp + ", isn't a valid topping.")
    return top
#The function that tells you your order and asks you whether it is correct or not. I'm passing in s and t as arguments where s is the
# users sub choice (as an integer) and t is the toppings (as a string)
def yourOrder(s, t):
    print("Your order: ")
    #Here I check what kind of sub user chose so I can print it out
    if (s == 1):
        print("Sub: \"Meat\"-ball sub")
    elif (s == 2):
        print("Sub: Cold-cut Club sub")
    elif (s == 3):
        print("Sub: Philly's Cheese Mis-Steak sub")
    elif (s == 4):
        print("Sub: Veggie Pile sub")
    #here i print what toppings th user wanted
    print("Toppings: " + t)
    correct = input("Is this correct? (y/n) ")
    if (correct == 'n'):
        print("I'm sorry, please try again.")
        #This statement ends the program
        exit()
        
#This is the receipt function and i pass in the users sub choice (s) and also the amount of guacamole they asked for (c) since that factors
# into the total price        
def receipt(s, c):
    subtotal = 0
    tax = 0
    total = 0
    #I check which sub they asked for and add its price to the subtotal
    if (s == 1):
        subtotal += 7.99
    elif (s == 2):
        subtotal += 8.25
    elif (s == 3):
        subtotal += 9.55
    elif (s == 4):
        subtotal += 6.75
    #I add the price of the amount of guacamole they wanted (guacamole = $1.50)
    subtotal += (1.5 * c)
    #Rounded the tax so that it's a nice, clean number
    tax = round((subtotal * .13), 2)
    total = subtotal + tax
    print()
    print("-------------------------")
    print("Subtotal: \t$" + str(subtotal))
    print("Tax: \t \t$" + str(tax))
    print("Total: \t \t$" + str(total))
    print("-------------------------")
    
#Finally I call all the functions and pass in any arguments that need to be passed    
welcome()
sub = subselect()
tops = toppings()
yourOrder(sub, tops)
receipt(sub, count)
