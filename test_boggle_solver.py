import unittest
from boggle_solver import Boggle


class TestBoggle(unittest.TestCase):

    # Test 1: An empty dictionary should return no solutions.
    def test_empty_dictionary(self):
        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = []

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 2: A 1x1 grid cannot contain a valid word.
    def test_1x1_grid(self):
        grid = [["A"]]
        dictionary = ["A"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 3: Words shorter than 3 letters are invalid.
    def test_words_less_than_three_letters(self):
        grid = [["A", "B", "C"]]
        dictionary = ["A", "AB", "ABC"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["ABC"])

    # Test 4: Letters next to each other horizontally can form a word.
    def test_horizontal_adjacency(self):
        grid = [["C", "A", "T"]]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CAT"])

    # Test 5: Diagonal tiles count as adjacent.
    def test_diagonal_adjacency(self):
        grid = [["C", "X"],
                ["X", "A"],
                ["T", "X"]]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CAT"])

    # Test 6: Vertical tiles can form a word.
    def test_vertical_adjacency(self):
        grid = [["C"],
                ["A"],
                ["T"]]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CAT"])

    # Test 7: A word not present on the board should not be found.
    def test_word_not_found(self):
        grid = [["C", "A"],
                ["T", "X"]]
        dictionary = ["DOG"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 8: Multiple valid words should be found.
    def test_multiple_words(self):
        grid = [["C", "A", "T"],
                ["D", "O", "G"]]
        dictionary = ["CAT", "DOG"]

        game = Boggle(grid, dictionary)

        solution = game.getSolution()

        self.assertEqual(len(solution), 2)
        self.assertIn("CAT", solution)
        self.assertIn("DOG", solution)

    # Test 9: The same tile cannot be reused within one word.
    def test_no_tile_reuse(self):
        grid = [["A", "B"]]
        dictionary = ["ABA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 10: A word can begin from a corner tile.
    def test_corner_start(self):
        grid = [["C", "X", "X"],
                ["X", "A", "X"],
                ["X", "X", "T"]]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CAT"])

    # Test 11: The Qu special tile can be used.
    def test_qu_tile(self):
        grid = [["Qu", "A"],
                ["X", "X"]]
        dictionary = ["QUA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["QUA"])

    # Test 12: The St special tile can be used.
    def test_st_tile(self):
        grid = [["St", "A"],
                ["X", "X"]]
        dictionary = ["STA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["STA"])

    # Test 13: The Ie special tile can be used.
    def test_ie_tile(self):
        grid = [["Ie", "T"],
                ["X", "X"]]
        dictionary = ["IET"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["IET"])

    # Test 14: A 0x0 grid should return no solutions.
    def test_empty_grid(self):
        grid = []
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 15: A dictionary word requiring a missing letter should not be found.
    def test_missing_letter(self):
        grid = [["C", "A"],
                ["T", "X"]]
        dictionary = ["CAR"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

            # Test 16: A 3x3 grid can form a word through multiple directions.
    def test_3x3_grid(self):
        grid = [["C", "A", "T"],
                ["X", "X", "X"],
                ["X", "X", "X"]]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["CAT"])

    # Test 17: A longer word can be formed using adjacent tiles.
    def test_longer_word(self):
        grid = [["T", "E", "N", "T"],
                ["X", "X", "X", "X"]]
        dictionary = ["TENT"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), ["TENT"])

    # Test 18: The same letter can appear on different tiles.
    def test_repeated_letter_different_tiles(self):
        grid = [["B", "A"],
                ["A", "T"]]
        dictionary = ["BAT"]

        game = Boggle(grid, dictionary)

        solution = game.getSolution()

        self.assertIn("BAT", solution)

    # Test 19: A longer word can use a special Qu tile.
    def test_qu_in_longer_word(self):
        grid = [["Q", "U", "A", "R"],
                ["X", "X", "T", "X"]]
        dictionary = ["QUART"]

        game = Boggle(grid, dictionary)

        self.assertIn("QUART", game.getSolution())

    # Test 20: The official simple example from the assignment.
    def test_assignment_example_one(self):
        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = ["A", "B", "AC", "ACA", "ACB", "DE"]

        game = Boggle(grid, dictionary)

        solution = game.getSolution()

        self.assertEqual(len(solution), 1)
        self.assertIn("ACB", solution)

    # Test 21: The official second assignment example.
    def test_assignment_example_two(self):
        grid = [["A", "B", "C", "D"],
                ["E", "F", "G", "K"],
                ["I", "J", "Ie", "D"],
                ["L", "M", "N", "A"]]
        dictionary = ["ABEF", "AFJIEB", "DGKD", "DGKA"]

        game = Boggle(grid, dictionary)

        solution = game.getSolution()

        self.assertIn("ABEF", solution)
        self.assertIn("AFJIEB", solution)
        self.assertIn("DGKD", solution)
        self.assertNotIn("DGKA", solution)

    # Test 22: A word that is too short should not be returned.
    def test_two_letter_word(self):
        grid = [["C", "A"],
                ["T", "X"]]
        dictionary = ["CA"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 23: A word can use diagonal movement multiple times.
    def test_multiple_diagonal_moves(self):
        grid = [["C", "X", "X"],
                ["X", "A", "X"],
                ["X", "X", "T"]]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertIn("CAT", game.getSolution())

    # Test 24: A word that requires reusing one tile should not be found.
    def test_reuse_tile_longer_word(self):
        grid = [["C", "A"],
                ["X", "T"]]
        dictionary = ["CACT"]

        game = Boggle(grid, dictionary)

        self.assertNotIn("CACT", game.getSolution())

    # Test 25: A word can be formed starting from the bottom row.
    def test_bottom_row_start(self):
        grid = [["X", "X", "X"],
                ["X", "X", "X"],
                ["C", "A", "T"]]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertIn("CAT", game.getSolution())

    # Test 26: A word can be formed starting from the right side.
    def test_right_side_start(self):
        grid = [["X", "X", "C"],
                ["X", "X", "A"],
                ["X", "X", "T"]]
        dictionary = ["CAT"]

        game = Boggle(grid, dictionary)

        self.assertIn("CAT", game.getSolution())

    # Test 27: Multiple dictionary words can be rejected when none exist.
    def test_no_dictionary_words_found(self):
        grid = [["A", "B"],
                ["C", "D"]]
        dictionary = ["DOG", "CAT", "FISH"]

        game = Boggle(grid, dictionary)

        self.assertEqual(game.getSolution(), [])

    # Test 28: A special St tile can be part of a longer word.
    def test_st_in_longer_word(self):
        grid = [["St", "O", "N"],
                ["X", "X", "X"]]
        dictionary = ["STON"]

        game = Boggle(grid, dictionary)

        self.assertIn("STON", game.getSolution())

    # Test 29: A special Ie tile can be part of a longer word.
    def test_ie_in_longer_word(self):
        grid = [["B", "Ie", "T"],
                ["X", "X", "X"]]
        dictionary = ["BIET"]

        game = Boggle(grid, dictionary)

        self.assertIn("BIET", game.getSolution())

    # Test 30: A dictionary can contain both valid and invalid words.
    def test_valid_and_invalid_words(self):
        grid = [["C", "A", "T"],
                ["D", "O", "G"]]
        dictionary = ["CAT", "DOG", "ELEPHANT", "AB"]

        game = Boggle(grid, dictionary)

        solution = game.getSolution()

        self.assertEqual(len(solution), 2)
        self.assertIn("CAT", solution)
        self.assertIn("DOG", solution)
        self.assertNotIn("ELEPHANT", solution)
        self.assertNotIn("AB", solution)
if __name__ == "__main__":
    unittest.main()