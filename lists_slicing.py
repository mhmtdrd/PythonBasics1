# modules in pyhton - pythom files:lowers , use underscroe

#first_name (smoke case)
#sql,java ->listsSlicing, firstname (camel case)

players = ['charles' ,'martina' , 'michael' , 'florence' , 'eli']
print(players[0:3]) # 3 players
print(players[:3]) # 3 players , by default it starts from index 0
print(players[1:3])  # 2 players

print(players[2:]) # 3 players , by default it end with last index
print(players[:]) # runs all elements of the list

new_players = players[:] # copied to new list , independent from players list
players.append('martin')
new_players.append('mark')
print('players:', players)
print('new players:' , new_players)

players1 = players # it is not a copy but duplicate refence


