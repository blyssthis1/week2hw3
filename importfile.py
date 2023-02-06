# Program in Jupyter Notebook should take in user input and use imported
# functions to calculate a circle's circumference or a houses square footage
 


from sqfoot import sqft as ft

ft(length,width)



from sqfoot import circumference as circum

circum(r)


def house():
    question = input('Would you like some help today?(y/n) ')
    if question.lower() == 'n':
        print("Have a nice day!")
    elif question.lower() == 'y':
        question1 = input("Do you need calculate circumference('c') or house square foot('s')?")
        if question1.lower() == 'c':
            radius = float(input('What is the radius? '))
            x = circumference(radius)
            print(x)
        elif question1.lower()== 's':
                length = input('What is the lenth of your house? ')
                width = input('What is the width of your house? ')
                y = sqft(length, width)
                print(y)
        else:
            print('Invalid Entry')
    else:
        print('Invalid Entry')
house()