
#import vonn modulen
import random

name = input('Bitte nenn uns deinen Namen: ')

adjektive = []
nomen = []

adjektive = ['dumm', 'schlau', 'nett', 'tolerant', 'nervig', 'egoistisch', 'überkanditeld']

plus = input('eingabe adjektiv: ')
adjektive.append(plus)

print(adjektive)

print(random.choice(adjektive) + ' ' + name)