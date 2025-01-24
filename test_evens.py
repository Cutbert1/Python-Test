import unittest
from evens import even_number_of_evens

class TestEvens(unittest.TestCase):
    def test_throws_error_if_value_passed_in_is_not_list(self):
        # Should Raise a TypeError if a list is not passed into the function
        # error message: "A list was not passed into the function"
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        # if the list is empty it will return False
        self.assertEqual(even_number_of_evens([]), False)
        # if the number of even numbers is even - return True
        self.assertEqual(even_number_of_evens([2, 4]), True)
        # if only one even number is passed - return False
        self.assertEqual(even_number_of_evens([2]), False)
        # if the number of odd numbers is odd - return False
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)

if __name__ == "__main__":
    unittest.main()


