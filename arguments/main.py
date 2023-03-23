# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# 1
def greet(name, greet= 'Hello, <name>!'):
    
    overwrite_greet = greet.replace('<name>', name)
    
    print(overwrite_greet)
    return overwrite_greet


greet('Arjan')
greet("Bob", "What's up, <name>!")

# 2
def force(mass, body= 'earth'):

    planets = {
        'sun': 274, 
        'jupiter': 25.0, 
        'neptune': 11.2, 
        'saturn': 10.4,   
        'earth': 9.8, 
        'uranus': 8.9, 
        'venus': 8.9, 
        'mars': 3.7, 
        'mercury': 3.7, 
        'moon': 1.6,
        'pluto': 0.6
    }

    if body in planets.keys():

        gravity = planets[body]
        print(gravity)
        force_calculate = mass * gravity
        print(force_calculate)
   
    else:
        print('planet not found')

    return force_calculate

force(2, 'sun' )

# 3

def pull(m1,m2,d):
    
    g = 6.674 * 10 ** -11
   
    gravitional_pull = g * m1 * m2 / d ** 2

    print(gravitional_pull)
    return gravitional_pull

pull(800, 1500, 3)