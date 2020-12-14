import os
import sys
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))
from Character import Character

class TestCharacter(unittest.TestCase):

    def setUp(self):
        self.char = Character()

    def tearDown(self):
        self.char = None

    def test_doublejump(self):
        self.assertTrue(self.char.double_jump)
        self.char.jump()

        while self.char.state != 'FALL':
            self.char._gravity()
            self.char._friction()

        self.assertTrue(self.char.double_jump)

        self.char.jump()
        self.assertFalse(self.char.double_jump)



if __name__ == '__main__':
    unittest.main()