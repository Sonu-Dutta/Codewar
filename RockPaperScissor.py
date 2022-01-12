# Let's play! You have to return which player won! In case of a draw return Draw!.
# Examples:
# rps('scissors','paper') // Player 1 won!
# rps('scissors','rock') // Player 2 won!
# rps('paper','paper') // Draw!

def rps(p1, p2):
# method1
    # beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    # if beats[p1] == p2:
    #     return "Player 1 won!"
    # if beats[p2] == p1:
    #     return "Player 2 won!"
    # return "Draw!"

# method2
#     options = ["rock", "paper", "scissors"]
#     outcomes = ["Draw!", "Player 1 won!", "Player 2 won!"]
#     return outcomes[options.index(p1) - options.index(p2)]

# method3
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]

print(rps('paper','rock'))