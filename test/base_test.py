import unittest


class BaseTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(pages)
    unittest.TextTestRunner(verbosity=1).run(suite)
