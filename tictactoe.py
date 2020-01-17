"""
Monte Carlo Tic-Tac-Toe Player - by Nick Togneri
"""
import random
import poc_ttt_gui
import poc_ttt_provided as provided


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100      # Number of trials to run
SCORE_CURRENT = 5.0 # Score for squares played by the current player
SCORE_OTHER = 3.0   # Score for squares played by the other player
BOARD_SIZE = 3

#GAME_BOARD = provided.TTTBoard(BOARD_SIZE)

# Add your functions here.
def mc_trial(board, player):
    """Takes a blank board and rotates players until game
    is won or a draw
    """
    while board.check_win() == None:
        move_choice = random.choice(board.get_empty_squares())
        board.move(move_choice[0], move_choice[1], player)
        player = provided.switch_player(player)
    return
    
def mc_update_scores(scores, board, player):
    """
    Takes a completed empty list of scores, a completed game
    board and checks it for winning or losing squares. Adds
    those squares to the player who either won or lost.
    """
    if board.check_win() == provided.DRAW:
        #print board.check_win() == 4,'PASS'
        return
    if board.check_win() == player:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == player:
                    scores[row][col] += SCORE_CURRENT
                else:
                    if board.square(row, col) != provided.EMPTY:
                        scores[row][col] -= SCORE_OTHER 
    else:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if board.square(row, col) == player:
                    scores[row][col] -= SCORE_CURRENT
                else:
                    if board.square(row, col) != provided.EMPTY:
                        scores[row][col] += SCORE_OTHER
    return     
    
def get_best_move(board, scores):
    """
    Takes empty squares from games and matches them to the
    squares with the highest scores.
    """
    list_of_scores = scores
    best_moves = []
    score = ()    
    empty_squares = board.get_empty_squares()
    empty_scores = []
    
    for square in empty_squares:
        empty_scores += [list_of_scores[square[0]][square[1]]]
    
    max_value = max(empty_scores)
    
    for empty in board.get_empty_squares():
        row = empty[0]
        col = empty[1]
        score = list_of_scores[row][col]
        if score == max_value and score != provided.EMPTY:
            best_moves.append((row, col))
#    
    next_move = random.choice(best_moves)
    return next_move

    
def mc_move(board, player, trials):
    
    """
        hdfghsldkfghalkdjfghalksdfgha.skdjfghakd.j
    """
    scores_list =  [[0] * board.get_dim() for _ in range(board.get_dim())]
    for _tests in range(trials):
        clone_board = board.clone()
        mc_trial(clone_board, player)
        mc_update_scores(scores_list, clone_board, player)
    #print board, scores_list
    return get_best_move(board, scores_list)



# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.
#mc_update_scores([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 
#                       provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
#                                                    [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], 
#                                                    [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]])
##provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
