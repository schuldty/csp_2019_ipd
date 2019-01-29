team_name = 'team_owen'
strategy_name = 'reason in first half'
strategy_description = ' use a reasonable way of judging the next move for the first 400 rounds then go full betrayal unless colluded with more than 100 times'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: 
        return 'c'
    if their_history[-1] == 'c'and len(my_history) < 400: 
        return'c'
    if their_history[-1] == 'b'and len(my_history)<400:
        return 'b'
    if len(their_history)> 400 and their_history[-1] == 'c' > 200:
        return 'c'
    if len(their_history)> 400 and their_history[-1] == 'b' > 200:
        return 'b'
        
        
    
    
    