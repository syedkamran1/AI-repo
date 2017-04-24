def sandwich_make(*items):
    print('You Have Ordered The Sandwich With Following Items!')
    for item in items:
        print('--> '+item)


sandwich_make('Cheese')
sandwich_make('Cheese','Onion')
sandwich_make('Cheese','Onion','Mustard Sauce')

