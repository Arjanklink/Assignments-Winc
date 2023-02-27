# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
playerscored = 'Ruud Gullit'
playerscored2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54


scorers = playerscored + " " + str(goal_0) + "," + " " + playerscored2 + " " + str(goal_1)

print(scorers)

report = f"{playerscored} scored in the {goal_0}nd minute" '\n' f"{playerscored2} scored in the {goal_1}th minute"

print(report)

player = 'Frank Rijkaard'
space_index = player.find(' ')

first_name = player[0:space_index]

print(first_name)


last_name = 'Rijkaard'
last_name_len = len(last_name)

print(last_name, last_name_len)

name_short = player[0] + '.' + ' ' + last_name

print(name_short)


x = (first_name + '!' + ' ') * len(first_name) 
chant = x.rstrip()

print(chant)

good_chant = chant[-1] != ' '

print(good_chant)