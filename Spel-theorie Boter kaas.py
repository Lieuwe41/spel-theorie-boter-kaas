import random
from bke import *

class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

class MySmartAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if board[4] == my_symbol:
            getal = getal + 4
        if can_win(board, my_symbol):
            getal = getal + 6
        if is_winner(board, my_symbol):
            getal = getal + 100
        elif can_win(board, opponent_symbol):
            getal = getal - 100
        return getal
    
my_random_agent = MyRandomAgent()
my_smart_agent = MySmartAgent()


validation_result = validate(agent_x=my_smart_agent, agent_o=my_random_agent, iterations=1200)
 
plot_validation(validation_result)