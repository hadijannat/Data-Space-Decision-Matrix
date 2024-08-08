import unittest
from src.decision_matrix import DecisionMatrix
import os

class TestDecisionMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = DecisionMatrix()

    def test_matrix_initialization(self):
        self.assertIsNotNone(self.matrix.fig)
        self.assertIsNotNone(self.matrix.ax)

    def test_plot_point(self):
        self.matrix.plot_point(7, 8)
        # Check if the point was added to the plot
        self.assertEqual(len(self.matrix.ax.lines), 3)  # 2 for the dividing lines, 1 for the point

    def test_save_matrix(self):
        filename = 'test_matrix.png'
        self.matrix.save_matrix(filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)  # Clean up

if __name__ == '__main__':
    unittest.main()
