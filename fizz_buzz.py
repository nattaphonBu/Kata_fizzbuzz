import unittest


class FizzBuzz(unittest.TestCase):
    def test_input_three_should_return_fizz(self):
        actual = calculate_fizzbuzz(3)
        expected = 'fizz'
        self.assertEqual(actual, expected)
    def test_input_six_should_return_fizz(self):
        actual = calculate_fizzbuzz(6)
        expected = 'fizz'
        self.assertEqual(actual, expected)
    
    def test_input_three_should_return_buzz(self):
        actual = calculate_fizzbuzz(5)
        expected = 'buzz'
        self.assertEqual(actual, expected)
    
    def test_input_ten_should_return_buzz(self):
        actual = calculate_fizzbuzz(10)
        expected = 'buzz'
        self.assertEqual(actual, expected)
    
    def test_input_1_should_return_1(self):
        actual = calculate_fizzbuzz(1)
        expected = 1
        self.assertEqual(actual, expected)
    
    def test_input_0_should_return_0(self):
        actual = calculate_fizzbuzz(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_input_15_should_return_fizzbuzz(self):
        actual = calculate_fizzbuzz(15)
        expected = 'fizzbuzz'
        self.assertEqual(actual, expected)
    
    def test_input_45_should_return_fizzbuzz(self):
        actual = calculate_fizzbuzz(45)
        expected = 'fizzbuzz'
        self.assertEqual(actual, expected)
    
    def test_input_2_should_return_2(self):
        actual = calculate_fizzbuzz(2)
        expected = 2
        self.assertEqual(actual, expected)

def calculate_fizzbuzz(number):
    if number == 0:
        return number
    if number % 15 == 0:
        return 'fizzbuzz'
    if number % 5 == 0:
        return 'buzz'
    if number % 3 == 0:
        return 'fizz'
    else:
        return number

if __name__ == '__main__':
    unittest.main()
