import unittest
import functions


class EvenOdd(unittest.TestCase):

    def test_even(self):
        response = functions.even_odd(2)
        self.assertEqual(response, 'even')

    def test_odd(self):
        response = functions.even_odd(1)
        self.assertEqual(response, 'odd')


class Birthday(unittest.TestCase):

    def test_positive(self):
        response = functions.birthday('Alex', 28)
        self.assertEqual(response, "Happy birthday Alex! I hear you're 28 today.")


class Display(unittest.TestCase):

    def test_display(self):
        message = functions.display('Hello, World!')
        self.assertEqual(message, 'Hello, World!')


class GiveMeFive(unittest.TestCase):

    def test_give_me_five(self):
        five = functions.give_me_five()
        self.assertEqual(five, five)


if __name__ == '__main__':
    unittest.main()
