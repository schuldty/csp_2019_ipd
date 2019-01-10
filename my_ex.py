####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'neeman'
strategy_name = 'random choice'
strategy_description = '''\
obviously i need to work on this some more
'''

import random 

def move(my_history, their_history, my_score, their_score):
    return random.choice(['b', 'c'])