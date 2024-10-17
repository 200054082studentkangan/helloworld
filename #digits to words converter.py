#number to words converter
running = True
while running:
    print ("this is thenumber to words converter!")
    number = input ("gimme a number  ")

    if number == '1':
        print ("this says one!")
    elif number == '2':
        print ("this says two!")
    elif number == '3':
        print ("this says three!")
    elif number == '4':
        print ("this says four!")
    elif number == '5':
        print ("this says five!")
    elif number == '6':
        print ("this says six!")
    elif number == '7':
        print ("this says seven!")
    elif number == '8':
        print ("this says eight!")
    elif number == '9':
        print ("this says nine!")
    elif number == '0':
        print ("this says zero!")
    else:
        print ("this isn't a number i can translate!")
    print ("wanna do it again?")
    again = input ("Y/N").upper()[0]
    if again != 'Y':
        running = False