import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('bryan', 'bai')
        self.assertEqual(formatted_name, 'Bryan Bai')
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('bai', 'jiang', 'li')
        self.assertEqual(formatted_name, 'Bai Li Jiang')

# unittest.main()

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(NameTestCase)
    unittest.TextTestRunner().run(suite)