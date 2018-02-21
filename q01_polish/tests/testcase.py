from unittest import TestCase
import pandas as pd

original_return = pd.read_csv('q01_australian/tests/Original_classes.csv', header=None)
student_return = pd.read_csv('q01_australian/predicted_class.csv', header=None)

original = len(original_return)


class TestHackathon(TestCase):
    def test_return(self):
        self.assertEqual(original, len(student_return),
                         "Expected list of variables does not match returned list of variables")
