import logging
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.moves = []
        self.game_id = random.randint(1000, 9999)  # Unique game identifier to separate games in logs
        self.knight_moves = 0
        self.swimmers = 0  # Mocking this value for now, assuming some chess variant
        self.current_turn = random.choice(['white', 'black'])

    def initialize_board(self):
        # Mock board initialization with tools (pieces)
        board = ['piece1', 'piece2', 'knight', 'swimmer']  # Just a mock
        return board

    def log_game_start(self):
        logger.info(f"[Game ID {self.game_id}] Game started by {self.current_turn}")

    def log_move(self, piece, start_pos, end_pos):
        self.moves.append(piece)
        if piece == 'knight':
            self.knight_moves += 1
        logger.debug(f"[Game ID {self.game_id}] {piece} moved from {start_pos} to {end_pos}")

    def log_board_state(self):
        board_state = str(self.board)
        logger.debug(f"[Game ID {self.game_id}] Current board state: {board_state}")

    def log_game_end(self, result):
        logger.info(f"[Game ID {self.game_id}] {result} won the game" if result != "draw" else f"[Game ID {self.game_id}] The game ended in a draw")
        logger.info(f"[Game ID {self.game_id}] Total moves: {len(self.moves)}")
        logger.info(f"[Game ID {self.game_id}] Total knight (cavalry) moves: {self.knight_moves}")
        logger.info(f"[Game ID {self.game_id}] Total swimmers: {self.swimmers}")  # A mock log for now
        # Assuming 'vessels' are a set of pieces; counting their survival duration
        vessel_duration = sum(1 for move in self.moves if move == 'vessel')
        logger.info(f"[Game ID {self.game_id}] Vessel survived for {vessel_duration} turns")

    def play_mock_game(self):
        self.log_game_start()
        for _ in range(10):  # Mock 10 moves
            piece = random.choice(self.board)
            start_pos = (random.randint(0, 7), random.randint(0, 7))
            end_pos = (random.randint(0, 7), random.randint(0, 7))
            self.log_move(piece, start_pos, end_pos)
            self.log_board_state()
        result = random.choice(["white", "black", "draw"])
        self.log_game_end(result)

game = ChessGame()
game.play_mock_game()
