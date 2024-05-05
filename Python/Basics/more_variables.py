# More Advanced Variables

## Lists

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# print(planets[2])


## Dictionaries

obvious = { 'water': 'wet', 'fire': 'hot', 'sky': 'blue'}

# print(obvious['fire'])

mgmt_addresses = {  'leaf1': '192.168.0.11/24',
                    'leaf2': '192.168.0.12/24', 
                    'leaf3': '192.168.0.13/24',
                    'leaf4': '192.168.0.14/24'
}

# print(mgmt_addresses[ 'leaf1'])

## Nesting

devices = [{ 'water': 'wet'}, [2, 3, 5, 7, 11]]

# print(devices[1][2])

# Set

colors = {'Red', 'Blue'}
colors.add('Green')
colors.add('Green')
# print(colors)

for item in colors:
    print(item)