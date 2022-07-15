
#Imports
import finviz



#Variables
headers = {}

#import this


while True:
    city = input('What City?\n>>> ')
    if city.isalpha():
        break
    else:
        print('That is not a vailid input!')

while True:
    city = input('What Month?\n>>> ')
    if city.isalpha():
        break
    else:
        print('That is not a vailid input!')

while True:
    city = input('What day of the week?\n>>> ')
    if city.isalpha():
        break
    else:
        print('That is not a vailid input!')