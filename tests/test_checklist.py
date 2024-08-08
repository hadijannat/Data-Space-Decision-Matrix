import unittest
from src.checklist import Checklist

class TestChecklist(unittest.TestCase):
    def setUp(self):
        self.checklist = Checklist()

    def test_checklist_initialization(self):
        self.assertEqual(len(self.checklist.questions), 16)
        self.assertEqual(len(self.checklist.responses), 0)

    def test_calculate_score(self):
        self.checklist.responses = [3, 4, 5, 2, 1]
        self.assertEqual(self.checklist.calculate_score(), 15)

    def test_interpret_score(self):
        self.checklist.responses = [1] * 16  # Score of 16
        self.assertEqual(self.checklist.interpret_score(), "Traditional data sharing methods may suffice")
        
        self.checklist.responses = [3] * 16  # Score of 48
        self.assertEqual(self.checklist.interpret_score(), "Consider implementing a data space")
        
        self.checklist.responses = [5] * 16  # Score of 80
        self.assertEqual(self.checklist.interpret_score(), "Strongly consider implementing a data space")

if __name__ == '__main__':
    unittest.main()
