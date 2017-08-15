"""
1:Make and serve me , you and Gibbs a cup of coffee(add coffee, add hot water, stir)

2:Change how the mix is stirred

3:A better way to make coffee with less repetition

4:===========Make you coffee with milk and sugar (add sugar, add milk)=========

5:Make Gibbs coffee with milk, sugar and something else (add sugar, add milk, ..)
"""
#======To avoid Reputation we shall define the functions below:===============
# For  make coffee
#========Adding Options we use the if statements========check my code below!!!=====
def make_coffee(options=''):

   # options=['sugar', 'milk']
   

    ingredients = ['coffee', 'hot water']

    if options:
        ingredients.append(','.join(options))
    print('Started making coffee..')
    print('Getting cup')
    print('Adding {}'.format(', '.join(ingredients)))

    #=============Edited next line(for 5 seconds)===========================
    print('Stir the mix for 5 seconds')
    print('Finished making coffee..')
    if options:
        coffee = 'Tasty coffee with {}' .format(', '.join(options))
    else:
     coffee = 'Tasty coffee'
        
    return coffee

    
def serve_coffee(coffee, person_name):
    #serving coffee out include the arguments of coffee and person_name in the print statement
    # Now any name and any coffee passed in will be outputted or served

    print("--Here's is your {} {}. Enjoy!!--\n".format(coffee, person_name))

#==================== Make my coffee and hot water====================================
my_coffee = make_coffee()
serve_coffee(my_coffee, 'Evans')

#================== Make your self coffee with sugar and hot water=====================================
my_coffee = make_coffee(['sugar'])
serve_coffee(my_coffee, 'you')

#====================Make Gibbs Coffee, hot water and with milk=====================================
my_coffee = make_coffee(['milk'])
serve_coffee(my_coffee, 'Gibbs')