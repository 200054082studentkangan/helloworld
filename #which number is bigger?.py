#which number is bigger?

running = True
while running:
    print ("give me two numbers and i'll tell you which is bigger!")

    first_num = input ("first number? > ")
    print (first_num)
    second_num = input ("second number? > ")

    if first_num > second_num: 
        print (first_num + " is bigger!")
    elif first_num < second_num:
        print (second_num + " is bigger!")
    else:
        print ("the numbers are equal!")
    fromthetop = input ("do it again? Y/N ").upper()[0]
    if fromthetop != 'Y':
        running = False