import datetime
import random

import chess

import utiles


class Agent:
    """
        Base class for agents.
    """

    def __init__(self, board: chess.Board, next_player) -> None:
        self.board = board
        self.next_player = next_player

    def get_action(self):
        """
            This method receives a GameState object and returns an action based on its strategy.
        """
        pass

    """
            get possible moves : 
                possibleMoves = board.legal_moves

            create a move object from possible move : 
                move = chess.Move.from_uci(str(possible_move))

            push the move : 
                board.push(move)

            pop the last move:
                board.pop(move)
    """


class RandomAgent(Agent):
    def __init__(self, board: chess.Board, next_player):
        super().__init__(board, next_player)

    def get_action(self):
        return self.random()

    def random(self):
        possible_moves_list = list(self.board.legal_moves)

        random_move = random.choice(possible_moves_list)
        return chess.Move.from_uci(str(random_move))

class MinimaxAgent(Agent):
    def __init__(self, board: chess.Board, next_player, depth):
        self.depth = depth
        super().__init__(board, next_player)

    def get_action(self):
        return self.minimax(self.depth, self.next_player, True)[1]

    def minimax(self, depth, turn, is_maximizing):
        best_move = None
        if depth == 0 or self.board.is_game_over():
            return evaluate_board_state(self.board, turn), best_move

        next_turn = 'black' if turn == 'white' else 'white'
        if is_maximizing:
            max_eval = float('-inf')
            for legal_move in self.board.legal_moves:
                move = chess.Move.from_uci(str(legal_move))
                self.board.push(move)
                current_eval, _ = self.minimax(depth - 1, next_turn, False)
                self.board.pop()

                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move = move

            return max_eval, best_move
        else:
            min_eval = float('inf')
            for legal_move in self.board.legal_moves:
                move = chess.Move.from_uci(str(legal_move))
                self.board.push(move)
                current_eval, _ = self.minimax(depth - 1, next_turn, True)
                self.board.pop()
                min_eval = min(min_eval, current_eval)
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move = move

            return min_eval, best_move


class AlphaBetaAgent(Agent):
    def __init__(self, board: chess.Board, next_player, depth):
        self.depth = depth
        super().__init__(board, next_player)

    def get_action(self):
        return self.alpha_beta(self.depth, self.next_player, True, float('-inf'), float('inf'))[1]

    def alpha_beta(self, depth, turn, is_maximizing, alpha, beta):
        best_move = None
        if depth == 0 or self.board.is_game_over():
            return evaluate_board_state(self.board, turn), best_move

        next_turn = 'black' if turn == 'white' else 'white'
        if is_maximizing:
            max_eval = float('-inf')
            for legal_move in self.board.legal_moves:
                move = chess.Move.from_uci(str(legal_move))
                self.board.push(move)
                current_eval, _ = self.alpha_beta(depth - 1, next_turn, False, alpha, beta)
                self.board.pop()

                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move = move
                alpha = max(alpha, max_eval)
                if max_eval >= beta:
                    break

            return max_eval, best_move

        else:
            min_eval = float('inf')
            for legal_move in self.board.legal_moves:
                move = chess.Move.from_uci(str(legal_move))
                self.board.push(move)
                current_eval, _ = self.alpha_beta(depth - 1, next_turn, True, alpha, beta)
                self.board.pop()
                min_eval = min(min_eval, current_eval)
                if current_eval < min_eval:
                    min_eval = current_eval
                    best_move = move
                beta = min(beta, min_eval)
                if min_eval <= alpha:
                    break

            return min_eval, best_move


class ExpectimaxAgent(Agent):
    def __init__(self, board: chess.Board, next_player, depth):
        self.depth = depth
        super().__init__(board, next_player)

    def get_action(self):
        return self.expectimax(self.depth, self.next_player, True)[1]

    def expectimax(self, depth, turn, is_maximizing):
        best_move = None
        if depth == 0 or self.board.is_game_over():
            return evaluate_board_state(self.board, turn), best_move

        next_turn = 'black' if turn == 'white' else 'white'
        if is_maximizing:
            max_eval = float('-inf')
            for legal_move in self.board.legal_moves:
                move = chess.Move.from_uci(str(legal_move))
                self.board.push(move)
                current_eval, _ = self.expectimax(depth - 1, next_turn, False)
                self.board.pop()

                if current_eval > max_eval:
                    max_eval = current_eval
                    best_move = move

            return max_eval, best_move

        else:
            expected_value = 0
            num_moves = len(list(self.board.legal_moves))
            for legal_move in self.board.legal_moves:
                move = chess.Move.from_uci(str(legal_move))
                self.board.push(move)
                current_eval, _ = self.expectimax(depth - 1, next_turn, True)
                self.board.pop()
                expected_value += current_eval / num_moves

            return expected_value, None


def evaluate_board_state(board, turn):
    node_evaluation = 0
    node_evaluation += utiles.check_status(board, turn)
    node_evaluation += utiles.evaluationBoard(board)
    node_evaluation += utiles.checkmate_status(board, turn)
    node_evaluation += utiles.good_square_moves(board, turn)
    return -node_evaluation