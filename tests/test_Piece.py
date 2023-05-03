import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from Piece import Knight
from enums import Player

class TestKnight(TestCase):
    def test_get_valid_peaceful_moves(self):
        game_state = MagicMock()

        empty_piece = MagicMock()
        empty_piece.get_player.return_value = Player.EMPTY

        knight = Knight("Knight", 4, 4, Player.PLAYER_1)
        game_state.get_piece.side_effect = [empty_piece] * 8
        game_state.is_valid_piece.return_value = True

        moves = knight.get_valid_peaceful_moves(game_state)
        expected_moves = [(2, 3), (2, 5), (3, 2), (3, 6), (5, 2), (5, 6), (6, 3), (6, 5)]
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_get_valid_peaceful_moves_corner(self):
        game_state = MagicMock()

        empty_piece = MagicMock()
        empty_piece.get_player.return_value = Player.EMPTY

        knight = Knight("Knight", 0, 0, Player.PLAYER_1)
        game_state.get_piece.side_effect = [empty_piece] * 8
        game_state.is_valid_piece.return_value = True

        moves = knight.get_valid_peaceful_moves(game_state)
        expected_moves = [(1, 2), (2, 1)]
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_get_valid_peaceful_moves_edge(self):
        game_state = MagicMock()

        empty_piece = MagicMock()
        empty_piece.get_player.return_value = Player.EMPTY

        knight = Knight("Knight", 0, 3, Player.PLAYER_1)
        game_state.get_piece.side_effect = [empty_piece] * 8
        game_state.is_valid_piece.return_value = True

        moves = knight.get_valid_peaceful_moves(game_state)
        expected_moves = [(1, 1), (2, 2), (2, 4)]
        self.assertEqual(sorted(moves), sorted(expected_moves))
