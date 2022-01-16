#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Responsible for hosting the rules of chess. Will use the python-chess library
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import chess, chess.pgn
import random
def making_list_file():
    with open('ComputerGames.pgn') as pgn:
        i = 0
        game= chess.pgn.read_game(pgn)
        whole_list = []
        while (True):
            if game != None:
                board = game.board()
                fen_list = []
                fen_list.append(board.fen())
                for move in game.mainline_moves():
                    board.push(move)
                    fen_list.append(board.fen())
                whole_list.append(fen_list)
                game = chess.pgn.read_game(pgn)
            else:
                break

    with open('listfile.txt', 'w') as filehandle:
        for listitem in whole_list:
            for fen in listitem:
                filehandle.write('%s\n' % fen)
            filehandle.write('\n \n')

def making_next_move_file():
    file = open('next_move_list.txt', 'w')
    oldfile = open('listfile.txt', 'r')
    line = oldfile.readline()
    while True:
        line = oldfile.readline()

        if not line:
            break
        file.write(line)

def make_random_move_file(list_of_games_txt_file, name_of_new_file_with_random_moves):
    oldfile = open(list_of_games_txt_file, 'r')
    newfile = open(name_of_new_file_with_random_moves, 'w')
    line = oldfile.readline()
    while True:
        try:
            board = chess.Board(line)
            moves = list(board.legal_moves)
            move = moves[random.randint(0, len(moves) - 1)]
            board.push(move)
            line = board.fen()
            newfile.write('%s\n' % line)
            line = oldfile.readline()
        except:
            if not line:
                break
            else:
                newfile.write('\n')
                line = oldfile.readline()

def main():
    file1 = open('listfile.txt', 'r')
    file2 = open('next_move_list.txt', 'r')
    file3 = open('rand_move_list.txt', 'r')
    file1.close()
    file2.close()
    file3.close()


if __name__ == '__main__':
    main()
