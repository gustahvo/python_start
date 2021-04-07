#string cocatenation (how to pu strings together)
#suppose we want to create a string that says 'subscribe to _____'
youtuber='Gustahvo'#some string variable

# a few ways to do this
print('subscribe to '+ youtuber)
print('subscribe to {}'.format(youtuber))
print(f'subscribe to {youtuber}')

adj = input('adjective:')
verb1= input('verb:')
verb2= input('verb:')
famous_person= input('famous person:')

madlib=f'computer programming is so {adj}! It makes me so excited all the time bacause \
 i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!'

print(madlib) 