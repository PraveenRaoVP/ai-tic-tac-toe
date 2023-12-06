# importing the modules required

from models import Game, Player, AI

turn = 0

name = input("Enter your name: ")

while(True):
    player = Player(name, 'X')
    ai = AI('AI', 'O')

    game = Game(player, ai)

    while True:
        game.print_board()
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))
        
        #invoke the make_move function
        try:
            game.make_move(row, col)
            ai.make_move(game)
        except ValueError:
            print('Invalid move')
            continue
        
        #invoke the check_winner function
        if game.check_winner():
            game.print_board()
            
            print(f'{game.players[game.current_player].name} won!')
            
            break
        
        #invoke the check_tie function
        if game.check_tie():
            game.print_board()
            print('Tie!')
    play_again = input('Play again? (y/n): ')
    if play_again == 'n':
        break

