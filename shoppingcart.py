
def shopping (item, quantity, shopping_list):
    quantity = int(quantity)
    shopping_list[item] = {
        'quantity': quantity,
        
    }
    
def main():
    shopping_list = {}
    while True:
        items = input('What items would you like to add? (Type "Done" when finished.): ')
        if items == 'done':
            break
        quantity = input("How many would you like? ")
        shopping (items, quantity, shopping_list)
    while True:
        show = input('Show the list (y/n): ')
        if show == 'y':
            print(shopping_list)

        remove = input('Would you like to remove items (y/n): ')
        if remove == 'y':
            what_to_remove = input('What would you like to remove? ')
            how_many = input('How many would you like to remove? ')
            if how_many.isdigit():
                how_many = int(how_many)
                shopping_list[what_to_remove]['quantity'] -= how_many
#                 shopping_list[what_to_remove]['quantity'] = shopping_list[what_to_remove]['quantity']- how many
                print(shopping_list)
        if remove == 'n':
            quit= input('Are you finished (y/n): ')
            if quit == 'y':
                print('Thank you come again')
                break
    
        
            
main()
