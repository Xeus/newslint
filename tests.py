import unittest
import newslint


class TestLinter(unittest.TestCase):

    def setUp(self):
        self.result = newslint.newslint('brown shirt obamacare tom friedman hippies fucker')

    def test_keys(self):
        self.assertTrue('credibility' in self.result.fail_points)
        self.assertTrue('nonpartisanship' in self.result.fail_points)
        self.assertTrue('professionalism' in self.result.fail_points)

    def test_points(self):
        self.assertEqual(self.result.fail_points['credibility'], 2.0)
        self.assertEqual(self.result.fail_points['nonpartisanship'], 2.0)
        self.assertEqual(self.result.fail_points['professionalism'], 1.0)

    def test_messages(self):
        self.assertEqual(len(self.result.warnings), 2)
        self.assertEqual(len(self.result.errors), 2)
        self.assertEqual(len(self.result.notices), 0)

    def test_mentions(self):
        self.assertEqual(len(self.result.mentions), 5)


if __name__ == '__main__':
    unittest.main()
