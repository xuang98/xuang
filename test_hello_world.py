"""Simple hello world test."""

import unittest


def hello_world():
    return "Hello, world!"


class HelloWorldTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
