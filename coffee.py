"""
1:Make and serve me , you and Gibbs a cup of coffee(add coffee, add hot water, stir)

2:Change how the mix is stirred

3:A better way to make coffee with less repetition

4:Make you coffee with milk and sugar (add sugar, add milk)

5:Make Gibbs coffee with milk, sugar and something else (add sugar, add milk, ..)
"""
#==================== Make my coffee====================================
ingredients = ['coffee', 'hot water']
print('Started making coffee..')
print('Getting cup')
print('Adding {}'.format(', '.join(ingredients)))

#=============Edited next line(for 5 seconds)===========================
print('Stir the mix for 5 seconds')
print('Finished making coffee..')
my_coffee= 'Tasty coffee'
print("--Here's is your {} {}. Enjoy!!--\n".format(my_coffee, 'Perez'))

#================== Make you coffee=====================================
print('Started making coffee..')
print('Getting cup')
print('Adding {}'.format(', '.join(ingredients)))
print('Stir the mix for 5 seconds')
print('Finished making coffee..')
your_coffee= 'Tasty coffee'
print("--Here's is your {} {}. Enjoy!!--\n".format(your_coffee, 'you'))

#====================Make Gibbs Coffee=====================================
print('Started making coffee..')
print('Getting cup')
print('Adding {}'.format(', '.join(ingredients)))
print('Stir the mix for 5 seconds')
print('Finished making coffee..')
gibbs_coffee= 'Tasty coffee'
print("--Here's is your {} {}. Enjoy!!--\n".format(gibbs_coffee, 'Gibbs'))
